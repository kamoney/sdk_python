from .decorators import Private

class PaymentLink:


    def __init__(self):
        pass



    @Private
    def create_payment_link(self, label: str, amount: float) -> dict:
        body = {
            'label': label,
            'amount': amount
        }
        response = self.make_request('post', '/private/merchant/paymentlink', body)
        return response
    

    @Private
    def list_payment_link(self, page=None, begin=None, end=None, search=None) -> dict:
        body = {
            'page': page,
            'begin': begin,
            'end': end,
            'search': search
        }
        response = self.make_request('get', f'/private/merchant/paymentlink/{id}', body)
        return response
    

    @Private
    def delete_payment_link(self, id: int) -> dict:
        response = self.make_request('delete', f'/private/merchant/paymentlink/{id}', {})
        return response
    