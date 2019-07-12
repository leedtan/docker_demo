from flask import Flask
from flask import request
import json
import logging
import pdb
import random
from uuid import uuid4

app = Flask(__name__)

USERS = {}
SESSIONS = {}

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login(request.data)
    else:
        return show_the_login_form(request.data)

def show_the_login_form():
    pass
    
def do_the_login(data):
    dct = json.loads(data.decode('utf-8'))
    if 'username' not in dct:
        return 'user needs username'
    if 'pwd' not in dct:
        return 'user needs pwd'
    usr, pwd = dct['username'], dct['pwd']
    if usr not in USERS:
        return usr + ' does not exist'
    if pwd != USERS[usr]:
        return 'wrong password'
    sid= str(uuid4())
    SESSIONS[sid] = {'username':usr, 'enddate':None}
    return sid

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return do_the_register(request.data)
    else:
        return show_the_register_form(request.data)

def show_the_register_form():
    pass
    
def do_the_register(data):
    dct = json.loads(data.decode('utf-8'))
    if 'username' not in dct:
        return 'user needs username'
    if 'pwd' not in dct:
        return 'user needs pwd'
    usr, pwd = dct['username'], dct['pwd']
    if usr in USERS:
        return usr + ' already exists'
    
    USERS[usr] = pwd
    return '::' + usr + '::added with password::' + pwd + '::'



def main():
    app.run()


if __name__ == '__main__':
    main()