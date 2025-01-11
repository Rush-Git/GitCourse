from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from self import self

driver = webdriver.Chrome

driver.get("https://www.flipkart.com/")

driver.find_element(By.XPATH, "//div[@type='text']".send_keys("rushaidha"))

driver.close()


