from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# store data in memory (temporary)
data_store = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]

        data_store.append([title, desc])

        return redirect("/")

    return render_template("index.html", data=data_store)


@app.route("/delete/<int:id>")
def delete(id):
    if id < len(data_store):
        data_store.pop(id)

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)