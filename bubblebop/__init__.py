from flask import Flask, render_template
from .config import Configuration
from .models import db, 
from .love_letter_form import LoveLetter

from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app) # It connects your db instance to the Flask app
migrate = Migrate(app, db)

@app.route("/")
def whatever_i_want():
    letter_form = LoveLetter()
    return render_template("form.html", leForm=letter_form)