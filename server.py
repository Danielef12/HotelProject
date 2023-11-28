from flask import Flask, render_template, request
from mongoengine import connect

conn = connect(host="mongodb://127.0.0.1:27017/Hotel")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/services.html")
def services():
    return render_template("services.html")


@app.route("/hotel.html")
def hotel():
    return render_template("hotel.html")


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route("/index.html/#")
def checkin():
    return render_template("")

if __name__ == "__main__":
    app.run(debug=True)
