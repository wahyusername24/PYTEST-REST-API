import requests
import json

#Platform 
# mweb, web, android, ios

#Base URL
base_url_dev = 'https://hera.mncplus.id'
base_url_rc = 'https://hermes.mncplus.id'
base_url_prod = 'https://zeus.rcti.plus'
dev_api = 'https://dev-api.rctiplus.com'
rc_api = 'https://rc-api.rctiplus.com'
prod_api = 'https://api.rctiplus.com'

#Apikey
dev = '43aCSi34YX5wUf4Fd3kb5Lbdvzwyx9f2'
rc = 'pHuoiDJvkh5d6CmmlNdUWVMSPLYTocCp'
prod = 'k1DzR0yYWIyZgvTvixiDHnb4Nl08wSU0'

#Credential
username = 'christophermcdonald@gmail.com'
password = '11112222'
platform = 'web'

def token_visitor():
    try:
        uri = f"{base_url_dev}/video/api/v1/visitor?platform={platform}"
        api_key = {'apikey':dev}
        r = requests.get(url=uri, headers=api_key)
        j_data = r.json()
        visitor = j_data['data']['access_token']
        print('')
        # print('Token Visitor:')
        # print(visitor)
        return visitor

    except requests.exceptions.RequestException as e:
        print('Request Exception:', e)


def login_core_api(visitor):
    url = dev_api + '/api/v3/login'
    header = {'Authorization':visitor}
    apiKey = {'apikey': dev}
    data = {
        "username": "wahyupanji240@gmail.com",
        "phone_code": "",
        "password": "qwerty12345",
        "device_id": "1",
        "platform": "web"
    }
    r = requests.post(url, headers={**header, **apiKey}, json=data)
    j_data = r.json()
    login = j_data['data']['access_token']
    print('')
    print('Token Login Core-API:')
    print(login)
    print('')
    return login

def login_core_idp(visitor):
    url = base_url_dev + '/core-idp/api/v1/visitor/login'
    header = {'Authorization':visitor}
    apiKey = {'apikey':dev}
    data = {
        "username": username,
        "password": password,
        "device_id": "3463784",
        "platform": platform
    }
    r = requests.post(url, headers={**header, **apiKey}, json=data)
    j_data = r.json()
    print("Status Code Core-IDP: ", r.status_code)

    login = j_data['data']['access_token']
    assert r.status_code == 200 #general status code
    assert j_data['status']['code'] == 0 #inner status code
    print('')
    # print('Token Login Core-IDP:')
    # print(login)
    print('')
    return login

# Call
# login_core_api(token_visitor())
# login_core_idp(token_visitor())