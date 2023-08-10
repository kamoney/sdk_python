import requests

class Public:
    def __init__(self):
        pass

    def make_request(self, method, endpoint, data):
        headers = {
            'Content-Type': 'application/json'
        }
        if method == 'get':
            req = requests.get(super().base_url+endpoint, json=data, headers=headers)
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


    ## Authorization
    def login(self, email: str, password: str) -> dict:
        body = {
            'email':email,
            'password': password
        }
        response = self.make_request('get',  f'{self.base_url}/public/auth', body)
        
        if response['success'] == True:
            self.authorization = response['data']['token']

        return response


    def confirm_2fa(self, tfa: str) -> dict:
        body = {
            'token':self.authorization,
            'tfa':tfa
        }
        request = self.make_request('post', f'{self.base_url}/auth/tfs', body)
        
        return response


    ## Account    
    def register(self, email: str, afiliate_code: str, terms: bool) -> dict:
        body = {
            'email': email,
            'affiliate_code': afiliate_code,
            'terms': terms
        }
        request = self.make_request('post', f'{self.base_url}/register', body)
        
        return response


    def active_account(self, email: str, code: str, password: str):    
        body = {
            'email': email,
            'code': code,
            'password': password
        }
        response = self.make_request('post', f'{self.base_url}/active', body)
        
        return response


    def recovery_account(self, email: str) -> dict:
        body = {
            'email': email
        }
        response = self.make_request('post', f'{self.base_url}/public/recovery', body)
        return response


    def recovery_account_confirm(self, email: str, code: str, password: str) -> dict:
        body = {
            'email': email,
            'code': code,
            'password': password
        }
        response = self.make_reqquest('post', f'{self.base_url}/public/recovery/confirm', body)
        
        return response

    ## Utils
    def get_bank(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/bank')
        
        return response


    def get_info(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/system/info')
        
        return response


    def get_notification(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/notification')
        
        return response


    def get_country(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/country')
        
        return response


    def get_state(self, country_id: int) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/country/{country_id}/state')
        
        return response


    def get_city(self, country_id: int, state_id: int) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/country/{country_id}/state/{state_id}/city')
        
        return response


    def get_currency(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/currency')
        
        return response


    def get_network(self, asset: str) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/{asset}')
        
        return response


    def get_faq(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/faq')
        
        return response


    def get_product(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/product')
        
        return response


    def get_contact(self, name: str, email: str, subject: str, message: str) -> dict:
        body = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        response = self.make_request('post', f'{self.base_url}/public/contact', body)
        
        return response


    def get_pix_types(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/pixtype')
        
        return response


    def get_affiliate(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/affiliate')
        
        return response


    def get_status(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/status')
        
        return response


    def get_coupon(self, coupon: str) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/coupon/{coupon}')
        
        return response


    def get_fee(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/fee')
        
        return response


    def get_buy_wallet_types(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/buy/wallet/type')
        
        return response


    def get_buy_payment_category(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/buy/payment/category')
        
        return response


    def get_buy_payment_category_types(self, code: str) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/buy/payment/category/{code}')
        
        return response


    def get_reward(self) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/reward')
        
        return response


    #Payment Link
    def get_payment_link(self, hash: str) -> dict:
        response = self.make_request('get',  f'{self.base_url}/public/merchant/payment/{hash}')
        
        return response


    def create_payment_link(self, hash: str) -> dict:
        request =  requests.post(f'{self.base_url}/public/merchant/paymentlink/{hash}')
        
        return response


    #Checkout
    def create_checkout(self, merchant_id: str, amount: float, email: str, callback:str, order_id:str, additional_info:str, redirect:str) -> dict:
        body = {
            'merchant_id': merchant_id,
            'amount': amount,
            'email': email,
            'callback': callback,
            'order_id': order_id,
            'additional_info': additional_info,
            'redirect': redirect
        }
        request = self.make_request('post', f'{self.base_url}/public/merchant/checkout', body)
        
        return response


    def get_checkout_info(self, id: str):
        response = self.make_request('get',  f'{self.base_url}/public/merchant/{id}')
        
        return response  