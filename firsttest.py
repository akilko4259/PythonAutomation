from selenium import webdriver
from selenium.webdriver.common.by import By
import time
service = webdriver.chrome.service.Service(executable_path=r"C:\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title) 
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME, "username").send_keys("Admin")
print("Username Entered")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.implicitly_wait(10)
print("Password Entered")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.implicitly_wait(10)


title = driver.title
expectedTitle = "OrangeHRM"
if title == expectedTitle:
    print("Login Successful - Test Passed")
else:
    print("Login Failed - Test Failed") 
# Quit browser after test
#driver.close()

driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)
print(driver.title)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("tagID")
driver.implicitly_wait(10)
time.sleep(5)
#driver.find_element(By.CSS_SELECTOR,"input.inputtext _55r1 _6luy").send_keys("Tagclass") This will give error because of space in class name
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("Tagclass")
driver.implicitly_wait(10)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Email address or phone number']").send_keys("tagattribute")
time.sleep(5)
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,"input.inputtext[name=pass]").send_keys("tagclassattribute")
time.sleep(5)
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()




links = driver.find_elements(By.TAG_NAME, "a")
print("Total # of links = ",len(links))
for link in links:
    print(link.get_attribute("href"))






    
driver.quit()
print("====================================Test Completed====================================")
