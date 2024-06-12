import subprocess

while True:
    for _ in range(3):  # Open the file 3 times in each iteration
        subprocess.Popen(["start", "text.txt"], shell=True)
