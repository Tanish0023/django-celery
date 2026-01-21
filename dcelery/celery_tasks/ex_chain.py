from celery import chain
from dcelery.celery_config import app

@app.task(queue='tasks')
def add(x,y):
  return x + y

@app.task(queue='tasks')
def multiply(result):
  if result == 5:
    raise ValueError("Cannot divide by zero")
  
  return result * 2

    
def run_tasks_chain():
  task_group = chain(add.s(2 , 3), multiply.s())
  result = task_group.apply_async()
  result.get()