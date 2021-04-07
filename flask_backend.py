from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

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

@app.route('/users', methods = ['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        if search_username:
            return {'users_list' : 
                       [
                           user for user in users['users_list'] 
                           if user['name'] == search_username
                       ]
                   }
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)
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





