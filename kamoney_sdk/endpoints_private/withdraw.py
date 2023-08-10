from ..utils.decorators import Private

class Withdraw:

    def __init__(self):
        pass


    @Private
    def create_withdraw(self, asset: str, bank: int, agency: int, account: int,
                        type: str, amount: float, tfa: str) -> dict:
        body = {
            'asset':asset,
            'bank':bank,
            'agency':agency,
            'account':account,
            'type': type,
            'amount': amount,
            'tfa': tfa
        }
        response = self.make_request('post', '/private/wallet/withdraw', body)
        return response
    

    @Private
    def list_withdraw(self, page=None, begin=None, end=None, search=None, asset=None, status=None) -> dict:
        body = {
            'page': page,
            'begin': begin,
            'end': end,
            'search': search,
            'asset': asset,
            'status': status
        }
        body = self.check_required_params(body)
        response = self.make_request('get', '/private/wallet/withdraw', body)
        return response
    

    @Private
    def get_withdraw_info(self, id_withdraw: int) -> dict:
        response = self.make_request('get', f'/private/withdraw/{id_withdraw}', {})
        return response
    

    @Private
    def download_withdraw_receipt(self, withdraw_id: int, name_file: str) -> dict:
        response = self.make_request('get', f'/private/wallet/withdraw/{withdraw_id}/receipt/{name_file}', {})
        return response
    

    
    