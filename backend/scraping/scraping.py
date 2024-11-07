import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser

def fetch_content(url):
    rp = RobotFileParser()
    rp.set_url(f'{url}/robots.txt')
    rp.read()
    if rp.can_fetch("*", url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headings = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])]
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        title = soup.title.string if soup.title else "No title found"
        return title, headings, paragraphs
    else:
        return None, None