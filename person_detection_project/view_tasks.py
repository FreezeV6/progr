from celery.app.control import Inspect
from tasks import celery_app

# Inspect Celery workers
i = celery_app.control.inspect()

print("Active tasks:", i.active())
print("Reserved tasks:", i.reserved())
print("Scheduled tasks:", i.scheduled())

registered_tasks = celery_app.tasks.keys()
print("Registered tasks:", registered_tasks)
