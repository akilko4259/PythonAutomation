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
options.add_argument("--disable-notifications")
options.add_experimental_option("excludeSwitches", ["enable-logging"])



# Initialize Chrome WebDriver service (specify path to chromedriver)
service = webdriver.chrome.service.Service(
    executable_path=r"C:\chromedriver-win64\chromedriver.exe"
)



# Launch Chrome browser
driver = webdriver.Chrome(service=service,options=options)
wait = WebDriverWait(driver,10)


driver.get("https://akashchaubey.com/Practice3.html")


rows = driver.find_elements(By.XPATH,"//table[@id='dataTable']/tbody/tr")
cells = driver.find_elements(By.XPATH,"//table[@id='dataTable']/tbody/tr/td")
columns = int(len(cells)/len(rows))
print("No of rows are: ",len(rows))
print("No of columns are: ",columns)

for i in range(1,len(rows)+1):
    for j in range(1,columns+1):
        print(driver.find_element(By.XPATH,"//table[@id='dataTable']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text,end=" | ")
    print()









driver.switch_to.frame("testFrame")

driver.find_element(By.XPATH,"//button[text()='Click Me']").click()

alert = driver.switch_to.alert

alert.text

txt = alert.text

alert.accept()

driver.switch_to.default_content()

driver.find_element(By.ID,"username").send_keys(txt)

#by Index
driver.switch_to.frame(0)



driver.find_element(By.XPATH,"//button[text()='Click Me']").click()

alert = driver.switch_to.alert

alert.text

txt = alert.text

alert.accept()

driver.switch_to.default_content()

intput = driver.find_element(By.ID,"username")
intput.send_keys("Second time "+txt)

print(intput.get_attribute("value"))

driver.find_element(By.LINK_TEXT,"External Link (Selenium)").click()    
time.sleep(5)   
windows = driver.window_handles
parent = windows[0]
child = windows[1]
time.sleep(5)     
driver.switch_to.window(child)
time.sleep(5)   
print(driver.title) 
driver.switch_to.window(parent)
time.sleep(5)   
print(driver.title)     


driver.get("https://www.gps-coordinates.net/my-location#google_vignette")

time.sleep(5)




driver.quit()
