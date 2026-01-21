from celery import shared_task
import time
from django.core.management import call_command

# @shared_task
# def task1():
#   return 

# @shared_task
# def task2():
#   return 

@shared_task(queue='tasks')
def management_command():
    call_command("test_command")

# @shared_task(queue='celery:1')
# def tp2():
#     time.sleep(3)

# @shared_task(queue='celery:2')
# def tp3():
#     time.sleep(3)

# @shared_task(queue='celery:3')
# def tp4():
#     time.sleep(3)
