import time

from playwright.sync_api import Page, Route, Request

def intercept_request(route):
    route.continue_(url='https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=12345')


def test_network_interception(page: Page):
    page.goto("https://rahulshettyacademy.com/client")

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",
               intercept_request)

    page.get_by_placeholder("email@example.com").fill("test@testee.com")
    page.get_by_placeholder("enter your passsword").fill("ABcd@1234")
    page.get_by_role("button", name="Login").click()

    page.locator('button').filter(has_text='Order').click()
    page.get_by_role('button', name='View').first.click()
    time.sleep(5)
    msg = page.locator(".blink_me").text_content()
    print(msg)