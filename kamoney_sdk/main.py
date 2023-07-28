import requests

class Kamoney:

    def __init__(self):
        self.authorization = None
        self.base_url = 'https://api2.kamoney.com.br/v2'
    
    ## Services
    def get_status_order(self) -> dict:
        request = requests.get(f'{self.base_url}/public/services/order')
        response = request.json()
        return response
    
    def get_status_merchant(self) -> dict:
        request = requests.get(f'{self.base_url}/public/services/merchant')
        response = request.json()
        return response
    
    def get_status_buy(self) -> dict:
        request = requests.get(f'{self.base_url}/public/services/buy')
        response = request.json()
        return response

    ## Authorization
    def login(self, email: str, password: str) -> dict:
        body = {
            'email':email,
            'password': password
        }
        request = requests.get(f'{self.base_url}/public/auth', json=body)
        response = request.json()
        if response['success'] == True:
            self.authorization = response['data']['token']

        return response
    
    
    def confirm_2fa(self, tfa: str) -> dict:
        body = {
            'token':self.authorization,
            'tfa':tfa
        }
        request = requests.post(f'{self.base_url}/auth/tfs', json=body)
        response = request.json()
        return response
    
    ## Account    
    def register(self, email: str, afiliate_code: str, terms: bool) -> dict:
        body = {
            'email': email,
            'affiliate_code': afiliate_code,
            'terms': terms
        }
        request = requests.post(f'{self.base_url}/register', json=body)
        response = request.json()
        return response.json()


    def active_account(self, email: str, code: str, password: str):    
        body = {
            'email': email,
            'code': code,
            'password': password
        }
        request = request.post(f'{self.base_url}/active', json=body)
        response = request.json()
        return response
    

    def recovery_account(self, email: str) -> dict:
        body = {
            'email': email
        }
        request = requests.post(f'{self.base_url}/public/recovery', data=body)
        response = request.response()
        return response
    

    def recovery_account_confirm(self, email: str, code: str, password: str) -> dict:
        body = {
            'email': email,
            'code': code,
            'password': password
        }
        request = requests.post(f'{self.base_url}/public/recovery/confirm', data=body)
        response = request.json()
        return response
    
    ## Utils
    def get_bank(self) -> dict:
        request = requests.get(f'{self.base_url}/public/bank')
        response = request.json()
        return response
    

    def get_info(self) -> dict:
        request = requests.get(f'{self.base_url}/public/system/info')
        response = request.json()
        return response
    

    def get_notification(self) -> dict:
        request = requests.get(f'{self.base_url}/public/notification')
        response = request.json()
        return response
    

    def get_country(self) -> dict:
        request = requests.get(f'{self.base_url}/public/country')
        response = request.json()
        return response.json()
    

    def get_state(self, country_id: int) -> dict:
        request = requests.get(f'{self.base_url}/public/country/{country_id}/state')
        response = request.json()
        return response
    

    def get_city(self, country_id: int, state_id: int) -> dict:
        request = requests.get(f'{self.base_url}/public/country/{country_id}/state/{state_id}/city')
        response = request.json()
        return response
    

    def get_currency(self) -> dict:
        request = requests.get(f'{self.base_url}/public/currency')
        response = request.json()
        return response
    
    
    def get_network(self, asset: str) -> dict:
        request = requests.get(f'{self.base_url}/public/{asset}')
        response = request.json()
        return response
    

    def get_faq(self) -> dict:
        request = requests.get(f'{self.base_url}/public/faq')
        response = request.json()
        return response
    

    def get_product(self) -> dict:
        request = requests.get(f'{self.base_url}/public/product')
        response = request.json()
        return response
    

    def get_contact(self, name: str, email: str, subject: str, message: str) -> dict:
        body = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        request = requests.post(f'{self.base_url}/public/contact', data=body)
        response = request.json()
        return response
    

    def get_pix_types(self) -> dict:
        request = requests.get(f'{self.base_url}/public/pixtype')
        response = request.json()
        return response
    

    def get_affiliate(self) -> dict:
        request = requests.get(f'{self.base_url}/public/affiliate')
        response = request.json()
        return response
    

    def get_status(self) -> dict:
        request = requests.get(f'{self.base_url}/public/status')
        response = request.json()
        return response
    

    def get_coupon(self, coupon: str) -> dict:
        request = requests.get(f'{self.base_url}/public/coupon/{coupon}')
        response = request.json()
        return response
    

    def get_fee(self) -> dict:
        request = requests.get(f'{self.base_url}/public/fee')
        response = request.json()
        return response
    

    def get_buy_wallet_types(self) -> dict:
        request = requests.get(f'{self.base_url}/public/buy/wallet/type')
        response = request.json()
        return response
    

    def get_buy_payment_category(self) -> dict:
        request = requests.get(f'{self.base_url}/public/buy/payment/category')
        response = request.json()
        return response
    

    def get_buy_payment_category_types(self, code: str) -> dict:
        request = requests.get(f'{self.base_url}/public/buy/payment/category/{code}')
        response = request.json()
        return response
    

    def get_reward(self) -> dict:
        request = requests.get(f'{self.base_url}/public/reward')
        response = request.json()
        return response
    

    #Payment Link
    def get_payment_link(self, hash: str) -> dict:
        request = requests.get(f'{self.base_url}/public/merchant/payment/{hash}')
        response = request.json()
        return response
    

    def create_payment_link(self, hash: str) -> dict:
        request =  requests.post(f'{self.base_url}/public/merchant/paymentlink/{hash}')
        response = request.json()
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
        request = requests.post(f'{self.base_url}/public/merchant/checkout', data=body)
        response = request.json()
        return response
    

    def get_checkout_info(self, id: str):
        request = requests.get(f'{self.base_url}/public/merchant/{id}')
        response = request.json()
        return response


    def _check_token(self):
        if self.authorization == None:
            raise Exception('You need be authenticated to call a private method!')        

    #Private
    def validate_token(self) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        request = requests.get(f'{self.base_url}/private/auth/validate', headers=headers)
        response = request.json()
        return response
    

    def get_account_info(self) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        request = requests.get(f'{self.base_url}/private/account', headers=headers)
        response = request.json()
        return response
    
    # 
    def change_account_info(self, name: str, personal_id: str, date_of_birth: str) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        request = requests.post(f'{self.base_url}/private/account', headers=headers)
        response = request.json()
        return response
    

    # /private/account/locality
    def get_account_locality(self) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        request = requests.post(f'{self.base_url}/private/account/locality', headers=headers)
        response = request.json()
        return response
    
    
    # /private/account/locality
    def change_account_locality(self, zipcode: str, street: str, number: str, complement: str, neighborhood, city: int, state: int) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        body = {
            'zipcode': zipcode,
            'street': street,
            'number': number,
            'complement': complement,
            'neighborhood': neighborhood,
            'city': city,
            'state': state
        }
        request = requests.post(f'{self.base_url}/private/account/locality', json=body, headers=headers)
        response = request.json()
        return response
    

    # /private/account/contact
    def change_account_contact(self, whatsapp: str, telegram: str) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        body = {
            'whatsapp': whatsapp,
            'telegram': telegram
        }
        request = requests.post(f'{self.base_url}/private/account/contact', headers=headers, data=body)
        response = request.json()
        return response
    

    # /private/account/history
    def get_account_history(self) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        request = requests.get(f'{self.base_url}', headers=headers)
        response = request.json()
        return response
    
    
    # /private/account/notification
    def get_account_history(self) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        request = requests.get(f'{self.base_url}/private/account/notification', headers=headers)
        response = request.json()
        return response
    

    # /private/account/notification
    def get_account_notifications(self, id=None) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        if id == None:
            request = requests.get(f'{self.base_url}/private/account/notification')
        else:
            request = requests.get(f'{self.base_url}/private/account/notification?id={id}')
        response = request.json()
        return response
    

    # /private/account/notification
    def mark_notifications_as_read(self):
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        requests.put(f'{self.base_url}/private/account/notification', headers=headers)
        return
