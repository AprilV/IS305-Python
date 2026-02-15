# Section 4: Selenium Browser Control - Practice

# Q1: Import webdriver from selenium, By from selenium.webdriver.common.by, and Keys from selenium.webdriver.common.keys
# WHAT IT DOES: Selenium's webdriver controls the browser; By helps find elements; Keys simulates keyboard
# ┌─ EXAMPLE ─────────────
# │ from selenium import webdriver
# │ from selenium.webdriver.common.by import By
# │ from selenium.webdriver.common.keys import Keys
# └───────────────────────




# Q2: Create variable named browser using webdriver.Firefox(), then use browser.get() to navigate to 'https://autbor.com/example3.html'
# WHAT IT DOES: webdriver.Firefox() launches Firefox browser; get() navigates to a URL
# ┌─ EXAMPLE ─────────────
# │ driver = webdriver.Firefox()
# │ driver.get('https://nostarch.com')
# └───────────────────────




# Q3: Use browser.find_element() with By.ID and 'author' to find element with id="author", store in variable named author_elem
# WHAT IT DOES: find_element() locates single element; By.ID searches for id attribute
# ┌─ EXAMPLE ─────────────
# │ title = browser.find_element(By.ID, 'main')
# └───────────────────────




# Q4: Print author_elem.tag_name and author_elem.text
# WHAT IT DOES: tag_name shows the HTML tag (like 'span'); text shows the content between tags
# ┌─ EXAMPLE ─────────────
# │ print(title.tag_name)
# │ print(title.text)
# └───────────────────────




# Q5: Use browser.find_elements() with By.TAG_NAME and 'p' to find all paragraph elements, store in variable named paragraphs, then print len() of paragraphs
# WHAT IT DOES: find_elements() returns list of all matching elements; By.TAG_NAME searches by HTML tag
# ┌─ EXAMPLE ─────────────
# │ headers = browser.find_elements(By.TAG_NAME, 'h1')
# │ print(len(headers))
# └───────────────────────




# Q6: Use browser.find_element() with By.LINK_TEXT and 'This text is a link' to find the link, store in variable named link, then call link.click()
# WHAT IT DOES: By.LINK_TEXT finds links by exact text; click() simulates clicking the element
# ┌─ EXAMPLE ─────────────
# │ button = browser.find_element(By.LINK_TEXT, 'Click here')
# │ button.click()
# └───────────────────────




# Q7: Call browser.back() to go back to previous page
# WHAT IT DOES: back() simulates clicking browser's Back button
# ┌─ EXAMPLE ─────────────
# │ browser.back()
# └───────────────────────




# Q8: Use browser.find_element() with By.ID to find 'login_user' element, store in variable named username, then use send_keys() to type 'testuser'
# WHAT IT DOES: send_keys() simulates typing into text fields
# ┌─ EXAMPLE ─────────────
# │ email = browser.find_element(By.ID, 'email_field')
# │ email.send_keys('test@example.com')
# └───────────────────────




# Q9: Use browser.find_element() with By.ID to find 'login_pass' element, store in variable named password, use send_keys() to type 'mypassword', then call password.submit()
# WHAT IT DOES: submit() submits the form containing the element
# ┌─ EXAMPLE ─────────────
# │ pwd = browser.find_element(By.ID, 'password_field')
# │ pwd.send_keys('secretpass')
# │ pwd.submit()
# └───────────────────────




# Q10: Use browser.find_element() with By.TAG_NAME and 'html' to get the html element, store in variable named html, then use send_keys() with Keys.END and Keys.HOME to scroll
# WHAT IT DOES: Sending Keys.END scrolls to bottom; Keys.HOME scrolls to top
# ┌─ EXAMPLE ─────────────
# │ page = browser.find_element(By.TAG_NAME, 'html')
# │ page.send_keys(Keys.END)
# │ page.send_keys(Keys.HOME)
# └───────────────────────




# Note: Call browser.quit() when done to close the browser
