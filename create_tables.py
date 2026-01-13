from app import app, db
from models import Article, Correction

with app.app_context():
    db.create_all()
    print("Tables created successfully.")