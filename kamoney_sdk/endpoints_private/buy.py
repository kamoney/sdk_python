from ..utils.decorators import Private


class Buy:

    
    def __init__(self):
        pass



    @Private
    def create_buy(self, asset: str, network: str, amount: float, wallet_type: int, payment_method: str,
                   addr=None, password=None, password_compare=None) -> dict:
        body = {
            'asset': asset,
            'network': network,
            'amount': amount,
            'wallet_type': wallet_type,
            'payment_method': payment_method,
            'addr': addr,
            'password': password,
            'password_compare': password_compare
        }
        body = self.check_required_params(body)
        response = self.make_request('post', f'/private/buy', body)
        return response
    

    @Private
    def get_private_key(self, id:int, password: str, tfa: str) -> dict:
        body = {
            'password': password,
            'tfa': tfa
        }
        response = self.make_request('post', f'/private/buy/{id}/private', body)
        return response
    


    @Private
    def list_buy_info(self, id: int) -> dict:
        response = self.make_request('get', f'/private/buy/{id}', {})
        return response
    


    @Private
    def generate_new_qrcode(self, id: int) -> dict:
        response = self.make_request('get', f'/private/buy/{id}/payment_method/reset')
        return response


    