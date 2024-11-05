import threading
import time

def worker_thread():
    print("Worker thread started")
    time.sleep(2)
    print("Worker thread finished")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create a new thread
    thread = threading.Thread(target=worker_thread)

    # Start the thread
    thread.start()

    # Main thread continues to execute
    print("Main thread continues")

    # Wait for the worker thread to finish
    thread.join()

    print("Main thread finished")
