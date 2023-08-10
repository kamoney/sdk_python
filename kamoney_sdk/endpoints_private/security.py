from ..utils.decorators import Private

class Security:

    def __init__(self):
        pass

    
    @Private
    def anti_phishing(self, password: str, tfa=None) -> dict:
        body = {
            'password': password,
            'tfa': tfa
        }
        body = self.check_required_params(body)
        response = self.make_request('post', '/private/security/antiphishing', body)
        return response
    
    
    @Private
    def get_anti_phishing_phrase(self, password: str, phrase: str, tfa=None) -> dict:
        body = {
            'password': password,
            'phrase': phrase,
            'tfa': tfa
        }
        body = self.check_required_params(body)
        response = self.make_request('post', '/private/security/antiphishing/view', body)
        return response
    

    @Private
    def get_tfa(self) -> dict:
        response = self.make_request('get', '/private/security/tfs', {})
        return response
    

    @Private
    def change_tfa(self, password: str, tfa: str) -> dict:
        '''
            Após o uso dessa função, será enviado um email para o proprietário da conta com um código
            de confirmação, que deverá ser utilizado na função confirm_action para confirmar a ativação
            ou desativação do 2fa.
        '''
        response = self.make_request('post', '/private/security/tfs', {})
        return response
    

    @Private
    def change_account_email(self, email: str, password: str) -> dict:
        body = {
            'email': email,
            'password': password
        }
        response = self.make_request('post', '/private/security/email', body)
        return response
    

    @Private
    def change_account_password(self, password: str, password_new: str, password_confirm: str) -> dict:
        body = {
            'password': password,
            'password_new': password_new,
            'password_confirm': password_confirm            
        }
        response = self.make_request('post', '/private/security/password', body)
        return response
    

    @Private
    def confirm_action(self, code: str) -> dict:
        body = {
            'code': code
        }
        response = self.make_request('post', '/private/security/action', body)
        return response
    

    # Ainda não finalizada.
    @Private
    def cancel_account_delete(self, password: str) -> dict:
        body = {
            'password': password
        }
        response = self.make_request('post', '/private/security/cancel', body)
        return response
    