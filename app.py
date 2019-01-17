from flask import Flask
app = Flask(__name__)
word = "Hello World"

@app.route('/users',methods=["GET"])
def String_Returner():
    with open('word.txt') as f:
        return f.readline()

@app.route('/users',methods=["POST"])
def Update_Word():
    with open('word.txt', "w+") as f:
        f.write("bet")
    return "200"

