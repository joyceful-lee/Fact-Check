from flask import Blueprint, render_template, request
from models import db, Article, Correction
from services.article_loading import get_all_articles

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    articles = Article.query.all()
    selected_article = None
    corrections = []

    if request.method == "POST":
        article_id = request.form.get("article_id")
        selected_article = Article.query.get(article_id)
        if selected_article:
            # Convert corrections to list of dicts
            corrections = [
                {"explanation": c.explanation} 
                for c in selected_article.relationship  # or selected_article.corrections if you named it that
            ]

    return render_template(
        "index.html",
        articles=articles,
        selected_article=selected_article,
        corrections=corrections
    )
