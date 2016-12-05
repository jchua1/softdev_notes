from flask import Flask

app = Flask(__name__) #app is just a variable name

@app.route("/") #function decorator: responds with message() when root is accessed
@app.route("/map") #can have 2 routes to the same function
def message():
    return __name__ + " Hi." #return instead of print

if __name__ == "__main__":
    app.run()
