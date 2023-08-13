class PaymentLink:

    def __init__(self):
        pass

        
    def get_payment_link(self, hash: str) -> dict:
        response = self.make_public_request('get',  '/public/merchant/payment/{hash}')
        
        return response


    def create_payment_link(self, hash: str) -> dict:
        request =  requests.post('/public/merchant/paymentlink/{hash}')
        
        return response