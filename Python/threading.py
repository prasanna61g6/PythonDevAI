"""
Concurrency and Threading in Python
- Concurrency
- Parallelism
- Process vs Thread
- Multithreading
- Thread Lifecycle
- Thread Arguments
- join()
- Daemon Threads
- Race Conditions
- Lock and RLock
- Semaphore
- Event
- Condition
- ThreadPoolExecutor
- CPU-bound vs I/O-bound tasks
- threading vs multiprocessing

"""


# ==================== CONCURRENCY AND PARALLELISM ====================

# Concurrency:
# Multiple tasks make progress during overlapping periods of time.
#
# Parallelism:
# Multiple tasks execute at the same time using multiple CPU cores.
#
# Example:
#
# Concurrency:
# Task A -> Task B -> Task A -> Task B
#
# Parallelism:
# Core 1 -> Task A
# Core 2 -> Task B


# ==================== PROCESS VS THREAD ====================

# Process:
# - Independent running program
# - Has its own memory space
# - More expensive to create
#
# Thread:
# - Smaller execution unit inside a process
# - Threads in the same process share memory
# - Usually lighter than processes


# ==================== BASIC THREADING ====================

import threading
import time


def print_numbers():
    for number in range(1, 6):
        print(number)
        time.sleep(0.5)


def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print(letter)
        time.sleep(0.5)


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads have finished.")


# ==================== THREAD ARGUMENTS ====================

def greet(name, times):
    for _ in range(times):
        print(f"Hello, {name}")
        time.sleep(0.2)


thread = threading.Thread(
    target=greet,
    args=("Prasanna", 3)
)

thread.start()
thread.join()


# ==================== join() ====================

# join() makes the current thread wait until
# another thread completes its execution.

def download_file():
    print("Downloading file...")
    time.sleep(2)
    print("Download complete.")


thread = threading.Thread(target=download_file)

thread.start()

thread.join()

print("Processing downloaded file.")


# ==================== DAEMON THREAD ====================

# A daemon thread runs in the background.
# It automatically stops when all non-daemon threads finish.

def background_task():
    while True:
        print("Background task running...")
        time.sleep(1)


daemon_thread = threading.Thread(
    target=background_task,
    daemon=True
)

daemon_thread.start()

time.sleep(2)

print("Main program finished.")


# ==================== RACE CONDITION ====================

# A race condition occurs when multiple threads access
# and modify shared data at the same time, causing
# unpredictable results.

counter = 0


def increment_counter():
    global counter

    for _ in range(100000):
        counter += 1


thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Counter without synchronization: {counter}")


# ==================== LOCK ====================

# A Lock allows only one thread at a time
# to access a critical section.

counter = 0

lock = threading.Lock()


def safe_increment():
    global counter

    for _ in range(100000):
        with lock:
            counter += 1


thread1 = threading.Thread(target=safe_increment)
thread2 = threading.Thread(target=safe_increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Counter with Lock: {counter}")


# ==================== RLOCK ====================

# RLock stands for Reentrant Lock.
# The same thread can acquire it multiple times.

rlock = threading.RLock()


def outer_function():
    with rlock:
        print("Outer function")

        inner_function()


def inner_function():
    with rlock:
        print("Inner function")


thread = threading.Thread(target=outer_function)

thread.start()
thread.join()


# ==================== SEMAPHORE ====================

# A Semaphore controls how many threads can access
# a resource at the same time.

semaphore = threading.Semaphore(2)


def access_resource(thread_number):
    with semaphore:
        print(f"Thread {thread_number} is using the resource.")

        time.sleep(1)

        print(f"Thread {thread_number} finished.")


threads = []

for number in range(1, 6):
    thread = threading.Thread(
        target=access_resource,
        args=(number,)
    )

    threads.append(thread)

    thread.start()


for thread in threads:
    thread.join()


# ==================== EVENT ====================

# An Event allows one thread to signal other threads.

event = threading.Event()


def wait_for_signal():
    print("Worker is waiting.")

    event.wait()

    print("Worker received the signal.")


worker = threading.Thread(target=wait_for_signal)

worker.start()

time.sleep(1)

print("Main thread sends the signal.")

event.set()

worker.join()


# ==================== CONDITION ====================

# Condition allows threads to wait for a particular
# condition before continuing.

condition = threading.Condition()

data_ready = False


def consumer():
    global data_ready

    with condition:
        print("Consumer is waiting.")

        condition.wait_for(lambda: data_ready)

        print("Consumer received the data.")


def producer():
    global data_ready

    time.sleep(1)

    with condition:
        data_ready = True

        print("Producer created the data.")

        condition.notify()


consumer_thread = threading.Thread(target=consumer)
producer_thread = threading.Thread(target=producer)

consumer_thread.start()
producer_thread.start()

consumer_thread.join()
producer_thread.join()


# ==================== THREAD POOL ====================

# ThreadPoolExecutor manages a group of reusable threads.

from concurrent.futures import ThreadPoolExecutor


def square(number):
    time.sleep(0.5)
    return number * number


numbers = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=3) as executor:

    results = executor.map(square, numbers)

    for result in results:
        print(result)


# ==================== SUBMIT AND FUTURES ====================

# submit() schedules individual tasks and returns a Future.

def calculate_square(number):
    time.sleep(1)
    return number * number


with ThreadPoolExecutor(max_workers=2) as executor:

    future1 = executor.submit(calculate_square, 5)
    future2 = executor.submit(calculate_square, 10)

    print(future1.result())
    print(future2.result())


# ==================== CPU-BOUND VS I/O-BOUND ====================

# CPU-bound task:
# Requires heavy CPU computation.
#
# Examples:
# - Large mathematical calculations
# - Image processing
# - Machine Learning computation
#
# Multiprocessing is usually more suitable.
#
#
# I/O-bound task:
# Spends significant time waiting for external operations.
#
# Examples:
# - Reading files
# - API requests
# - Database operations
# - Network communication
#
# Multithreading or async programming can be useful.


# ==================== THREADING VS MULTIPROCESSING ====================

# Threading:
# - Multiple threads inside one process
# - Shared memory
# - Lightweight
# - Useful mainly for I/O-bound tasks
#
# Multiprocessing:
# - Multiple independent processes
# - Separate memory
# - Can use multiple CPU cores
# - Useful for CPU-bound tasks


# ==================== PRACTICAL EXAMPLE ====================

# Simulating multiple file downloads.

def download(url):
    print(f"Starting download: {url}")

    time.sleep(1)

    print(f"Completed download: {url}")

    return url


urls = [
    "file_1",
    "file_2",
    "file_3",
    "file_4"
]


with ThreadPoolExecutor(max_workers=2) as executor:

    futures = [
        executor.submit(download, url)
        for url in urls
    ]

    for future in futures:
        future.result()


print("All downloads completed.")