class Utils:
    def get_bank(self) -> dict:
        response = self.make_public_request('get',  '/public/bank')
        
        return response


    def get_info(self) -> dict:
        response = self.make_public_request('get',  '/public/system/info')
        
        return response


    def get_notification(self) -> dict:
        response = self.make_public_request('get',  '/public/notification')
        
        return response


    def get_country(self) -> dict:
        response = self.make_public_request('get',  '/public/country')
        
        return response


    def get_state(self, country_id: int) -> dict:
        response = self.make_public_request('get',  '/public/country/{country_id}/state')
        
        return response


    def get_city(self, country_id: int, state_id: int) -> dict:
        response = self.make_public_request('get',  '/public/country/{country_id}/state/{state_id}/city')
        
        return response


    def get_currency(self) -> dict:
        response = self.make_public_request('get',  '/public/currency')
        
        return response


    def get_network(self, asset: str) -> dict:
        response = self.make_public_request('get',  '/public/{asset}')
        
        return response


    def get_faq(self) -> dict:
        response = self.make_public_request('get',  '/public/faq')
        
        return response


    def get_product(self) -> dict:
        response = self.make_public_request('get',  '/public/product')
        
        return response


    def get_contact(self, name: str, email: str, subject: str, message: str) -> dict:
        body = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        response = self.make_public_request('post', '/public/contact', body)
        
        return response


    def get_pix_types(self) -> dict:
        response = self.make_public_request('get',  '/public/pixtype', {})
        return response


    def get_affiliate(self) -> dict:
        response = self.make_public_request('get',  '/public/affiliate')
        
        return response


    def get_status(self) -> dict:
        response = self.make_public_request('get',  '/public/status')
        
        return response


    def get_coupon(self, coupon: str) -> dict:
        response = self.make_public_request('get',  '/public/coupon/{coupon}')
        
        return response


    def get_fee(self) -> dict:
        response = self.make_public_request('get',  '/public/fee')
        
        return response


    def get_buy_wallet_types(self) -> dict:
        response = self.make_public_request('get',  '/public/buy/wallet/type')
        
        return response


    def get_buy_payment_category(self) -> dict:
        response = self.make_public_request('get',  '/public/buy/payment/category')
        
        return response


    def get_buy_payment_category_types(self, code: str) -> dict:
        response = self.make_public_request('get',  '/public/buy/payment/category/{code}')
        
        return response


    def get_reward(self) -> dict:
        response = self.make_public_request('get',  '/public/reward')
        
        return response