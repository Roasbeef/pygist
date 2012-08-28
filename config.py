import os
import sys
import ConfigParser
import json
import requests

from clint.textui import colored, puts

config_file = os.path.expanduser('~/.config/pygist/config.ini')

config = ConfigParser.ConfigParser()


def write_config():

    with open(config_file, 'w') as file:
        config.write(file)


def make_config():
    if os.path.exists(config_file):
        pass
    else:
        os.makedirs(os.path.dirname(config_file))
        open(config_file, 'w').close()
        config.add_section('pygist')
        config.set('pygist', 'username', '')
        config.set('pygist', 'password', '')
        config.set('pygist', 'token', '')
        return config


def get_token():
    config.read(config_file)
    return config.get('pygist', 'token')


def get_username():
    config.read(config_file)
    return config.get('pygist', 'username')


def get_password():
    config.read(config_file)
    return config.get('pygist', 'password')


def set_password(password):
    config.set('pygist', 'password', password)
    write_config()


def set_token(token):
    config.set('pygist', 'token', token)
    write_config()


def set_username(username):
    config.set('pygist', 'username', username)
    write_config()


def login(username, password):
    body = json.dumps({'note': "pygist"})
    r = requests.post('https://api.github.com/authorizations', auth=(username, password),
                      data=body)
    if r.status_code == 201:
        puts(colored.green('You have successfully been authenticated with Github'))
    else:
        puts('{0}. {1}'.format(colored.blue('pygist'),
             colored.red('Invalid Credentials')))
        sys.exit(3)

    data = json.loads(r.content)
    token = data["token"]

    if get_username() == username:
        pass
    else:
        set_username(username)

    if get_password() == password:
        pass
    else:
        set_password(password)

    if get_token == token:
        pass
    else:
        set_token(token)


def have_auth_info():
    get_username() != '' and get_token() != ''
