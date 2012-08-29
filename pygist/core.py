import requests

from clint.textui import colored, puts, columns
from .config import get_token, get_username, get_password, have_auth_info

import json
import sys


def get_auth_header():
    auth = {"Authorization": "token %s" % get_token()}
    return auth


def delete_gist(gist_id):
    delete_url = 'https://api.github.com/gists/%s' % (gist_id)
    if not have_auth_info:
        puts('{0}. {1}'.format(colored.blue('pygist'),
             colored.green('You need to login to do that ')))
        sys.exit(-1)

    username = get_username()
    password = get_password()
    r = requests.delete(delete_url, auth=(username, password))
    if r.status_code == 204:
        puts('{0}. {1}'.format(colored.blue('pygist'),
            colored.green('gist: %s deleted successfully' % gist_id)))
    else:
        puts('{0}. {1}'.format(colored.blue('pygist'),
             colored.red("You either passed a gist that isn't yours"
                         "or you need to login silly.")))
        sys.exit(-1)


def get_clipboard():
    import subprocess
    data = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    return data.communicate()[0]


def create_gist(files=None, description=None, paste=False):
    post_url = 'https://api.github.com/gists'
    username = get_username()
    password = get_password()

    post_dict = {'description': description, 'public': True}
    if paste:
        post_dict['files'] = {description: {'content': get_clipboard()}}
    else:
        file_name = lambda x: x.split('/')[-1]
        post_dict['files'] = dict((file_name(file), {'content': open(file).read()}) for file in files)

    r = requests.post(post_url, auth=(username, password), data=json.dumps(post_dict))
    if r.status_code == 201:
        post_resp = json.loads(r.content)
        puts('{0}. {1}'.format(colored.blue('pygist'),
             colored.green('gist: %s created successfully' % post_resp['id'])))
    else:
        puts('{0}. {1}'.format(colored.blue('pygist'),
             colored.green('You need to login to create a gist')))
        sys.exit(-1)
