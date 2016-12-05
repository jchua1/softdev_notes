from flask import Flask, render_template

app = Flask(__name__)

l = [0,1,2,3,4,5]

@app.route("/")
def hi():
    return render_template("donow.html", message = "Hi there!", collection = l)

if __name__ == "__main__":
    app.debug = True
    app.run()
