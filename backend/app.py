from flask import Flask, jsonify
from routes.submission import submission_blueprint
import requests
from bs4 import BeautifulSoup
from scraping.scraping import fetch_content

app = Flask(__name__)

app.register_blueprint(submission_blueprint)

@app.route('/')
def home():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True)