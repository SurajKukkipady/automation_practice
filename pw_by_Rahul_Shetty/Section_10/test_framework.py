from playwright.sync_api import Page, expect, Playwright
import json
from apiBase import APIUtils
import pytest
from login_page import Login_Page

with open('credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_list = test_data['user_credentials']

@pytest.mark.parametrize("user", user_list)
def test_e2e_web_api(playwright : Playwright, user):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    user_name = user['user_email']
    password = user['password']


    #create order via API
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user)

    #object for login page
    login_page = Login_Page(page)
    login_page.navigate()

    login_page.login()

    page.get_by_placeholder("email@example.com").fill(user['user_email'])
    page.get_by_placeholder("enter your passsword").fill(user['password'])
    page.get_by_role("button", name="Login").click()

    page.locator('button').filter(has_text='Order').click()
    page.locator('tr').filter(has_text=order_id).get_by_role('button', name='View').click()

    expect(page.locator('.tagline')).to_have_text('Thank you for Shopping With Us')



