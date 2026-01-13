from models import Article

def get_all_articles():
    """Fetch all articles from the database."""
    return Article.query.order_by(Article.date_created.desc()).all()