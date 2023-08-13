import requests
from .endpoints_public.Account import Account
from .endpoints_public.Services import Services
from .endpoints_public.Utils import Utils
from .endpoints_public.PaymentLink import PaymentLink
from .endpoints_public.Checkout import Checkout
from .endpoints_public.Authorization import Authorization

class Public(Authorization, Account, Services, Utils, PaymentLink, Checkout):

    def __init__(self, public_key=None, private_key=None):
        pass


    def make_public_request(self, method, endpoint, data):
        headers = {
            'Content-Type': 'application/json'
        }
        if method == 'get':
            req = requests.get(self.base_url+endpoint, json=data, headers=headers)
            response = req.json()
            return response
        elif method == 'post':
            req = requests.post(self.base_url+endpoint, json=data, headers=headers)
            response = req.json()
            return response            
        elif method == 'put':
            req = requests.put(self.base_url+endpoint, json=data, headers=headers)
            response = req.json()
            return response
        elif method == 'patch':
            req = requests.patch(self.base_url+endpoint, json=data, headers=headers)
            response = req.json()
            return response            
        elif method == 'delete':
            req = requests.delete(self.base_url+endpoint, json=data, headers=headers)
            response = req.json()
            return response
        else:
            raise Exception(f'Error: method {method} unsupported!')

