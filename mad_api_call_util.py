# Import this class and use the necessary methods based on response by chat bot

import requests, json

BASE_URL = 'http://testing.makeadiff.in/api/v1'
auth = ('username', 'password')

def get_credits(userid):
    resource = '/users/{}/credit'.format(userid)
    return requests.get(BASE_URL + resource, auth=auth)

def get_class_history(userid):
    resource = '/users/{}/past_classes'.format(userid)
    return requests.get(BASE_URL + resource, auth=auth)

def handle_response_extract_data(response):
    res = response.json()
    if res['status'] == 'success':
        return res['data']
