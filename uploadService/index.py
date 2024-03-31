from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route("/")
def hello_world():
    response = make_response(render_template("index.html"))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0")    

