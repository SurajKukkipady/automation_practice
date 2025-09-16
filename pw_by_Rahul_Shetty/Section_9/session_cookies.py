from playwright.sync_api import Page, Playwright
from pw_by_Rahul_Shetty.Section_8.utils.apiBase import APIUtils


def test_session_cookies(playwright: Playwright):
    api_utils = APIUtils()
    token_value = api_utils.get_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Set the session cookie
    page.add_init_script(f"""localStorage.setItem('token','{token_value}')""")

    page.goto("https://rahulshettyacademy.com/client")

