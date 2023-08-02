class Affiliates:
    def __init__(self):
        pass

    # /private/account/recipients
    def create_account_recipient(self, type: int, account_type: str, bank: int, agency: str, account_number: str, 
                                owner: str, personal_id: str, description: str) -> dict:
        body = {
            'type': type,
            'account_type': account_type,
            'bank': bank,
            'agency': agency,
            'account_number': account_number,
            'owner': owner,
            'personal_id': personal_id,
            'description': description
        }
        response = self.make_request('post', '/private/account/recipients', body)
        return response

    # /private/account/affiliates
    def get_account_affiliate_info(self) -> dict:
        response = self.make_response('get', '/private/account/affiliates', {})
        return response

    # /private/account/recipients
    def get_account_recipients(self) -> dict:
        response = self.make_request('get', '/private/account/recipients', {})
        return response
