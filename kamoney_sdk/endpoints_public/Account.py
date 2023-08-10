class Account:

    def __init__(self):
        pass


    ## Account    
    def register(self, email: str, afiliate_code: str, terms: bool) -> dict:
        body = {
            'email': email,
            'affiliate_code': afiliate_code,
            'terms': terms
        }
        response = self.make_request('post',  f'{self.base_url}/register', body)
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
        response = self.make_request('post',  f'{self.base_url}/public/recovery', body)
        return response


    def recovery_account_confirm(self, email: str, code: str, password: str) -> dict:
        body = {
            'email': email,
            'code': code,
            'password': password
        }
        response = self.make_request('post',  f'{self.base_url}/public/recovery/confirm', body)
        return response
