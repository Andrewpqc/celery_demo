import time
from . import app
@app.task
def sub(x, y):
    print("sub task called")
    time.sleep(5)
    return x / y