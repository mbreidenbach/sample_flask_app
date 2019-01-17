from flask import Flask
app = Flask(__name__)

@app.route('/Search')
def String_Returner():
    return "Hello World!"

