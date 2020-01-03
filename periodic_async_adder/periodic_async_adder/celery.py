import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'periodic_async_adder.settings')

celery_app = Celery('periodic_async_adder')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'add-every-2-seconds': {
        'task': 'thumbnailer.tasks.adding_task',
        'schedule': 2.0,
        'args': (16, 16)
    },
    'print-name-every-5-seconds': {
        'task': 'thumbnailer.tasks.print_msg',
        'schedule': 5.0,
        'args': ("DjangoPY",)
    },
}
