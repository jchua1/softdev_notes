from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def msg():
    return render_template("main.html")

@app.route("/one/")
def one():
    return render_template("one.html")

@app.route("/two/")
def two():
    return render_template("two.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
