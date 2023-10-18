import requests
import random
import json
import string


#base url:
base_url = "https://hera.mncplus.id/claim-monetization"

#Auth token:
auth_token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2aWQiOjY1MjAsInRva2VuIjoiZDJhNDhiNTk2ZDc5ZWNmOCIsInBsIjoibXdlYiIsImRldmljZV9pZCI6IjEifQ.KZ31oR5fiV0KmrYYyrsmRb9H1o5UtklYC5SqWEUhQKc"
api_key =  "43aCSi34YX5wUf4Fd3kb5Lbdvzwyx9f2" #abc


#GET
def get_request():
    
    try:
        url = base_url + "/music-claim/list-musics?page=1&length=10"
        print("get url: ", url)
        header = {'Authorization': auth_token}
        apikeys = {'apikey': api_key}

        r = requests.get(headers=header, params=apikeys)
        # r.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
        j_data = r.json()
        j_str = json.dumps(j_data, indent=4)

        sts_code = r.status_code
        print("Status Code: ", sts_code)
        print("GET Response Body API: ", j_str)
    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)

#Call
get_request()