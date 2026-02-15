# Section 5: Playwright Browser Control - Practice

# Q1: Import sync_playwright from playwright.sync_api
# WHAT IT DOES: Playwright controls browsers with modern features like headless mode
# ┌─ EXAMPLE ─────────────
# │ from playwright.sync_api import sync_playwright
# └───────────────────────




# Q2: Create variable named playwright using sync_playwright().start(), then create browser using playwright.firefox.launch() with headless=False and slow_mo=50, then create page using browser.new_page()
# WHAT IT DOES: start() initializes Playwright; launch() opens browser; new_page() creates tab
# ┌─ EXAMPLE ─────────────
# │ pw = sync_playwright().start()
# │ br = pw.chromium.launch(headless=False, slow_mo=50)
# │ pg = br.new_page()
# └───────────────────────




# Q3: Use page.goto() to navigate to 'https://autbor.com/example3.html', then print page.title()
# WHAT IT DOES: goto() navigates to URL; title() returns page title
# ┌─ EXAMPLE ─────────────
# │ page.goto('https://nostarch.com')
# │ print(page.title())
# └───────────────────────




# Q4: Use page.locator() with 'p' to find paragraphs and store in variable named p_elems, then print p_elems.count()
# WHAT IT DOES: locator() finds elements by CSS selector; count() returns number of matches
# ┌─ EXAMPLE ─────────────
# │ headers = page.locator('h1')
# │ print(headers.count())
# └───────────────────────




# Q5: Use p_elems.nth() with 0 to get first paragraph, then print inner_text() of that element
# WHAT IT DOES: nth() gets element at index; inner_text() returns text content
# ┌─ EXAMPLE ─────────────
# │ first_header = headers.nth(0)
# │ print(first_header.inner_text())
# └───────────────────────




# Q6: Use page.get_by_text() with 'is a link' to find link element, store in variable named link, then call link.click()
# WHAT IT DOES: get_by_text() finds elements containing text; click() simulates mouse click
# ┌─ EXAMPLE ─────────────
# │ button = page.get_by_text('Click here')
# │ button.click()
# └───────────────────────




# Q7: Call page.go_back() to return to previous page
# WHAT IT DOES: go_back() simulates clicking browser's Back button
# ┌─ EXAMPLE ─────────────
# │ page.go_back()
# └───────────────────────




# Q8: Use page.locator() with '#login_user' to find username field, then use fill() to enter 'testuser'
# WHAT IT DOES: fill() clears field and types new text
# ┌─ EXAMPLE ─────────────
# │ page.locator('#email').fill('test@example.com')
# └───────────────────────




# Q9: Use page.locator() with '#login_pass' to find password field, use fill() to enter 'mypassword', then use page.locator() with 'input[type=submit]' to find submit button and click() it
# WHAT IT DOES: Fills password field and clicks submit button (Playwright has no submit() method)
# ┌─ EXAMPLE ─────────────
# │ page.locator('#pwd').fill('secret')
# │ page.locator('button[type=submit]').click()
# └───────────────────────




# Q10: Use page.get_by_role() with 'checkbox' to find checkbox, store in variable named checkbox, then call check(), uncheck(), and set_checked(True) methods
# WHAT IT DOES: check() checks checkbox; uncheck() unchecks it; set_checked() sets specific state
# ┌─ EXAMPLE ─────────────
# │ box = page.get_by_role('checkbox')
# │ box.check()
# │ box.uncheck()
# │ box.set_checked(True)
# └───────────────────────




# Note: Call browser.close() and playwright.stop() when done
