from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("http://localhost:8004")
time.sleep(3)

def slow_type(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(0.1)

def fill_form(email, password):
    slow_type(driver.find_element(By.NAME, "name"), "Anu")
    slow_type(driver.find_element(By.NAME, "email"), email)
    slow_type(driver.find_element(By.NAME, "event"), "Tech Fest")
    slow_type(driver.find_element(By.NAME, "password"), password)
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(3)

# TC1: Valid Registration
fill_form("anu@gmail.com", "admin@123")
print("✅ TC1 PASS" if "Registration Successful" in driver.page_source else "❌ TC1 FAIL")

# TC2: Wrong Email
driver.get("http://localhost:8004")
fill_form("wrong@gmail.com", "admin@123")
print("✅ TC2 PASS" if "Cannot register" in driver.page_source else "❌ TC2 FAIL")

# TC3: Short Password
driver.get("http://localhost:8004")
fill_form("anu@gmail.com", "anu@123")
print("✅ TC3 PASS" if "Invalid password!" in driver.page_source else "❌ TC3 FAIL")

driver.quit()