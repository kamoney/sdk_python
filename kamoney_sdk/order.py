from .decorators import Private

class Order:

    def __init__(self):
        self.object_types = {
            "payment_slips": ["barcode", "institution", "amount", "due_date", "personal_id"],
            "direct_transfers": ["account_type", "bank_id", "agency", "account_number", "personal_id", "owner", "amount"],
            "digital_products": ["product_id", "quantity"],
            "pix": ["type", "key", "amount"]
        }


    @Private
    def create_order(self, objects: list, asset: str, network=None, coupon=None) -> dict:
        if isinstance(object, dict) == False:
            raise Exception("Type object incorrect!")
        body = {
            'asset': asset,
            'network': network,
            'coupon': coupon,
        }
        body = self.check_required_params(body)
        objects_list = {
            'payment_slips': [],
            'direct_transfers': [],
            'digital_products': [],
            'pix': []
        }
        for object in objects:
            if isinstance(object, dict) == False:
                raise Exception("Object types on \"objects\" in create_order should be an dict!")
            object_decomposed = [key for key in object.keys()]
            for object_type, keys in self.object_types:
                if object_decomposed == keys:
                    objects_list[object_type].append(object)
        body.update(objects_list)
        response = self.make_request('post', f'/private/order', body)
        return response
    

    @Private
    def list_order(self, page=None, begin=None, end=None, search=None, status=None) -> dict:
        body = {
            'page': page,
            'begin': begin,
            'end': end,
            'search': search,
            'status': status
        }
        body = self.check_required_params(body)
        response = self.make_request('get', f'/private/order', body)
        return response
    

    @Private
    def get_order_info(self, id: int) -> dict:
        response = self.make_request('get', f'/private/order/{id}', {})
        return response
    

    @Private
    def list_receipt(self, page=None, begin=None, end=None, search=None) -> dict:
        body = {
            'page': page,
            'begin': begin,
            'end': end,
            'search': search
        }
        body = self.check_required_params(body)
        response = self.make_request('get', f'/private/order/receipt', body)
        return response
    

    @Private
    def download_receipt_list(self, filename: str) -> dict:
        response = self.make_request('get', f'/private/order/receipt/{filename}', {})
        return response
    


        
        
        
