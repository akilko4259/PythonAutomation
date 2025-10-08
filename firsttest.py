# Import required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import os
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select




# 🔹 Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 🔹 Suppress ChromeDriver logs
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])



# Initialize Chrome WebDriver service (specify path to chromedriver)
service = webdriver.chrome.service.Service(
    executable_path=r"C:\chromedriver-win64\chromedriver.exe"
)



# Launch Chrome browser
driver = webdriver.Chrome(service=service,options=options)
wait = WebDriverWait(driver,10)
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

#driver.get("https://www.facebook.com/")
#driver.set_page_load_timeout(10)
#print("Page Title:", driver.title)
         

#submit = wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']")))

# Enter email using CSS Selector (ID selector)
#driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("tagID")

# Example: Using CSS Selector by class (only first class without spaces)
#  If multiple classes have spaces, only the first class name should be used
#driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("Tagclass")

# Example: Using CSS Selector with attribute
#driver.find_element(
#    By.CSS_SELECTOR, "input[placeholder='Email address or phone number']"
#).send_keys("tagattribute")

# Example: Using CSS Selector with class + attribute
#driver.find_element(By.CSS_SELECTOR, "input.inputtext[name=pass]").send_keys(
#    "tagclassattribute"
#)

# Click on Login button
#submit.click()

# -------------------------------
# EXTRACT ALL LINKS FROM PAGE
# -------------------------------

# Find all <a> elements
links = driver.find_elements(By.TAG_NAME, "a")
print("Total # of links = ", len(links))



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


links = driver.find_elements(By.TAG_NAME,"a")
print("Total # of links = ",len(links))
for link in links:
    print("Valude of ID : ",link.get_attribute("href"))
    print("Link Text = ",link.text)

driver.get("https://demo.nopcommerce.com/")
driver.get("https://google.com/")

driver.back()

driver.forward()

driver.refresh()
   
driver.get("https://testautomationpractice.blogspot.com/")

checkboxes = driver.find_elements(By.XPATH,"//*[@type='checkbox' and contains(@id,'day')]")

for checkbox in checkboxes:
    
    if  checkbox.get_attribute("id") == "sunday" or checkbox.get_attribute("id") == "saturday":
         print("Skipping checkbox : ",checkbox.get_attribute("id"))
    else:
         checkbox.click()
         print("Selected checkbox : ",checkbox.get_attribute("id"))
    time.sleep(2)   

for checkbox in checkboxes:
    if checkbox.is_selected():
        print("Checkbox is selected : ",checkbox.get_attribute("id"))
    else:
        print("Checkbox is NOT selected : ",checkbox.get_attribute("id"))



driver.get("http://www.deadlinkcity.com/")
links = driver.find_elements(By.TAG_NAME,"a")
print("Total links are : ",len(links))
for link in links:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
        if res.status_code >=400:
            print("Link is broken : ",url)
        else:
            print("Link is valid : ",url)
    except Exception as e:
        print("Generated an exception for link : ",url)
        print("Exception is : ",e)
# -------------------------------
# CLOSE BROWSER
# -------------------------------
driver.get("https://testautomationpractice.blogspot.com/")


driver.set_page_load_timeout(10)    
wait.until(EC.element_to_be_clickable((By.XPATH,"//select[@id='country']")))
dropdown = Select(driver.find_element(By.XPATH,"//select[@id='country']"))
dropdown.select_by_visible_text("India")
for option in dropdown.options:
    print("Option is : ",option.text)   
time.sleep(3)   



driver.get("https://the-internet.herokuapp.com/javascript_alerts")

alert = driver.find_element(By.XPATH,"//button[contains(text(),'Click for JS Prompt')]").click()

alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("Test")
alertwindow.accept()
time.sleep(5)
result = driver.find_element(By.XPATH,"//p[@id='result']")
time.sleep(5)
print(result.text)


driver.get("https://akashchaubey.com/Practice3.html")

driver.switch_to.frame("testFrame")
time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Click Me']").click()


driver.quit()
