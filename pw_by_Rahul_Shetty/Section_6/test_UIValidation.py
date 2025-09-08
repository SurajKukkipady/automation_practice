from playwright.sync_api import Page, expect


#add 2 items in cart and validate if the items are added with the same name
def test_UIValidationDyanmicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label('Username:').fill('rahulshettyacademy')
    page.get_by_label('Password:').fill('learning')
    page.get_by_role('combobox').select_option('teach')
    page.get_by_role("checkbox", name="terms").click()
    page.get_by_role('button', name='Sign In').click()

    iphone = page.locator("app-card").filter(has_text="iphone X")
    iphone.get_by_role('button').click()

    samsung = page.locator("app-card").filter(has_text="Samsung Note 8")
    samsung.get_by_role('button').click()

    page.get_by_text('Checkout').click()

    expect(page.locator('.media-body')).to_have_count(2)


