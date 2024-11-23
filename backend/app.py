from flask import Flask, jsonify # type: ignore
from flask_cors import CORS
from routes.submission import submission_blueprint
from routes.database_entry import database_entry_blueprint
import requests
from bs4 import BeautifulSoup
from scraping.scraping import fetch_content
import psycopg2
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(database="web_scraper", user="postgres", 
                        password="postgres", host="localhost", port="5432")

cur = conn.cursor()

# Create tables to store the data
cur.execute('''
    CREATE TABLE IF NOT EXISTS website_data (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        url TEXT
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id SERIAL PRIMARY KEY,
        website_id INT REFERENCES website_data(id),
        question TEXT,
        answer TEXT
    );
''')

# Insert the main website data
cur.execute('''
    INSERT INTO website_data (title, url)
    VALUES (%s, %s)
    RETURNING id;
''', (
    "\n    All products | Books to Scrape - Sandbox\n", 
    "https://books.toscrape.com/"
))

website_id = cur.fetchone()[0]

# Insert the questions and answers
questions = [
    ("What type of books are you interested in purchasing?", "Fiction"),
    ("How often do you buy books online?", "Daily"),
    ("What is your preferred format for books?", "Paperback"),
    ("What is your budget for purchasing books?", "Under £10"),
    ("Which genre do you enjoy reading the most?", "Mystery/Thriller")
]

for question, answer in questions:
    cur.execute('''
        INSERT INTO questions (website_id, question, answer)
        VALUES (%s, %s, %s);
    ''', (website_id, question, answer))

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

app.register_blueprint(submission_blueprint)
app.register_blueprint(database_entry_blueprint)

def get_db_connection():
    """Establish and return a connection to the database."""
    conn = psycopg2.connect(
        database="web_scraper",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    return conn

@app.route('/')
def home():
    return "Hello, world!"

@app.route('/add-data', methods=['POST'])
def add_data():
    """Endpoint to add data to the database."""
    try:
        # Parse JSON request data
        data = request.get_json()
        logging.debug(f"Received data: {data}")
        title = data['title']
        url = data['url']
        responses = data['responses']

        return print(title)

        if not title or not url or not responses:
            return jsonify({'error': 'Missing required fields'}), 400

        # Database connection
        conn = get_db_connection()
        cur = conn.cursor()

        # Insert website data
        cur.execute('''
            INSERT INTO website_data (title, url)
            VALUES (%s, %s)
            RETURNING id;
        ''', (title, url))
        website_id = cur.fetchone()[0]

        # Insert questions and answers
        for response in responses:
            question = response['Question'].get('question')
            answer = response['Question'].get('answer')
            cur.execute('''
                INSERT INTO questions (website_id, question, answer)
                VALUES (%s, %s, %s);
            ''', (website_id, question, answer))

        # Commit the transaction
        conn.commit()

        # Close connection
        cur.close()
        conn.close()

        return jsonify({'message': 'Data added successfully', 'website_id': website_id}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
