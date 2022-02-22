import time
from hero.celery import app

@app.task(name="do_something")
def do_something():
    start = time.perf_counter()
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping...")
    finish = time.perf_counter()
    print(f'Finished in {finish-start}')

