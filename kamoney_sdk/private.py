from .endpoints_private.account import Account
from .endpoints_private.affiliates import Affiliates
from .endpoints_private.api import Api
from .endpoints_private.auth import Auth
from .endpoints_private.buy import Buy
from .endpoints_private.fee_and_reward import Fee_And_Reward
from .endpoints_private.level import Level
from .endpoints_private.merchant import Merchant
from .endpoints_private.order import Order
from .endpoints_private.payment_link import PaymentLink
from .endpoints_private.recipients import Recipients
from .endpoints_private.security import Security
from .endpoints_private.wallet import Wallet
from .endpoints_private.withdraw import Withdraw

import hmac
import hashlib
import requests
import random

class Private(Account, Affiliates, Api, Auth, Buy, Fee_And_Reward, Level, Merchant,
              Order, PaymentLink, Recipients, Security, Wallet, Withdraw):

    def __init__(self, public_key, secret_key):
        self.keys = {
            'public_key': public_key,
            'private_key': secret_key
        }
        
    

    def sign_request(self, data, secret_key):
        query_string = self.convert_to_query_string(data).encode()
        secret_key = secret_key.encode()
        sign = hmac.new(secret_key, query_string, hashlib.sha512).hexdigest()
        return sign


    def convert_to_query_string(self, params):
        nonce = round( ((random.random() * 1000) % 1000) ) # PRNG temporário
        if isinstance(params, dict):
            query_string = "&".join([f"{key}={value.replace(' ', '+')}" for key, value in params.items()])
            query_string = query_string + f'&nonce={nonce}'
            query_string = query_string[1:]
            print(f'nonce: {nonce}')
            print(f'query_string: {query_string}')
            return query_string
        else:
            raise Exception("You need give an dict object to convert!")
        

    def check_required_params(self, data):
        result = data
        if isinstance(data, dict) == False:
            raise Exception('check_required_params function need a param of type dict!')
        for key, value in data.items():
            if value == None:
                result.pop(key)
        return result


    def make_request(self, method, endpoint, data):
        headers = {
            'Content-Type': 'application/json',
            'pub': self.keys['public_key'],
            'sign': self.sign_request(data, self.keys['private_key'])
        }
        if method == 'get':
            req = requests.get(self.base_url+endpoint, headers=headers)
            response = req.json()
            return response
        elif method == 'post':
            req = requests.post(super().base_url+endpoint, json=data, headers=headers)
            response = req.json()
            return response            
        elif method == 'put':
            req = requests.put(super().base_url+endpoint, json=data, headers=headers)
            response = req.json()
            return response
        elif method == 'patch':
            req = requests.patch(super().base_url+endpoint, json=data, headers=headers)
            response = req.json()
            return response            
        elif method == 'delete':
            req = requests.delete(super().base_url+endpoint, json=data, headers=headers)
            response = req.json()
            return response
        else:
            raise Exception(f'Error: method {method} unsupported!')
        