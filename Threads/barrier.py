"""
A threading.Barrier in Python is a synchronization primitive that allows a
specified number of threads to wait until
all of them have reached a certain point in their execution.
Once this point is reached, all threads are released
to continue their execution.

How it Works:

Creation:

You create a Barrier object with a specific number of parties (threads).

Waiting:

Each thread calls the wait() method on the barrier.
If the number of threads that have reached the barrier is less than the specified
number of parties, the thread is
blocked until the required number is reached.

Release:

Once the required number of threads have called wait(), all of them are released simultaneously.
"""
import threading
import time

def worker(barrier, name):
    print(f"{name} waiting at the barrier")
    barrier.wait()
    print(f"{name} released from the barrier")

barrier = threading.Barrier(3)

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(barrier, f"Thread {i+1}"))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

"""
Explanation:

We create a Barrier object with 3 parties.
Three threads are created, each calling the worker function with the barrier object.
Each thread prints a message, reaches the barrier, and calls barrier.wait().
Once all three threads have reached the barrier, they are released simultaneously.
Each released thread prints a message indicating it has been released.
Key Points:

Synchronization: Ensures that a group of threads coordinate their actions.
Efficiency: Avoids unnecessary waiting and ensures that threads proceed together.
Flexibility: Can be used in various scenarios, such as parallel processing, data synchronization, and task coordination.
By understanding and effectively using threading.Barrier, you can optimize your multi-threaded Python applications and 
improve their overall performance.
"""
