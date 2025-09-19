from playwright.sync_api import Page, expect, Playwright
import json
from apiBase import APIUtils
import pytest
from login_page import Login_Page
from dashboard_page import Dashboard_Page

with open('credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_list = test_data['user_credentials']

@pytest.mark.parametrize("user", user_list)
def test_e2e_web_api(playwright : Playwright, user, browser_instance):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()

    user_name = user['user_email']
    password = user['password']

    #create order via API
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user)

    #object for login page
    login_page = Login_Page(browser_instance)
    login_page.navigate()

    dashboard_page = login_page.login(user_name, password)

    #dashboard_page = Dashboard_Page(page)
    dashboard_page.selectOrderNavLink(order_id)

    expect(browser_instance.locator('.tagline')).to_have_text('Thank you for Shopping With Us')



