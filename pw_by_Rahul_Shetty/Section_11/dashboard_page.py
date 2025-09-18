from playwright.sync_api import Page

class Dashboard_Page:

    def __init__(self, page):
        self.page = page

    def selectOrderNavLink(self, order_id):
        self.page.locator('button').filter(has_text='Order').click()
        self.page.locator('tr').filter(has_text=order_id).get_by_role('button', name='View').click()

