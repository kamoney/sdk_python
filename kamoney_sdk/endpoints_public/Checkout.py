class Checkout:
    def __init__(self):
        pass

        
    def create_checkout(self, merchant_id: str, amount: float, email: str, callback:str, order_id:str, additional_info:str, redirect:str) -> dict:
        body = {
            'merchant_id': merchant_id,
            'amount': amount,
            'email': email,
            'callback': callback,
            'order_id': order_id,
            'additional_info': additional_info,
            'redirect': redirect
        }
        request = self.make_public_request('post', '/public/merchant/checkout', body)
        
        return response


    def get_checkout_info(self, id: str):
        response = self.make_public_request('get',  '/public/merchant/{id}')
        
        return response  