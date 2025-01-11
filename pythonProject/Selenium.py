import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:

    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

checkbutton = driver.find_elements(By.XPATH, "//input[@value='radio3']")
print(len(checkbutton))

for cb in checkbutton:

    if cb.get_attribute("value") == "radio3":
        cb.click()
        assert cb.is_selected()
        break

#another method for checking radio button:
# Radiobutton = driver.find_elements(By.CSS_Selector, .radiobutton)
#Radiobutton[2].click()
#assert Radiobutton[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()


#browser alert
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Rush")

driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert

alertText = alert.text

print(alertText)

assert "Rush" in alertText

alert.accept()

# alert.dismissQ

time.sleep(10)


