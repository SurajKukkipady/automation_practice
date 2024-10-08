'''Scenario
Record the following steps. Press the button below and wait for data to appear (15 seconds), click on text of the loaded label.
Then execute your test to make sure it waits for label text to appear.'''

import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://www.uitestingplayground.com/clientdelay")
    #click on the button
    page.get_by_role("button", name="Button Triggering Client Side").click()
    #wait for the element
    page.wait_for_selector("text=Data calculated on the client", state="visible")
    time.sleep(2)
    #vaidate
    expect(page.get_by_text("Data calculated on the client")).to_be_visible()

    context.close()
    browser.close()

