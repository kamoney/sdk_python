from ..utils.decorators import Private


class Merchant:


    def __init__(self):
        pass



    @Private
    def create_merchant(self, asset: str, network: str, amount=None, email=None, callback=None,
                        additional_info=None, redirect=None):
        body = {
            'asset': asset,
            'network': network,
            'amount': amount,
            'email': email,
            'callback': callback,
            'additional_info': additional_info,
            'redirect': redirect
        }
        body = self.check_required_params(body)
        response = self.make_request('post', f'/private/merchant', body)
        return response
    


    @Private
    def list_merchant(self, page=None, begin=None, end=None, search=None, status=None) -> dict:
        body = {
            'page': page,
            'begin': begin,
            'end': end,
            'search': search,
            'status': status
        }
        body = self.check_required_params(body)
        response = self.make_request('get', '/private/merchant', body)
        return response
    


    @Private
    def get_merchant_info(self, id: int) -> dict:
        response = self.make_request('get', f'/private/merchant/{id}', {})
        return response
