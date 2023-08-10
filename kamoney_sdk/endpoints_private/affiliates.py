class Affiliates:
    def __init__(self):
        pass

    # /private/account/affiliates
    def get_account_affiliate_info(self) -> dict:
        response = self.make_response('get', '/private/account/affiliates', {})
        return response


