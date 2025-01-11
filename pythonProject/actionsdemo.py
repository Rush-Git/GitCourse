from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
# action.doubleclick(driver.findElement(By
# action.context click()
# action.drag and droR()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

# action.context.click(driver.findElement(By.LINK TEXT "TOR".perform())
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
