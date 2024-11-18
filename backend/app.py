from flask import Flask, jsonify # type: ignore
from flask_cors import CORS
from routes.submission import submission_blueprint
import requests
from bs4 import BeautifulSoup
from scraping.scraping import fetch_content

app = Flask(__name__)
CORS(app)

app.register_blueprint(submission_blueprint)

@app.route('/')
def home():
    return "Hello, world!"

@app.route('/test')
def test():
    test_string = [
  {
    "choices": [
      "iPhone",
      "Mac",
      "iPad",
      "Apple Watch"
    ],
    "question": "What type of products are you interested in?"
  },
  {
    "choices": [
      "Myself",
      "Someone else"
    ],
    "question": "Are you shopping for yourself or someone else?"
  },
  {
    "choices": [
      "Holiday gifts",
      "Learning about new products",
      "Accessories",
      "Technical support"
    ],
    "question": "What is your main reason for visiting the Apple Store today?"
  },
  {
    "choices": [
      "Credit/Debit card",
      "PayPal",
      "Apple Financing",
      "Other"
    ],
    "question": "How do you prefer to pay for your purchases?"
  },
  {
    "choices": [
      "Personal use",
      "Business",
      "Education",
      "Healthcare"
    ],
    "question": "What is your primary usage for Apple products?"
  },
  {
    "choices": [
      "Very familiar",
      "Somewhat familiar",
      "Not familiar"
    ],
    "question": "How familiar are you with Apple products?"
  },
  {
    "choices": [
      "Yes, definitely",
      "Maybe",
      "No, standard products are fine"
    ],
    "question": "Are you interested in customized products?"
  },
  {
    "choices": [
      "Yes",
      "No"
    ],
    "question": "Do you currently own any Apple devices?"
  },
  {
    "choices": [
      "Every year",
      "Every 2-3 years",
      "I keep my devices until they break",
      "I rarely upgrade"
    ],
    "question": "How often do you upgrade your Apple devices?"
  },
  {
    "choices": [
      "Yes",
      "No"
    ],
    "question": "Would you like information on special financing options?"
  }
]
    return test_string

if __name__ == '__main__':
    app.run(debug=True)
