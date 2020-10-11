from flask import Flask
from time import sleep
app = Flask(__name__)

@app.route('/')
def index():
    sleep(10)
    print("hi")
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=8000)