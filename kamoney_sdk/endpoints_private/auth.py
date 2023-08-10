import requests
from ..utils.decorators import Private
class Auth:
    def __init__(self): pass

    # endpoint /private/auth/validate
    @Private
    def validate_token(self) -> dict:
        self._check_token()
        headers = {
            'Authorization': f'Bearer {self.authorization}'
        }
        request = requests.get(f'{self.base_url}/private/auth/validate', headers=headers)
        response = request.json()
        return response
