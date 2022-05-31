from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is a simple Flask app'

@app.errorhandler(404)
def not_found(_):
    return 'not found', 404
