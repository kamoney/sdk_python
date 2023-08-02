from .decorators import Private

class Level:

    def __init__(self):
        pass

    def get_account_limit(self) -> dict:
        response =  self.make_request('get', '/private/account/limit', {})
        return response
    
    