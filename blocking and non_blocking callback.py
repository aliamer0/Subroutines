import threading
import time

# Blocking function
def slow_function(callback):
    import time
    time.sleep(3)  # Simulate a delay
    result = "Data processed"
    callback(result)

def print_result(result):
    print("Callback result:", result)

# Execution (Blocking)
print("Starting...")
slow_function(print_result)
print("Finished")  # This waits for slow_function to complete

# Non-blocking function using a thread
def slow_function(callback):
    def task():
        time.sleep(3)  # Simulate a delay
        result = "Data processed"
        callback(result)
    threading.Thread(target=task).start()

def print_result(result):
    print("Callback result:", result)

# Execution (Non-Blocking)
print("Starting...")
slow_function(print_result)
print("Finished")  # This runs immediately without waiting
