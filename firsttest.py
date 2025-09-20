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
# CLOSE BROWSER
# -------------------------------

driver.quit()
