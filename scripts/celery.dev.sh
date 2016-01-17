source venv/bin/activate
celery -A worker_development worker -l debug -C
