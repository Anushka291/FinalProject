from flask import Flask, request, render_template
from selenium import webdriver
import threading
import time

app = Flask(__name__)

driver = None


# -------- START BROWSER AFTER SERVER STARTS --------
def start_browser():
    global driver
    time.sleep(2)  # wait for Flask to start

    driver = webdriver.Edge()
    driver.get("http://localhost:8082")


# -------- SELENIUM CHECK --------
def run_selenium_check():
    global driver
    time.sleep(1)

    result = driver.page_source

    if "Registration Successful" in result:
        print("✅ PASS: Registration Successful")

    elif "Password" in result:
        print("❌ FAIL: Password Issue")

    elif "Cannot register" in result:
        print("❌ FAIL: Email Issue")

    else:
        print("❌ FAIL: Unknown Issue")


# -------- ROUTE --------
@app.route("/", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        event = request.form["event"]
        password = request.form["password"]

        # -------- VALIDATION --------
        if len(password) < 6:
            message = "Password must be at least 6 characters!"

        elif not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
            message = "Password must contain letters and numbers!"

        elif email != "anu@gmail.com":
            message = "Cannot register - Wrong Email!"

        elif password != "admin@123":
            message = "Invalid password!"

        else:
            message = "Registration Successful"

        # run selenium check
        threading.Thread(target=run_selenium_check).start()

    return render_template("index.html", message=message)


# -------- MAIN --------
if __name__ == "__main__":
    threading.Thread(target=start_browser).start()
    app.run(port=8082, debug=False)