# Import Module
import os
import unidecode

# Folder Path
path = r"C:\Users\mathe\Documents\GitHub\organizacao_recuperacao_informacao\tp2\Ex1\input"

# Change the directory
os.chdir(path)

# Read text File

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        x = f.read()
        print(x)

# iterate through all file
for file in os.listdir():
	# Check whether file is in text format or not
	if file.endswith(".txt"):
		file_path = f"{path}\\{file}"

		# call read text file function
		read_text_file(file_path)
