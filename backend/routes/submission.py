from flask import Blueprint, request, jsonify # type: ignore
from scraping.scraping import fetch_content
from generate_qna.generate import generate_qna

submission_blueprint = Blueprint('submission', __name__)

def create_output(title, url, questions):
    return {
        "title": title,
        "url": url,
        "questions": questions
    }

def add_question(question, choices):
    return {
        "question": question,
        "choices": choices
    }

@submission_blueprint.route('/submit_url', methods=['POST'])
def submit_url():
    data = request.get_json()
    user_input = data['url']
    print(user_input)
    q_list = []
    title, headings, paragraphs = fetch_content(user_input)
    if title and headings and paragraphs:
        content = " ".join([title] + headings + paragraphs)
        question_bank = generate_qna(content)
        for i in range(len(question_bank)):
            q_list.append(add_question(question_bank[i].question, question_bank[i].choices))
        output = create_output(title, user_input, q_list)
        return output
    else:
        return jsonify({"error": "Content could not be fetched or is restricted"}), 400
