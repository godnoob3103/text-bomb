import random
import string
import threading

def generate_random_text():
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(100, 1000)))

def save_text_to_file(text):
    with open("text.txt", "a") as file:  # Open file in append mode
        file.write(text + "\n")

def worker():
    while True:
        random_text = generate_random_text()
        save_text_to_file(random_text)

if __name__ == "__main__":
    num_threads = 10  # Adjust the number of threads based on your system's capabilities
    threads = []
    
    # Create and start the worker threads
    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
