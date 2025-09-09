from playwright.sync_api import Page, expect

def testUIchecks(page):
    #hide/display placeholder
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for i in range(page.locator('th').count()):
        if page.locator('th').nth(i).filter(has_text="Price").count() > 0:
            colValue = i

