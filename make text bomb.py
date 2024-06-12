import random
import string
import time

def generate_random_text():
    text = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(100, 1000)))
    return text

def save_text_to_file(text):
    with open("text.txt", "a") as file:  # Open file in append mode
        file.write(text + "\n")

if __name__ == "__main__":
    while True:
        random_text = generate_random_text()
        save_text_to_file(random_text)
        print("Random text appended to text.txt")
        time.sleep(0.1)  # Adding a short delay to prevent system overload
