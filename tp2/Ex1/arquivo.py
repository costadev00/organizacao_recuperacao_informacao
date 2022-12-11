import os

# directory where the text files are located
dir_path = "/input/"

# list all files in the directory
files = os.listdir(dir_path)

# read the contents of each file and print it
for file in files:
    with open(os.path.join(dir_path, file), "r") as f:
        print(f.read())
