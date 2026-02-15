# Section 4: Selenium Browser Control - Reference Examples

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Start browser
browser = webdriver.Firefox()
browser.get('https://autbor.com/example3.html')

# Find element by ID
user_elem = browser.find_element(By.ID, 'login_user')
print(user_elem.tag_name)

# Find elements by tag name
p_elems = browser.find_elements(By.TAG_NAME, 'p')
print(len(p_elems))
print(p_elems[0].text)

# Find element by link text
link_elem = browser.find_element(By.LINK_TEXT, 'This text is a link')
link_elem.click()

# Go back
browser.back()

# Fill out form
user_elem = browser.find_element(By.ID, 'login_user')
user_elem.send_keys('admin')
password_elem = browser.find_element(By.ID, 'login_pass')
password_elem.send_keys('password123')
password_elem.submit()

# Scroll page
html_elem = browser.find_element(By.TAG_NAME, 'html')
html_elem.send_keys(Keys.END)
html_elem.send_keys(Keys.HOME)

# Close browser
browser.quit()
