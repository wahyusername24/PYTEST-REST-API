import requests
import json

from TokenGenerator import token_visitor
from TokenGenerator import base_url_dev, dev
from TokenGenerator import dev_api


#auth_token:
visitor_token = token_visitor()

#credential:
platform = "web"
country_code = ""
phone_code = ""
username = "thesigit7@gmail.com" #phone or email
password = "11112222" 
fullname = "TheSigit7" 
dob = "2000-04-25"
gender =  "male"

def generate_otp():
    try:
        url = base_url_dev + '/core-idp/api/v1/visitor/otp'
        print("post url: ", url)
        header = {'Authorization': visitor_token}
        apikeys = {'apikey': dev}

        data = {
            "username": username,
            "type": "registration",
            "signature_code": "A7kYlDVUViX",
            "platform": platform,
            "captcha":"03AAYGu2SP1E0oOp28jbR_aFNHorSUg5yEus_TvMX6FhLBx49j-iQvfifclBg3bFMUlKKTxALjm0CGphz7wkrCz2xwWBpNu6qlpWf86bbcjJXRrQOuG_nk2SJ10ze2cxpyp7BLqARjU1i5ZjSczySVss_vnhPybbyhVEvZqktmTct1HOBoysAb3AR6Enw4YjB6EqCOy6thuUDUa9LVyjgfOlr_RiqFhQ9J8liFlC7DyXuEeC8L9urL-C3opZXrc_-PPPY_30wleLxf2EKOrxhopWspD4lK5SOn06K-3r0pYXs4WWPdGDUQjvR8vkH3NEiCHyMPjKylJDp1awuW6ymqAlsMJEDpVTbIAjuz54QXAeZZ6sGNa0I8dtG6woT2uPQ5f6SrfZNkBt9YrthJ8aukqabj6KiQzbx73GoE3A8S4zEzgO6pqY2CxqpACZPrIfuV_QRQSmRVY2LPrS5LUDKTJInM3ObejrCZGO-x2S8LJ1w-6y19g6knkUiiUEO2CM041UT_dq_oCgyGIaSSHX8enqiJtERhe3Zq6w"
        }
        
        r = requests.post(url, headers={**header, **apikeys}, json=data)
        r.raise_for_status()
        j_data = r.json()
        j_str = json.dumps(j_data, indent=4)
        status_code = r.status_code
        assert status_code == 200

        otp = j_data['data']['otp']
        print("Status Code: ", status_code)
        print("Response Body: ", j_str)
        print("Your OTP: ", otp)

        return otp

    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)

def create_account(otp):
    try:
        url = dev_api + '/api/v3/register'
        header = {'Authorization': visitor_token}
        data = {
            "otp": otp,
            "country_code": country_code,
            "phone_code": phone_code,
            "username": username,
            "password": password, 
            "fullname": fullname, 
            "dob": dob,
            "gender": gender,
            "device_id": "1234567890"
        }

        r = requests.post(url, headers=header, json=data)
        r.raise_for_status
        j_data = r.json()
        j_str = json.dumps(j_data, indent=4)
        print('Response Body: ', j_str)
        assert r.status_code == 200 #general status code
        assert j_data['status']['code'] == 0 #inner status code
        assert j_data['data']['email'] == username
        assert j_data['data']['display_name'] == fullname
        assert j_data['data']['email_verified'] == 'yes'
        assert j_data['data']['username'] == username
        

    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)

# Call
create_account(generate_otp())