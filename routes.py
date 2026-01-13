from flask import Blueprint, render_template, request
from models import Article, Correction

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
            corrections = [
                {"explanation": c.explanation} 
                for c in selected_article.relationship
            ]

    return render_template(
        "index.html",
        articles=articles,
        selected_article=selected_article,
        corrections=corrections
    )
