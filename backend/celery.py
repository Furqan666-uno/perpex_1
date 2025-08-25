import os
import multiprocessing
from celery import Celery

multiprocessing.set_start_method("spawn", force=True)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app = Celery("backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()