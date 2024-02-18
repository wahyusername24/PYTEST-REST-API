import requests
import json

from TokenGenerator import token_visitor, base_url_dev, base_url_rc, base_url_prod, dev_api, rc_api, prod_api, dev, rc, prod
from test_register_account import test_create_account

# Define Environment
base_url_idp = base_url_dev
base_url_api = dev_api
apikey = dev
platform = 'web'
token, email, password = test_create_account() 
username = email
password = password

def generate_otp():
    try:
        url = base_url_idp + '/core-idp/api/v1/visitor/otp'
        print("post url: ", url)
        header = {'Authorization': token_visitor()}
        apikeys = {'apikey': apikey}

        data = {
            "username": username,
            "type": "delete-profile",
            "signature_code": "A7kYlDVUViX",
            "platform": "web",
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

def test_delete_account():
    otp = generate_otp()
    url = base_url_idp + '/core-idp/api/v1/user'
    header = {'Authorization': token}
    apikeys = {'apikey': apikey}

    data = {
        "otp" : otp
    }

    r = requests.delete(url, headers={**header,**apikeys}, json=data)
    r.raise_for_status()
    sts_code = r.status_code
    print("Status Code: ",sts_code)
    j_data = r.json()
    j_str = json.dumps(j_data, indent=4)
    print('Response Body: ', j_str)
    assert sts_code == 200

if __name__ == "__main__":
    test_delete_account()