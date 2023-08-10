import requests
import hashlib
import hmac
from .private import Private
from .public import Public
'''
    A classe Private irá realizar a herança múltipla de todas as classes que implementam cada integração.

'''


class Kamoney(Public, Private):

    def __init__(self, public_key, secret_key):
        self.base_url = 'https://api2.kamoney.com.br/v2'
        super().__init__(public_key, secret_key)



    



    
    
        

