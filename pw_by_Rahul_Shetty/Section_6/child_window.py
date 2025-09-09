from playwright.sync_api import Page, expect

def test_child_window(page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")

    with page.expect_popup() as new_page_info:
        page.locator(".blinkingText").first.click()
        new_page = new_page_info.value
        text = new_page.locator('.red').text_content()
        print(text)



