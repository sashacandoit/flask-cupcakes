"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMG_URL = "https://i.postimg.cc/P5QB2c69/cupcake2.png"


class Cupcake(db.Model):
    """Cupcake Model"""

    __tablename__ = "cupcakes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Colum(db.Text, nullable=False, )