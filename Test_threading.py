import threading
import time

def print_numbers():
    for i in range(10):
        time.sleep(0.5)
        print(f"Number: {i}")

def print_letters():
    for letter in 'abcdefghij':
        time.sleep(0.5)
        print(f"Letter: {letter}")

# Creating threads
number_thread = threading.Thread(target=print_numbers)
letter_thread = threading.Thread(target=print_letters)

# Starting threads
number_thread.start()
letter_thread.start()

# Waiting for threads to complete
number_thread.join()
letter_thread.join()

print("Both threads have finished.")
