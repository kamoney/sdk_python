from .decorators import Private

class Recipients:
    def __init__(self):
        pass

    # /private/account/recipients
    @Private
    def list_account_recipients(self) -> dict:
        response = self.make_request('get', '/private/account/recipients', {})
        return response
    

    # /private/account/recipients
    @Private
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
    

    @Private
    def delete_account_recipient(self, id: str) -> dict:
        response = self.make_request('delete', f'/private/account/recipients/{id}', {})
        return response


    @Private
    def change_account_recipient(self, id: str, account_type: str, bank: str, agency: str, account_number: str,
                                  owner: str, personal_id: str, description: str) -> dict:
        body = {
            'account_type': account_type,
            'bank': bank,
            'agency': agency,
            'account_number': account_number,
            'owner': owner,
            'personal_id': personal_id,
            'description': description
        }
        response = self.make_request('post', f'/private/account/recipients/{id}')
        return response

    @Private
    def get_account_recipient(self, id: str) -> dict:
        response = self.make_request('get', f'/private/account/recipients/{id}', {})
        return response
