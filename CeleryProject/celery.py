from __future__ import absolute_import, unicode_literals
import imp
import os
from pickle import TRUE

from celery import Celery
from django.conf import settings
from pytz import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryProject.settings')

app = Celery('CeleryProject.settings')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    
}




app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print('Request : ' , self.request)