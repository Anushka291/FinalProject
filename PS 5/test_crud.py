from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import WebDriverException
import time

# Setup Edge options
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.set_capability("ms:loggingPrefs", {"browser": "ALL"})

# Start driver
driver = webdriver.Edge(options=options)

# Open your HTML file
driver.get("D:\\AISSMS IOIT\\Third Year\\6th Semester\\DEVOPS\\DevOps EndSem\\PS 5\\index.html")

print("---------------------------")
print("Test Started")
print("---------------------------")

try:
    while True:
        try:
            # ✅ Check if browser is still open
            if len(driver.window_handles) == 0:
                raise WebDriverException("Browser closed")

            # Get browser logs
            logs = driver.get_log("browser")

            for log in logs:
                message = log["message"]

                if "CREATED" in message:
                    print("TC-1 | Add Student    | PASS")
                elif "UPDATED" in message:
                    print("TC-2 | Edit Student   | PASS")
                elif "DELETED" in message:
                    print("TC-3 | Delete Student | PASS")

            time.sleep(1)

        except WebDriverException:
            # ✅ This will now trigger when browser closes
            print("\n---------------------------")
            print("TC-4 | Browser Close | PASS")
            print("---------------------------")
            break

except KeyboardInterrupt:
    print("\nManual Stop Detected")

finally:
    try:
        driver.quit()
    except:
        pass