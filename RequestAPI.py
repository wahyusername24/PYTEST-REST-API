import requests
import random
import json
import string

#base url:
base_url = "https://gorest.co.in"

#Auth token:
auth_token = "Bearer ea00fd8ea0c3b9d9f1280caf1d6f2ccf423c1f1b93869e33ae1b0d86913c8027"

#GenerateRandomEmail
def generate_random_email():
    domain = 'automation.com'
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + '@' + domain
    return email

#GET Request
def get_request():
    url = base_url + "/public/v2/users/"
    print("GET url:" , url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    stscode = response.status_code
    print("Your status code: ", stscode)

    assert response.status_code == 200
    json_data = response.json() 
    json_str = json.dumps(json_data, indent=4)
    print("Response Body API: ", json_str) 

#POST Request
def post_request():
    url = base_url +  "/public/v2/users/"
    print("POST url:" , url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "John Frusciante",
        "email": generate_random_email(),  
        "gender": "male",
        "status": "active"
    }
    r = requests.post(url, json=data, headers=headers)
    stscode = r.status_code
    json_data = r.json()
    json_str = json.dumps(json_data, indent=4)

    print("Your status code: ", stscode)
    print("Response Body API: ", json_str)

    assert r.status_code == 201
    assert "name" in json_data #make sure the response return "name" after creating data
    assert json_data['name'] == 'John Frusciante' #match the result
    user_id = json_data['id'] #make it reusable for PUT Request
    print("user_id ===>", user_id)
    return user_id

#PUT Request
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("PUT url:" , url)
    headers = {"Authorization": auth_token} 
    data = { 
        "name": "Kurt Cobain",
        "email": generate_random_email(),  
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    s_code = response.status_code
    print("Your status code: ", s_code)
    print("Response Body API: ", json_str)
    assert response.status_code == 200
    assert "name" in json_data
    assert json_data['id'] == user_id #Verify that after changes, id remains the same
    assert json_data['name'] == "Kurt Cobain"
    print("UPDATE USER SUCCESS...")
    # uid = json_data['id']
    # return uid

#DELETE Request
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("DELETE url:" , url)
    headers = {"Authorization":auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("Your status code: ", response.status_code)
    print("DELETE USER SUCCESS...")


#Call the function
get_request()
put_request(post_request())
delete_request(post_request())
