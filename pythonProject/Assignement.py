from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])

#print(driver.find_element(By.XPATH, "//div[@class='im-para red']").text)
#result = driver.find_elements(By.CSS_SELECTOR,"im-para red").text

message = driver.find_element(By.CSS_SELECTOR, ".red").text

var = message.split()

print(var[4])

driver.close()

driver.switch_to.window(windowsOpened[0])

driver.find_element(By.ID, "username").send_keys(var[4])
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.ID, "signInBtn").click()
wait = WebDriverWait(driver, 10)

wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)



#print(driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text)