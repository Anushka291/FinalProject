from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

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

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(port=8004, debug=False)