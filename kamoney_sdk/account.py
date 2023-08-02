import requests
from .decorators import Private

class Account():
    def __init__(self):
        pass


    @Private
    def change_account_info(self, name: str, personal_id: str, date_of_birth: str) -> dict:
        body = {
            'name': name,
            'personal_id': personal_id,
            'date_of_birth': date_of_birth
        }
        response = self.make_request('post', '/private/account', body)
        return response


    # /private/account/locality
    @Private
    def change_account_locality(self, zipcode: str, street: str, number: str, complement: str, neighborhood, city: int, state: int) -> dict:
        body = {
            'zipcode': zipcode,
            'street': street,
            'number': number,
            'complement': complement,
            'neighborhood': neighborhood,
            'city': city,
            'state': state
        }
        response = self.make_request('post', '/private/account/locality', body)
        return response


    # endpoint /private/account/contact
    @Private
    def change_account_contact(self, whatsapp: str, telegram: str) -> dict:
        body = {
            'whatsapp': whatsapp,
            'telegram': telegram
        }
        response = self.make_request('post', '/private/account/contact', body)
        return response


    # /private/account/history
    @Private
    def get_account_history(self, page=None, date=None) -> dict:
        request = requests.get(f'{self.base_url}', headers=headers)
        response = request.json()
        if page and date:
            body = {
                'page':page,
                'date':date
            }
            response = self.make_request('get', '/private/account/history', body)
        else:
            response = self.make_request('post', '/private/account/history', {})
        return response
    

    # endpoint /private/account
    @Private
    def get_account_info(self) -> dict:
        response = self.make_request('get', '/private/account', {})
        return response
    
    
    # endpoint /private/account/notification
    @Private
    def get_account_notifications(self, id=None) -> dict:
        if id == None:
            response = self.make_request('get', '/private/account/notification', {})
        else:
            response = self.make_request('get', f'/private/account/notification?id={id}', {})
        return response
    
    # /private/account/locality
    @Private
    def get_account_locality(self) -> dict:
        response = self.make_request('get', '/private/account/locality', {})
        return response    
    
    # /private/account/notification/{id}
    @Private
    def mark_notification_as_read_by_id(self, id: str):
        self.make_request('put', f'/private/account/notification/{id}', {})
        return

    # /private/account/notification
    @Private
    def mark_notifications_as_read(self):
        headers = {}
        requests.put(f'{self.base_url}/private/account/notification', headers=headers)
        self.make_request('put', '/private/account/notification', {})
        return
