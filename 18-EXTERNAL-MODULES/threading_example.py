# Multithreading in Python
# This program demonstrates how to create and run multiple threads.

import threading
import time


# Function executed by each thread
def thread_worker(thread_number):
    print(f"Thread {thread_number} has started.")

    # Simulate some work using sleep
    time.sleep(2)

    print(f"Thread {thread_number} has finished.")


# List to store thread objects
thread_list = []


# Create and start threads
for thread_index in range(3):
    new_thread = threading.Thread(target=thread_worker, args=(thread_index,))

    thread_list.append(new_thread)
    new_thread.start()


# Wait for all threads to complete execution
for thread in thread_list:
    thread.join()


print("All threads have finished execution.")
