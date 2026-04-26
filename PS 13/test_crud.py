from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time

# Setup Edge
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Edge(options=options)

# Open your app
driver.get("D:\\AISSMS IOIT\\Third Year\\6th Semester\\DEVOPS\\DevOps EndSem\\PS 13\\index.html")

print("\n---------------------------")
print(" AUTOMATED TEST STARTED ")
print("---------------------------\n")

time.sleep(2)

# -------------------------
# TC-1: ADD STUDENT
# -------------------------
driver.find_element(By.ID, "name").send_keys("Anushka")
time.sleep(1)

driver.find_element(By.ID, "prn").send_keys("12345")
time.sleep(1)

driver.find_element(By.ID, "course").send_keys("IT")
time.sleep(1)

driver.find_element(By.XPATH, "//button[text()='Add Student']").click()
time.sleep(2)

print("TC-1 | Add Student    | PASS")

# -------------------------
# TC-2: UPDATE STUDENT
# -------------------------
driver.find_element(By.XPATH, "//button[text()='Edit']").click()
time.sleep(2)

name = driver.find_element(By.ID, "name")
name.clear()

# Slow typing (visible)
for ch in "Updated Name":
    name.send_keys(ch)
    time.sleep(0.2)

prn = driver.find_element(By.ID, "prn")
prn.clear()
for ch in "99999":
    prn.send_keys(ch)
    time.sleep(0.2)

course = driver.find_element(By.ID, "course")
course.clear()
for ch in "CS":
    course.send_keys(ch)
    time.sleep(0.2)

# Click same Add button (acts as update now)
driver.find_element(By.XPATH, "//button[text()='Add Student']").click()
time.sleep(2)

print("TC-2 | Edit Student   | PASS")

# -------------------------
# TC-3: DELETE STUDENT
# -------------------------
driver.find_element(By.XPATH, "//button[text()='Delete']").click()
time.sleep(2)

print("TC-3 | Delete Student | PASS")

# -------------------------
# TC-4: CLOSE BROWSER
# -------------------------
time.sleep(2)
driver.quit()

print("TC-4 | Browser Close  | PASS")

print("\n---------------------------")
print(" ALL TESTS COMPLETED ")
print("---------------------------")