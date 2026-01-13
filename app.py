from flask import Flask
from dotenv import load_dotenv
from extensions import db
from routes import main
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)