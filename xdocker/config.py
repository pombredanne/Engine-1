import os

ROOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)
DATA_DIRECTORY = os.path.join(ROOT_PATH, os.pardir, 'data')
USER_DIRECTORY = os.path.join(DATA_DIRECTORY, 'users')
LOG_DIRECTORY = 'logs'

for direc in (DATA_DIRECTORY, USER_DIRECTORY, LOG_DIRECTORY):
    if not os.path.exists(direc):
        os.mkdir(direc)

# Webservice part

DEBUG = True
APP_HOST = '0.0.0.0'
APP_PORT = 5000


# Worker part

SECURITY_GROUP_NAME = 'xervmon'
KEY_NAME = 'xervmon'
KEY_EXTENSION = '.pem'

SSH_PORT = 22
HTTP_PORT = 80
HTTPS_PORT = 443
