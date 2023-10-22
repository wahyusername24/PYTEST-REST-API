import requests
import json

#Platform 
# mweb, web, android, ios

#Base URL
base_url_dev = 'https://hera.mncplus.id'
base_url_rc = 'https://hermes.mncplus.id'
dev_api = 'https://dev-api.rctiplus.com'
rc_api = 'https://rc-api.rctiplus.com'

#Apikey
dev = '43aCSi34YX5wUf4Fd3kb5Lbdvzwyx9f2'
rc = 'pHuoiDJvkh5d6CmmlNdUWVMSPLYTocCp'

def token_visitor():
    try:
        uri = base_url_dev + '/video/api/v1/visitor?platform=mweb'
        api_key = {'apikey':dev}
        r = requests.get(url=uri, headers=api_key)
        j_data = r.json()
        print('')
        print('Token Visitor:')
        visitor = j_data['data']['access_token']
        print(visitor)
        return visitor

    except requests.exceptions.RequestException as e:
        print('Request Exception:', e)


def token_login(visitor):
    url = dev_api + '/api/v3/login'
    header = {'Authorization':visitor}
    apiKey = {'apikey': dev}
    data = {
    "username": "apritadhita@gmail.com",
    "phone_code": "",
    "password": "dhita229",
    "device_id": "1",
    "platform": "mweb"
    }
    r = requests.post(url, headers={**header, **apiKey}, json=data)
    j_data = r.json()
    print('')
    print('Token Login:')
    login = j_data['data']['access_token']
    print(login)


# Call
# token_visitor()
token_login(token_visitor())