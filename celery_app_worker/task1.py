import time
from . import app
@app.task
def add(x, y):
    print("add task called!")
    time.sleep(2)
    return x + y