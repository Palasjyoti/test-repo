from flask import Flask

app=Flask(__name__)


@app.route('/') #e,g. google.com
def home():
    return "Hello World- My First Rest API-Palas"

app.run(port=5000)