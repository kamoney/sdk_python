import requests

class Affiliates:
    def __init__(self):
        pass

    # /private/account/recipients
    def create_account_recipient(self, type: int, account_type: str, bank: int, agency: str, account_number: str, 
                                owner: str, personal_id: str, description: str) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'{self.authorization}'
        }
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
        request = requests.post(f'{self.base_url}/private/account/recipients', body=body, headers=headers)
        response = request.json()
        return response

    # /private/account/affiliates
    def get_account_affiliate_info(self) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        request = requests.get(f'{self.base_url}/private/account/affiliates', headers=headers)
        response = request.json()
        return response

    # /private/account/recipients
    def get_account_recipients(self) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        request = requests.get(f'{self.base_url}/private/account/recipients', headers=headers)
        response = request.json()