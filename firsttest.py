# Import required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver service (specify path to chromedriver)
service = webdriver.chrome.service.Service(
    executable_path=r"C:\chromedriver-win64\chromedriver.exe"
)

# Launch Chrome browser
driver = webdriver.Chrome(service=service)

# Open OrangeHRM demo website
driver.get("https://opensource-demo.orangehrmlive.com/")

# Print page title
print(driver.title)

# Maximize browser window
driver.maximize_window()

# Set implicit wait (applies to all elements globally)
driver.implicitly_wait(10)

# -------------------------------
# LOGIN TO ORANGEHRM
# -------------------------------

# Enter Username
driver.find_element(By.NAME, "username").send_keys("Admin")
print("Username Entered")

# Enter Password
driver.find_element(By.NAME, "password").send_keys("admin123")
print("Password Entered")

# Click on Login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Verify page title after login
title = driver.title
expectedTitle = "OrangeHRM"
if title == expectedTitle:
    print("Login Successful - Test Passed")
else:
    print("Login Failed - Test Failed")

# -------------------------------
# OPEN FACEBOOK LOGIN PAGE
# -------------------------------

driver.get("https://www.facebook.com/")
print(driver.title)

# Enter email using CSS Selector (ID selector)
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("tagID")

# Example: Using CSS Selector by class (only first class without spaces)
# ⚠️ If multiple classes have spaces, only the first class name should be used
driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("Tagclass")

# Example: Using CSS Selector with attribute
driver.find_element(
    By.CSS_SELECTOR, "input[placeholder='Email address or phone number']"
).send_keys("tagattribute")

# Example: Using CSS Selector with class + attribute
driver.find_element(By.CSS_SELECTOR, "input.inputtext[name=pass]").send_keys(
    "tagclassattribute"
)

# Click on Login button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# -------------------------------
# EXTRACT ALL LINKS FROM PAGE
# -------------------------------

# Find all <a> elements
links = driver.find_elements(By.TAG_NAME, "a")
print("Total # of links = ", len(links))

# Print all link URLs
for link in links:
    print(link.get_attribute("href"))

# -------------------------------
# FETCH PAGE DETAILS
# -------------------------------

# Print current page URL
print("Current URL:", driver.current_url)

# Print current page title
print("Page Title:", driver.title)

# Print current page source (HTML of the page)
print("Page Source length:", len(driver.page_source))  # safer than printing whole HTML

# Print window handle (unique identifier of the browser window)
print("Current Window Handle:", driver.current_window_handle)

# Maximize browser window
driver.maximize_window()

# -------------------------------
# NAVIGATE TO DEMO SITE
# -------------------------------

driver.get("https://demo.nopcommerce.com/")

# Click on "Register" link using Link Text
driver.find_element(By.LINK_TEXT, "Register").click()

# -------------------------------
# RADIO BUTTON OPERATIONS
# -------------------------------

# Locate Male and Female radio buttons
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

# Check initial state of Male radio button
print("Male Radio Button is displayed:", rd_male.is_displayed())   # Is it visible on page?
print("Male Radio Button is enabled:", rd_male.is_enabled())       # Is it clickable?
print("Male Radio Button is selected:", rd_male.is_selected())     # Is it already selected?

# Click on Male radio button
rd_male.click()

# Check state again after clicking
print("After clicking Male radio button:")
print("Male Radio Button is displayed:", rd_male.is_displayed())
print("Male Radio Button is enabled:", rd_male.is_enabled())
print("Male Radio Button is selected:", rd_male.is_selected())








driver.find_element(By.LINK_TEXT,"nopCommerce").click()
time.sleep(5)


time.sleep(5)


links = driver.find_elements(By.TAG_NAME,"a")
print("Total # of links = ",len(links))
for link in links:
    print("Valude of ID : ",link.get_attribute("href"))
    print("Link Text = ",link.text)
# -------------------------------
# CLOSE BROWSER
# -------------------------------

driver.quit()