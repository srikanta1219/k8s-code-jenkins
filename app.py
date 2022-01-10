from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HEY THIS IS SRIKANTA TESTING GITOPS PROJECT 2!!!'
