import requests

class Public:
    def __init__(self):
        pass

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