from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import XLUtilitis
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/")
driver.maximize_window()

path = "D:\\OneDrive\\Excel\\login-usha.xlsx"
rows = XLUtilitis.getRowCount(path, 'Sheet1')

for r in range(2, rows + 1):
    username = XLUtilitis.readData(path, 'Sheet1', r, 1)
    password = XLUtilitis.readData(path, 'Sheet1', r, 2)

    # Locate elements (correct locators)
    username_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "pass")

    # Clear before sending data
    username_field.clear()
    password_field.clear()

    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click login button
    login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']"))
    )
    login_btn.click()

    # ✅ 👉 IMPLEMENT HERE (after login click)
    try:
        error_msg = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[text()='The login information you entered is incorrect. ']")
            )
        )

        print("Test Failed - Invalid Credentials")
        XLUtilitis.writeData(path, 'Sheet1', r, 3, "Failed")

    except:
        print("Test Passed")
        XLUtilitis.writeData(path, 'Sheet1', r, 3, "Passed")


    # Refresh for next iteration
    driver.get("https://www.instagram.com/")