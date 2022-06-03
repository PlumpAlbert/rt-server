# vim:ft=python:ts=2:sw=0
# Author: Plump Albert (plumpalbert@gmail.com)
from dotenv import dotenv_values
import os

from dotenv.main import dotenv_values

ENV = {
    **dotenv_values('.env'),
    **dotenv_values('.env.local'),
    **os.environ
}

SQLALCHEMY_DATABASE_URI = "%s%s://%s:%s@%s:%s/%s" % (
    ENV['DB_CONNECTION_DIALECT'],
    '+%s' % ENV['DB_DRIVER'] if ENV['DB_DRIVER'] else '',
    ENV['DB_USERNAME'], ENV['DB_PASSWORD'],
    ENV['DB_HOST'], ENV['DB_PORT'],
    ENV['DB_DATABASE']
)

CSRF_ENABLED = True
CSRF_SESSION_KEY = ENV['APP_KEY']
SECRET_KEY = ENV['APP_KEY']
