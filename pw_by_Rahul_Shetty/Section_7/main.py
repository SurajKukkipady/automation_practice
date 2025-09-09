from playwright.sync_api import Page, expect

def testUIchecks(page):
    #hide/display placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_visible()

    #Alert handling
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role('button', name="Confirm").click()

    #Frame handling
    frame = page.frame_locator('#courses-iframe')
    frame.get_by_role("link", name="All Access Plan").click()
    expect(frame.locator('body')).to_contain_text("Happy Subscibers")

    #Mouse hover
    page.locator('#mousehover').hover()
    page.get_by_role("link", name="Top").click()