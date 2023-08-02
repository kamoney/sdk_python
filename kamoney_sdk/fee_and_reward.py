from .decorators import Private 

class Fee_And_Reward:

    def __init__(self):
        pass


    @Private
    def get_account_fee(self) -> dict:
        response = self.make_request('get', '/private/account/fee', {})
        return response
    

    @Private
    def get_account_reward(self) -> dict:
        response = self.make_request('get', '/private/account/reward', {})
        return response
    