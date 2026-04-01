from contextlib import nullcontext

import pytest
import os
import requests
import json

from  Utility.main import get_request_data ,base_url,get_updated_request_data ,get_variable ,compare_response_data,return_random_str,global_dict,admin_auth,headers


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
variables_data_path=os.path.join(BASE_DIR, "Utility", "variable_jsons")
# setting test user before running the tests and unsetting it after the tests are done

def create_test_user(roles=None):
    """Helper function to create a test user with specified roles"""
    if roles is None:
        roles = ["ROLE_SYS_ADMIN"]

    request_data = get_request_data('create_user_for_test.json', global_dict, variables_data_path)

    # Update with roles
    fields_to_update = {
        "userRoleList": roles
    }

    updated_data = get_updated_request_data(request_data, fields_to_update)

    request_url = base_url + "/xusers/secure/users"
    resp = requests.post(request_url, verify=False, auth=admin_auth, headers=headers, data=json.dumps(updated_data))
    return resp.json()


# Create user objects with different roles
user1 = create_test_user(["ROLE_SYS_ADMIN"])
user2 = create_test_user(["ROLE_USER"])
user3 = create_test_user(["ROLE_USER"])
user4 = create_test_user(["ROLE_ADMIN_AUDITOR"])
user5 = create_test_user(["ROLE_KEY_ADMIN_AUDITOR"])




