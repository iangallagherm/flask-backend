from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

users = { 
    'users_list' :
    [
        { 
            'id' : 'xyz789',
            'name' : 'Charlie',
            'job': 'Janitor',
        },
        {
            'id' : 'abc123', 
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id' : 'ppp222', 
            'name': 'Mac',
            'job': 'Professor',
        }, 
        {
            'id' : 'yat999', 
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        {
            'id' : 'zap555', 
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}

def random_user_id():
    chars = ''.join([chr(random.randint(97, 122)) for i in range(3)])
    nums = ''.join([str(random.randint(0, 9)) for i in range(3)])
    return chars + nums

@app.route('/users', methods = ['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')
        user_search_list = users 
        if search_username:
            user_search_list = {'users_list' : 
                       [
                           user for user in user_search_list['users_list'] 
                           if user['name'] == search_username
                       ]
                   }
        if search_job:
            user_search_list = {'users_list' : 
                       [
                           user for user in user_search_list['users_list'] 
                           if user['job'] == search_job
                       ]
                   }
        return user_search_list
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd['id'] = random_user_id();
        users['users_list'].append(userToAdd)
        resp = jsonify(
            success = True,
            data = userToAdd
            )
        resp.status_code = 201
        return resp

@app.route('/users/<id>', methods = ['GET', 'DELETE'])
def get_user(id):
    if request.method == 'GET':
        if id:
            for user in users['users_list']:
                if user['id'] == id:
                    return user
            return ({})
        return users
    elif request.method == 'DELETE':
        if id:
            for user in users['users_list']:
                if user['id'] == id:
                    users['users_list'].remove(user)
                    resp = jsonify(success=True)
                    return resp
        resp = jsonify(success=False)
        resp.status_code = 406
        return resp

