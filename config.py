from _typeshed import OpenBinaryMode
import os


class config(object):
    SECRET_PY = os.environ.get('SECRET_KEY') or "secret_string"

    MONGODB_SETTINGS = {'db': 'vcloth'}
