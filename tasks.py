import requests
from database import SessionLocal
from models import News
from datetime import datetime
from celery import Celery

# Celery Configuration
celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def fetch_and_store_news():
    api_key = 'aa2a83c1187c477d957848366d09548a'
    url = 'https://newsapi.org/v2/top-headlines?' \
          'sources=bbc-news&' \
          f'apiKey={api_key}'
    response = requests.get(url)
    news_data = response.json()

    db = SessionLocal()
    for article in news_data.get("articles", []):
        db_news = News(
            source_id=article.get("source", {}).get("id"),
            source_name=article.get("source", {}).get("name"),
            author=article.get("author"),
            title=article.get("title"),
            description=article.get("description"),
            url=article.get("url"),
            url_to_image=article.get("urlToImage"),
            published_at=article.get("publishedAt"),
            content=article.get("content"),
            created_at = datetime.now()
        )
        db.add(db_news)

    db.commit()
    db.close()