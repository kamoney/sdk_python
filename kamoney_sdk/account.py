import requests
from .decorators import Private

class Account:
    def __init__(self):
        pass

    @Private
    def change_account_info(self, name: str, personal_id: str, date_of_birth: str) -> dict:
        body = {
            'name': name,
            'personal_id': personal_id,
            'date_of_birth': date_of_birth
        }
        sign = super().sign_request(body, self.keys['secret_key'])
        headers = {
            'public': self.keys['public_key'],
            'sign': sign,
            'Content-Type': 'application/json'
        }
        request = requests.post(f'{self.base_url}/private/account', headers=headers)
        response = request.json()
        return response

    # /private/account/locality
    @Private
    def change_account_locality(self, zipcode: str, street: str, number: str, complement: str, neighborhood, city: int, state: int) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        body = {
            'zipcode': zipcode,
            'street': street,
            'number': number,
            'complement': complement,
            'neighborhood': neighborhood,
            'city': city,
            'state': state
        }
        request = requests.post(f'{self.base_url}/private/account/locality', json=body, headers=headers)
        response = request.json()
        return response

    # endpoint /private/account/contact
    @Private
    def change_account_contact(self, whatsapp: str, telegram: str) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        body = {
            'whatsapp': whatsapp,
            'telegram': telegram
        }
        request = requests.post(f'{self.base_url}/private/account/contact', headers=headers, data=body)
        response = request.json()
        return response

    # /private/account/history
    @Private
    def get_account_history(self) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        request = requests.get(f'{self.base_url}', headers=headers)
        response = request.json()
        return response
    
    # endpoint /private/account
    @Private
    def get_account_info(self) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        request = requests.get(f'{self.base_url}/private/account', headers=headers)
        response = request.json()
        return response
    
    # endpoint /private/account/notification
    @Private
    def get_account_notifications(self, id=None) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        if id == None:
            request = requests.get(f'{self.base_url}/private/account/notification')
        else:
            request = requests.get(f'{self.base_url}/private/account/notification?id={id}')
        response = request.json()
        return response
    
    # /private/account/locality
    @Private
    def get_account_locality(self) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        request = requests.post(f'{self.base_url}/private/account/locality', headers=headers)
        response = request.json()
        return response    
    
    # /private/account/notification/{id}
    @Private
    def mark_notification_as_read_by_id(self, id: str):
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        requests.put(f'{self.base_url}/private/account/notification/{id}', headers=headers)
        return

    # /private/account/notification
    @Private
    def mark_notifications_as_read(self):
        headers = {}
        requests.put(f'{self.base_url}/private/account/notification', headers=headers)
        return
