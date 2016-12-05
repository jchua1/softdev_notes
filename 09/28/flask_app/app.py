from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/login/")
def box():
    print request.headers
    return render_template("text.html")

@app.route("/authenticate/", methods = ["POST"])
def auth():
    print request.headers
    print request.form
    print request.form["text"]
    return "AUTHENTICATE"

if __name__ == "__main__":
    app.debug = True
    app.run()
