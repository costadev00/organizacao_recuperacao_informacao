# Import Module
import os
import unidecode

# Folder Path
path = "/home/matheuscosta/Documentos/GitHub/organizacao_recuperacao_informacao/tp2/Ex1/input"

# Change the directory
os.chdir(path)
# Read text File


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        x = f.read()
        x = unidecode.unidecode(x)
        x = x.lower()
        return x


# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"

        # call read text file function
        x = read_text_file(file_path)
        # remove the repeated words of x
        x = list(dict.fromkeys(x.split()))
        x = sorted(x)
        #remove all the ',' characters of x
        x = [i.replace(',', '') for i in x]
        #make a variable that reads voc.txt
        v = read_text_file("voc.txt")
        voc = v.split()
        # print(v)
        # make a bag of words of x and output a txt file
        with open("output.txt", "w") as output:
            for i in range(len(voc)):
                if voc[i] in x:
                    # print(voc[i])
                    print(1)
                else:
                    print(0)
