from playwright.sync_api import Page

fake_payload_response = {"data": [], "message": "No Orders"}

def intercept_response(route):
    route.fulfill(
        json = fake_payload_response
    )

def test_network_interception(page: Page):
    page.goto("https://rahulshettyacademy.com/client")

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",
               intercept_response)

    page.get_by_placeholder("email@example.com").fill("test@testee.com")
    page.get_by_placeholder("enter your passsword").fill("ABcd@1234")
    page.get_by_role("button", name="Login").click()

    page.locator('button').filter(has_text='Order').click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)