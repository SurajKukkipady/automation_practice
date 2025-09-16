from playwright.sync_api import Page, expect, Playwright
import json
from apiBase import APIUtils


def test_e2e_web_api(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #read json file
    with open('credentials.json') as f:
        test_data = json.load(f)
        print(test_data)

    #create order via API
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright)

    #login flow
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("test@testee.com")
    page.get_by_placeholder("enter your passsword").fill("ABcd@1234")
    page.get_by_role("button", name="Login").click()

    page.locator('button').filter(has_text='Order').click()
    page.locator('tr').filter(has_text=order_id).get_by_role('button', name='View').click()

    expect(page.locator('.tagline')).to_have_text('Thank you for Shopping With Us')



