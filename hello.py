from flask import Flask

app = Flask(__name__)

@app.route ('/')
def hello_wolrd():
 return 'Hello World'
p3 v