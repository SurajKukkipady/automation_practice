from playwright.sync_api import Page, expect, Playwright

def test_e2e_web_api(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("Email").fill("test@testee.com")
    page.get_by_placeholder("Password").fill("ABcd@1234")
    page.get_by_role("button", name="Login").click()