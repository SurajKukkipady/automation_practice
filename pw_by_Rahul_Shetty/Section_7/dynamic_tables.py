from playwright.sync_api import Page, expect

def testUIchecks(page):
    #hide/display placeholder
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for i in range(page.locator('th').count()):
        if page.locator('th').nth(i).filter(has_text="Price").count() > 0:
            price_colValue = i
            break

    rice_row = page.locator('tr').filter(has_text="Rice")
    expect(rice_row.locator('td').nth(price_colValue)).to_have_text("37")

