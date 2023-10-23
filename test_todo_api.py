import requests
import uuid
# pytest
# python -m pytest -v -s
# python -m pytest -v -s .\test_todo_api.py::test_can_list_task

base_url = "https://todo.pixegami.io"


def test_can_create_task():
    # create task
    payload = new_task_payload()
    create_task_response = create_task(payload)

    assert create_task_response.status_code == 200
    c_data = create_task_response.json()
    
    task_id = c_data['task']['task_id']
    
    # get task 
    get_task_response = get_task(task_id)

    assert get_task_response.status_code == 200
    g_data = get_task_response.json()
    assert g_data['content'] == payload['content']
    assert g_data['user_id'] == payload['user_id']

def test_can_update_task():
    # Create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
   
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    # Update the task
    new_payload = {
        "user_id": payload['user_id'],
        "task_id": task_id,
        "content": "my updated content",
        "is_done": True,
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    # Get and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()

    assert get_task_data['content'] == new_payload['content']
    assert get_task_data['is_done'] == new_payload['is_done']

def test_can_list_task():
    # Create N tasks
    n = 3
    payload = new_task_payload()
    for _ in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    # List tasks, and check that there are N items
    user_id = payload["user_id"]
    list_task_response = list_task(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()

    tasks = data["tasks"]
    assert len(tasks) == n

    pass

def test_can_delete_task():
    # Create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    # Delete the task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    # Get the task, and check that it's not found
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404 #400 indicates error from the client

def create_task(payload):
    return requests.put(base_url + '/create-task', json=payload)

def update_task(payload):
    return requests.put(base_url + '/update-task', json=payload)

def get_task(task_id):
    return requests.get(base_url + f'/get-task/{task_id}')

def list_task(user_id):
    return requests.get(base_url + f'/list-tasks/{user_id}')

def delete_task(task_id):
    return requests.delete(base_url + f"/delete-task/{task_id}")

def new_task_payload():
    user_id = f"test_user_ {uuid.uuid4().hex}"
    content = f"test_content_ {uuid.uuid4().hex}"
    return {
        "content": content,
        "user_id": user_id,
        "is_done": False,
    }

