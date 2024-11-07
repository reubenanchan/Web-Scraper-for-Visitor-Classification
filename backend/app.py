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

@app.route('/scrape')
def scrape():
    url = 'https://www.apple.com/ca/store?afid=p238%7CshFROjR3i-dc_mtid_1870765e38482_pcrid_719207693017_pgrid_165151408209_pntwk_g_pchan__pexid__ptid_kwd-10778630_&cid=aos-us-kwgo---slid---product-'

    title, headings, paragraphs = fetch_content(url)

    content = " ".join([title] + headings + paragraphs)
    '''
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"error" : "Failed to retrieve data"}), 500

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.string if soup.title else "No title found"
    '''
    return content

if __name__ == '__main__':
    app.run(debug=True)