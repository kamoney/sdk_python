from .decorators import Private

class Api:

    def __init__(self):
        pass


    @Private
    def create_new_api_key(self) -> dict:
        response = self.make_request('post', '/private/security/api', {})
        return response
    

    @Private
    def list_api_keys(self, page=None) -> dict:
        body = {
            'page': page
        }
        body = self.check_required_params(body)
        response = self.make_request('get', '/private/security/api', {})
        return response
    

    @Private
    def delete_api_key(self, id:int) -> dict:
        response = self.make_request('delete', f'/private/security/api/{id}', {})
        return response
    

    # Voltar nessa função depois
    @Private
    def recover_secret_key(self, password: str, tfa=None):
        body = {
            'password': password,
            'tfa': tfa
        }
        body = self.check_required_params(body)
        response = self.make_request('post', '/private/security/api/145/secret')
        return response
    
    