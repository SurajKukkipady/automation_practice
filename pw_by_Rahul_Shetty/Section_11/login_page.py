#from playwright.sync_api import Page
# from pw_by_Rahul_Shetty.Section_11.dashboard_page import Dashboard_Page
from dashboard_page import Dashboard_Page



class Login_Page:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self , user_email, user_password):
        self.page.get_by_placeholder("email@example.com").fill(user_email)
        self.page.get_by_placeholder("enter your passsword").fill(user_password)
        self.page.get_by_role("button", name="Login").click()

        dashboard_page = Dashboard_Page(self.page)
        return dashboard_page