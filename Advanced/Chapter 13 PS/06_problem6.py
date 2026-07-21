from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!\n we are in flask hellow world haha<p>"
app.run()