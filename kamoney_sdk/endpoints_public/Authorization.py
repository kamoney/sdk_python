class Authorization:

    def __init__(self):
        pass


    def login(self, email: str, password: str) -> dict:
        body = {
            'email':email,
            'password': password
        }
        response = self.make_public_request('get',  '/public/auth', body)
        
        if response['success'] == True:
            self.authorization = response['data']['token']

        return response


    def confirm_2fa(self, tfa: str) -> dict:
        body = {
            'token':self.authorization,
            'tfa':tfa
        }
        request = self.make_public_request('post', '/auth/tfs', body)
        
        return response

