from flask import Blueprint

notes = Blueprint('notes', __name__)


@notes.route('/', methods=["GET"])
def home_():
    return "Notes Endpoint"
