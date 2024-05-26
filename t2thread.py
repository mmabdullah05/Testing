import threading

# Shared resource
counter = 0
counter_lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(1000):
        with counter_lock:
            counter += 1

# Creating threads
threads = []
for _ in range(10):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# Waiting for all threads to complete
for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")
