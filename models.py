from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    date_published = db.Column(db.String(20), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(300), nullable=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    relationship = db.relationship(
        'Correction',
        backref='article',
        lazy=True,
        cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Article {self.id!r}: {self.title!r}>"
    
class Correction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)
    index = db.Column(db.Integer, nullable=False)
    explanation = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    __table_args__ = (
        db.UniqueConstraint('article_id', 'index', name='uq_article_index'),
    )

    def __repr__(self):
        return f"<Correction {self.id!r} for Article {self.article_id!r}>"