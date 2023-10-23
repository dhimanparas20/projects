from flask import Flask, jsonify
import threading
import time

app = Flask(__name__)

# Event flags to signal when background tasks are complete
task1_completed = threading.Event()
task2_completed = threading.Event()

# Function to run in a separate thread
def background_task():
    for i in range(100000):
        print("Thread 1")  # Simulate a time-consuming task
    task1_completed.set()  # Signal that task 1 is complete

def background_task2():
    for i in range(100000):
        print("Thread 2")  # Simulate a time-consuming task
    task2_completed.set()  # Signal that task 2 is complete

@app.route('/', methods=['GET'])
def start_background_task():
    # Start the background tasks in separate threads
    background_thread = threading.Thread(target=background_task)
    background_thread2 = threading.Thread(target=background_task2)
    background_thread.start()
    background_thread2.start()

    # Wait for the background tasks to complete
    background_thread.join()
    background_thread2.join()

    # Return a response based on task completion
    if task1_completed.is_set() and task2_completed.is_set():
        response = {"status": "Background tasks completed."}
    else:
        response = {"status": "Background tasks still running."}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
