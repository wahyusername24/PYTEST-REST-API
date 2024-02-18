import requests
import json
import pytest
from faker import Faker
from TokenGenerator import token_visitor, base_url_dev, base_url_rc, base_url_prod, dev_api, rc_api, prod_api, dev, rc, prod

fake = Faker()

def generate_random_credentials():
    random_fullname = fake.user_name()
    random_email = random_fullname + "@gmail.com"
    return random_email, random_fullname

def test_create_account():
    email, fullname = generate_random_credentials()
    password = "11112222"
    dob = "2000-04-25"
    gender = "male"
    
    # Define Environment
    base_url_idp = base_url_dev
    base_url_api = dev_api
    apikey = dev

    try:
        platform = "web"
        country_code = ""
        phone_code = ""
        
        # Generate OTP
        otp_url = base_url_idp + '/core-idp/api/v1/visitor/otp'
        otp_data = {
            "username": email,
            "type": "registration",
            "signature_code": "A7kYlDVUViX",
            "platform": platform,
            "captcha": "03AAYGu2SP1E0oOp28jbR_aFNHorSUg5yEus_TvMX6FhLBx49j-iQvfifclBg3bFMUlKKTxALjm0CGphz7wkrCz2xwWBpNu6qlpWf86bbcjJXRrQOuG_nk2SJ10ze2cxpyp7BLqARjU1i5ZjSczySVss_vnhPybbyhVEvZqktmTct1HOBoysAb3AR6Enw4YjB6EqCOy6thuUDUa9LVyjgfOlr_RiqFhQ9J8liFlC7DyXuEeC8L9urL-C3opZXrc_-PPPY_30wleLxf2EKOrxhopWspD4lK5SOn06K-3r0pYXs4WWPdGDUQjvR8vkH3NEiCHyMPjKylJDp1awuW6ymqAlsMJEDpVTbIAjuz54QXAeZZ6sGNa0I8dtG6woT2uPQ5f6SrfZNkBt9YrthJ8aukqabj6KiQzbx73GoE3A8S4zEzgO6pqY2CxqpACZPrIfuV_QRQSmRVY2LPrS5LUDKTJInM3ObejrCZGO-x2S8LJ1w-6y19g6knkUiiUEO2CM041UT_dq_oCgyGIaSSHX8enqiJtERhe3Zq6w"
        }

        r_otp = requests.post(otp_url, json=otp_data, headers={'Authorization': token_visitor(), 'apikey': apikey})
        r_otp.raise_for_status()
        j_data = r_otp.json()
        j_str = json.dumps(j_data, indent=4)
        status_code = r_otp.status_code
        otp = j_data['data']['otp']
        assert status_code == 200

        # Create Account
        register_url = base_url_api + '/api/v3/register'
        register_data = {
            "otp": otp,
            "country_code": country_code,
            "phone_code": phone_code,
            "username": email,
            "password": password,
            "fullname": fullname,
            "dob": dob,
            "gender": gender,
            "device_id": "1234567890"
        }

        r_register = requests.post(register_url, json=register_data, headers={'Authorization': token_visitor()})
        r_register.raise_for_status()
        stsCode = r_register.status_code
        j_data2 = r_register.json()
        j_str2 = json.dumps(j_data2, indent=4)
        token = j_data2['data']['access_token']
        print("Register Status Code: ", stsCode)
        print(j_str2)

        # Assertions
        assert r_register.status_code == 200
        assert j_data2['status']['code'] == 0
        assert j_data2['data']['email'] == email
        assert j_data2['data']['display_name'] == fullname
        assert j_data2['data']['email_verified'] == 'yes'
        assert j_data2['data']['username'] == email
        return token, email, password
    
    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)

# if __name__ == "__main__":
#     test_create_account()
        