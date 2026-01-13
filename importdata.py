import csv
from flask import request
from sqlalchemy.exc import IntegrityError
from app import app
from models import db, Article, Correction

MODEL = Correction  # Change to Correction to import corrections

with app.app_context():
    if MODEL == Correction:
        filename = "DB - corrections.csv"
        for a in Article.query.all():
            print(a.id, a.title)

        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                article = Article.query.filter_by(id=row['article_id']).first()


                if not article:
                    print(f"Skipping: article not found ({row['article_id']})")
                    continue

                correction = Correction(
                    id=int(row["id"]),
                    article_id=article.id,
                    index=int(row["index"]),
                    explanation=row["explanation"].strip()
                )
                print(correction.article_id)
                print(correction.index)

                try:
                    db.session.add(correction)
                    db.session.commit()
                    print("Added")
                except IntegrityError:
                    db.session.rollback()
                    print("Skipped: duplicate")

        print("Correction import complete (duplicates skipped)")
    else:
        filename = "DB - articles.csv"
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                article = Article(
                    id=int(row["id"]),
                    title=row["title"].strip(),
                    content=row["content"].strip(),
                    link=row["link"].strip(),
                    date_published=row["date_published"].strip(),
                    publisher=row["publisher"].strip()
                )
                print(article.id)
                print(article.title)
                print(article.content)
                print(article.date_published)
                print(article.publisher)
                print(article.date_created)
                
                try:
                    db.session.add(article)
                    db.session.commit()
                    print("Added")
                except IntegrityError:
                    db.session.rollback()
                    print("Skipped: duplicate")

        print("Article import complete (duplicates skipped)")
