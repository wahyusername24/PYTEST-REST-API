import requests
import random
import json
import string

from TokenGenerator import token_visitor, token_login
from TokenGenerator import dev, rc

#base url:
base_url = "https://hera.mncplus.id/claim-monetization"

#Auth token:
visitor_token = token_visitor()
login_token = token_login(visitor_token)


#GET
def get_request():
    
    try:
        url = base_url + "/music-claim/list-musics?page=1&length=10"
        print("get url: ", url)
        header = {'Authorization': login_token}
        apikeys = {'apikey': dev}

        r = requests.get(url, headers={**header, **apikeys}) #merge the header and apikeys dictionaries into a single dictionary that is then passed as the headers argument to the requests.get() method.
        r.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
        j_data = r.json()
        j_str = json.dumps(j_data, indent=4)

        sts_code = r.status_code
        print("Status Code: ", sts_code)
        print("GET Response Body API: ", j_str)
        assert sts_code == 200

        for item in j_data['data']:
            assert 'id' in item
            assert 'label_id' in item
            assert 'title' in item
            assert 'artist' in item


    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)

#Call
get_request()