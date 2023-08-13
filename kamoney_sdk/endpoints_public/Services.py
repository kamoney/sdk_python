class Services:

    def __init__(self):
        pass


    def get_status_order(self) -> dict:
        response = self.make_request('get', f'/public/services/order')
        return response


    def get_status_merchant(self) -> dict:
        response = self.make_request('get', f'/public/services/merchant')
        return response


    def get_status_buy(self) -> dict:
        response = self.make_request('get', f'/public/services/buy')
        return response
