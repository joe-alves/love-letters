# import: flask_sqlalchemy 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Model called Letter  to from body 
class Letter(db.Model):
    __tablename__ = 'letters'
    id = db.Column(db.Integer, primary_key=True)
    to = db.Column(db.String(255), nullable=False)
    sender = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
