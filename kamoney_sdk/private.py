from .account import Account
import hmac
import hashlib
import requests

class Private(Account):

    def __init__(self, public_key, secret_key):
        self.keys = {
            'public_key': public_key,
            'secret_key': secret_key
        }
    

    def sign_request(self, data, secret_key):
        if isinstance(data, str):
            data = data.encode('utf-8')
        if isinstance(secret_key, str):
            secret_key.encode('utf-8')
        sign = hmac.new(secret_key, self.convert_to_query_string(data), hashlib.sha512).hexdigest()
        return sign


    def convert_to_query_string(params):
        if isinstance(params, dict):
            query_string = "&".join([f"{key}={value.replace(' ', '+')}" for key, value in params.items()])
            return query_string
        else:
            raise Exception("You need give an dict object to convert!")
        
    def make_request(self, method, endpoint, data):
        if method == 'get':
            pass
        elif method == 'post':
            pass
