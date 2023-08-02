from .decorators import Private

class Wallet:

    def __init__(self):
        pass


    @Private
    def list_account_wallets(self, page=None) -> dict:
        if page == None:
            response = self.make_request('get', '/private/wallet', {})
        else:
            response = self.make_request('get', f'/private/wallet?page={page}', {})
        return response
    

    @Private
    def get_wallet_extract(self, page=None, begin=None, end=None, search=None, type=None) -> dict:
        # ...
        return