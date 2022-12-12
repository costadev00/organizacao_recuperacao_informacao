import os
import math
from unidecode import unidecode

# Altere para o caminho da pasta que será lida!
caminho = "/home/matheuscosta/Documentos/GitHub/organizacao_recuperacao_informacao/tp2/Ex1/input"
os.chdir(caminho)


def ler_arquivo_de_texto(caminho_do_arquivo: str):
    with open(caminho_do_arquivo, "r") as arquivo:
        dados_de_texto = unidecode(arquivo.read()).lower()
    return dados_de_texto.split()


# É necessário que o BoW esteja no caminho indicado, altere o nome do .txt se necessário
vocabulario = ler_arquivo_de_texto(caminho + "/voc.txt")


def gerar_lista_de_frequencias(dados: list):
    nova_lista_de_frequencias = []
    frequencia = 0
    for palavra in vocabulario:
        frequencia = dados.count(palavra)
        nova_lista_de_frequencias.append(frequencia)
    return nova_lista_de_frequencias


def calcular_tf(dados: list):
    lista_de_tf = []
    for elemento in dados:
        if (elemento != 0):
            log = math.log(elemento, 2)
            lista_de_tf.append(1+log)
        else:
            lista_de_tf.append(0)
    return lista_de_tf



def contar_arquivos():
    contador = 0
    for arquivo in sorted(os.listdir()):
        if arquivo.comeca_com("voc"):
            continue
        if arquivo.termina_com(".txt"):
            contador = contador + 1
    return contador

def calcular_idf(dados: list):
    lista_contador = []
    lista_tf = []
    contador = 0
    for i in range(len(dados[0])):
        contador = 0
        for j in range(len(dados)):
            if (dados[j][i] > 0):
                contador += 1
        lista_contador.append(contador)

    for elemento in lista_contador:
        if (elemento != 0):
            lista_tf.append(math.log(len(dados)/elemento, 2))
        else:
            lista_tf.append(0)
    return lista_tf



lista_tf = []
# Percorre todos os arquivos de gera uma lista de todos os TFS
for arquivo in sorted(os.listdir()):
    tf = []
    # Condicional abaixo não irá formular array do próprio vocabulário
    if arquivo.startswith("voc"):
        continue
    if arquivo.endswith(".txt"):
        caminho_arquivo = f"{caminho}/{arquivo}"
        conteudo_dados = ler_arquivo_de_texto(caminho_arquivo)
        print("Arquivo: ", arquivo)
        lista_frequencia = gerar_lista_de_frequencias(conteudo_dados)
        print("📊 Vetor de frequência: ", lista_frequencia)
        tf = calcular_tf(lista_frequencia)
        print("TF = ", tf)
        print("\n")

        lista_tf.append(tf)

lista_idf = calcular_idf(lista_tf)
print("📊 IDF = ", lista_idf)


def calcular_tf_idf():
    lista_tf_idf = []
    for elemento in lista_tf:
        tf_idf = []
        for i in range(len(elemento)):
            tf_idf.append(elemento[i] * lista_idf[i])
        lista_tf_idf.append(tf_idf)
    return lista_tf_idf


print("\nTF-IDF =  ", calcular_tf_idf())
