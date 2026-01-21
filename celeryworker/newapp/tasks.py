from celery import shared_task
import requests
from sentry_sdk import capture_exception

@shared_task
def check_webpage():
  try:
    response = requests.get("http://localhost:8000")
    if response.status_code != 200:
      raise Exception("Website is down")
  except requests.exceptions.RequestException as e:
    capture_exception(e)
  
  
# @shared_task
# def task2():
#   return 