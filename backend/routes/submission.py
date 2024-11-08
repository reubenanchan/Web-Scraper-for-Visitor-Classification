from flask import Blueprint, request, jsonify # type: ignore
from scraping.scraping import fetch_content
from generate_qna.generate import generate_qna

submission_blueprint = Blueprint('submission', __name__)

@submission_blueprint.route('/submit')
def submit_url():
    #url = request.json.get('url')
    url = 'https://www.apple.com/ca/store?afid=p238%7CshFROjR3i-dc_mtid_1870765e38482_pcrid_719207693017_pgrid_165151408209_pntwk_g_pchan__pexid__ptid_kwd-10778630_&cid=aos-us-kwgo---slid---product-'
    title, headings, paragraphs = fetch_content(url)
    if title and headings and paragraphs:
        content = " ".join([title] + headings + paragraphs)
        qna = generate_qna(content)
        return qna
    else:
        return jsonify({"error": "Content could not be fetched or is restricted"}), 400
