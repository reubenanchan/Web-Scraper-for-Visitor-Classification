from flask import Blueprint, request, jsonify # type: ignore

database_entry_blueprint = Blueprint('database_entry', __name__)

@database_entry_blueprint.route('/database', methods=['POST'])
def create_database_entry():
    data = request.get_json()
    # Simulating a database connection
    title = data['title']
    return jsonify(title), 201