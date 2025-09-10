from playwright.sync_api import Playwright

orders_payload = '{"orders":[{"country":"Afghanistan","productOrderedId":"68a961459320a140fe1ca57a"}]}'
# token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OGMwMDNhY2Y2NjlkNmNiMGFiZTY4MjgiLCJ1c2VyRW1haWwiOiJ0ZXN0QHRlc3RlZS5jb20iLCJ1c2VyTW9iaWxlIjo4NjYwMTUzNDg4LCJ1c2VyUm9sZSI6ImN1c3RvbWVyIiwiaWF0IjoxNzU3NTEwMzA0LCJleHAiOjE3ODkwNjc5MDR9.Oegp76gm-mzmR8GSesv5LgonNzYxTsbcRM2vhMP7A0c'
class APIUtils:

    def get_token(self, playwright : Playwright):
        api_req_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response = api_req_context.post('/api/ecom/auth/login',
                                        data = {"userEmail":"test@testee.com",
                                        "userPassword":"ABcd@1234"})
        assert response.ok
        response_body = response.json()
        return response_body['token']

    def create_order(self, playwright : Playwright):
        token = self.get_token(playwright)
        api_req_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response = api_req_context.post('/api/ecom/order/create-order',
                             data=orders_payload, headers={"Authorization": token,
                             "Content-Type": "application/json"})

        response.json()