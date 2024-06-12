import random
import string

def generate_random_text():
text = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(100, 1000)))
return text

def save_text_to_file(text):
with open("text.txt", "a") as file: # Open file in append mode
file.write(text + "\n")

if name == "main":
while True:
random_text = generate_random_text()
save_text_to_file(random_text)
print("Random text appended to text.txt")
# No delay or a very short delay (be cautious not to overload system)