import threading
import time
import random

shared_resource = 0
#locking
myLock = threading.Lock()

def increment_resource(num_iterations):
    global shared_resource
    global myLock
    for _ in range(num_iterations):
        time.sleep(.001)
        with myLock:
            shared_resource += random.randint(-5,5)

threads = []
num_threads = 10
num_iterations = 1000

for _ in range(num_threads):
    thread = threading.Thread(target=increment_resource,
                              daemon=True, args=(num_iterations,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Final shared resource value:", shared_resource)