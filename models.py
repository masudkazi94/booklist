from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text)
    year = db.Column(db.Integer)
    read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Book{self.title}>'