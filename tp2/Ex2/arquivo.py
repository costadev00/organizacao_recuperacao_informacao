import os
import math
from unidecode import unidecode

# Alterar para o path da pasta a ser lida!
path = "/home/runner/TP2-TFIDF"
os.chdir(path)


def read_text_file(file_path: str):
    with open(file_path, "r") as file:
        text_data = unidecode(file.read()).lower()
    return text_data.split()


# Necessario que o BoW esteja no path indicado, altere o nome do .txt caso necessario
vocabulario = read_text_file(path + "/vocabulario.txt")


def generate_frequency_list(data: list):
    """Gera vetor de frequencia referente ao BoW"""
    new_frequency_list = []
    frequency = 0
    for word in vocabulario:
        frequency = data.count(word)
        new_frequency_list.append(frequency)
    return new_frequency_list


def calculate_tf(data: list):
    tf_list = []
    for element in data:
        if (element != 0):
            log = math.log(element, 2)
            tf_list.append(1+log)
        else:
            tf_list.append(0)
    return tf_list


def count_files():
    count = 0
    for file in sorted(os.listdir()):
        if file.startswith("vocabulario"):
            continue
        if file.endswith(".txt"):
            count = count + 1
    return count


def calculate_idf(data: list):
    count_list = []
    tf_list = []
    count = 0
    for i in range(len(data[0])):
        count = 0
        for j in range(len(data)):
            if (data[j][i] > 0):
                count += 1
        count_list.append(count)

    for element in count_list:
        if (element != 0):
            tf_list.append(math.log(len(data)/element, 2))
        else:
            tf_list.append(0)
    return tf_list


tf_list = []
# Percorre todos os arquivos de gera uma lista de todos os TFS
for file in sorted(os.listdir()):
    tf = []
    # Condicional abaixo nao ira formular array do proprio vocabulario
    if file.startswith("vocabulario"):
        continue
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
        content_data = read_text_file(file_path)
        print("Arquivo: ", file)
        frequency_list = generate_frequency_list(content_data)
        print("Vetor de frequencia: ", frequency_list)
        tf = calculate_tf(frequency_list)
        print("TF: ", tf)
        print("\n")
        tf_list.append(tf)

idf_list = calculate_idf(tf_list)
print("IDF: ", idf_list)


def calculate_tf_idf():
    tf_idf_list = []
    for element in tf_list:
        tf_idf = []
        for i in range(len(element)):
            tf_idf.append(element[i] * idf_list[i])
        tf_idf_list.append(tf_idf)
    return tf_idf_list


print("\nTF-IDF dos arquivos acima, respectivamente: ", calculate_tf_idf())
