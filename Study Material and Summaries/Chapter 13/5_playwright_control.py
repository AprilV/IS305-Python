# Section 5: Playwright Browser Control - Reference Examples

from playwright.sync_api import sync_playwright

# Start browser with visible window
playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()

# Navigate to page
page.goto('https://autbor.com/example3.html')
print(page.title())

# Find elements using locators
elems = page.locator('p')
print(elems.count())
print(elems.nth(0).inner_text())

# Find by text
link = page.get_by_text('is a link')
link.click()

# Go back
page.go_back()

# Fill form and submit
page.locator('#login_user').fill('admin')
page.locator('#login_pass').fill('password123')
page.locator('input[type=submit]').click()

# Check/uncheck checkbox
checkbox = page.get_by_role('checkbox')
checkbox.check()
checkbox.uncheck()
checkbox.set_checked(True)

# Scroll page
page.locator('html').press('End')
page.locator('html').press('Home')

# Close browser
browser.close()
playwright.stop()
