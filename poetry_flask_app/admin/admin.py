from flask import Blueprint

admin = Blueprint('admin', __name__)


@admin.route('/', methods=["GET"])
def home_():
    return "Admin Endpoint"
