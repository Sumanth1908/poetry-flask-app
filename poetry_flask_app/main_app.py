from flask import Flask

from poetry_flask_app.admin.admin import admin
from poetry_flask_app.notes.notes import notes

app = Flask(__name__)

app.register_blueprint(notes, url_prefix='/notes')
app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)
