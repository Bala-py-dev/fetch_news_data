from fastapi import FastAPI
from datetime import timedelta
from tasks import fetch_and_store_news, celery_app

app = FastAPI()

# FastAPI Route
@app.get("/fetch-news")
def fetch_news():
    fetch_and_store_news()
    return {"status": "success", "message": "News fetched and stored in the database."}

# Celery Configuration for Scheduled Task
celery_app.conf.beat_schedule = {
    'fetch-news-task': {
        'task': 'tasks.fetch_and_store_news',
        'schedule': timedelta(minutes=1),
    },
}