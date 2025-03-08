import sys
import re

# lê o arquivo de sequência
def le_arquivo_sequencia(nome_arquivo):
    arquivo = open(nome_arquivo, "r") 
    linha = arquivo.read() 
    linha = list(linha.rstrip()) # remove o \n e transforma em lista
    linha.insert(0, '-') # adiciona o gap no início da lista
    return(linha)

# lê o arquivo de mutações
def le_arquivo_mutacoes(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    linha = arquivo.read()
    linha = linha.rstrip() 
    mutacoes = linha.split(", ") # separa as mutações por vírgula
    return(mutacoes)

# faz a substituição do aminoácido
def substituir(lista, aa1, pos, aa2):
    if lista[pos] != aa1: # verifica se o aminoácido na posição pos é igual ao aminoácido aa1
        print(f"Erro: a posição {pos} não contém o aminoácido {aa1}") 
        exit()
    else:
        lista[pos] = aa2 # substitui o aminoácido aa1 pelo aminoácido aa2 na posição pos

def faz_substituicoes(lista, mut):
    for i in mut: # percorre a lista de mutações
        if i[0:3] != "del" and i[0:3] != "ins": # verifica se a mutação é de substituição
            aa1 = i[0] # pega o primeiro aminoácido da mutação
            aa2 = i[-1] # pega o último aminoácido da mutação
            pos = int(i[1:-1]) # pega a posição da mutação

            # Exemplo: mutação A67V -> aa1 = A, aa2 = V, pos = 67

            substituir(lista, aa1, pos, aa2) # faz a substituição do aminoácido

def deletar(lista, pos): 
    lista[pos] = "-" # deleta o aminoácido na posição pos

def faz_delecoes(lista, mut):
    for i in mut:
        if i[0:3] == "del":
            i = i.lstrip("del") # remove o "del" da mutação: del69-70 -> 69-70
            temp = i.split("-") # 69-70 -> [69, 70]
            pos1 = int(temp[0]) # ínicio do intervalo
            pos2 = int(temp[0]) # pode ser vazio

            if len(temp) > 1: # fim do intervalo, se não for vazio
                pos2 = int(temp[1])

            for j in range(pos1, pos2+1): # deleta os aminoácidos no intervalo
                deletar(lista, j)

def inserir(lista, pos, aa):
    lista.insert(pos, aa) # insere o aminoácido aa na posição pos

def faz_insercoes(lista, mut):
    for i in range(len(mut)-1, -1, -1): # percorre a lista de mutações de trás para frente
        if mut[i] [0:3] == "ins":
            mutacao = mut[i].lstrip("ins") # remove o "ins" da mutação: ins69A -> 69A
            pos = re.search("[\d]+", mutacao) # buscar um ou mais dígitos na mutação
            pos = int(pos.group()) # pega a posição da mutação
            sequencia = re.search("[A-Z]+", mutacao) # buscar uma ou mais letras maiúsculas na mutação
            sequencia = list(sequencia.group()) # transforma a sequência em uma lista
            sequencia.reverse() # inverte a sequência

            for aa in sequencia:
                inserir(lista, pos, aa)

def gerar_sequencia_final(lista):
    sequencia = ""

    for i in lista: 
        if i != "-": # se i não for um gap, adiciona o aminoácido à sequência
            sequencia += i

    return sequencia

def imprimir_comparativo(sequencia_original, sequencia_mutante):
    tamanho = min(len(sequencia_original), len(sequencia_mutante))

    for i in range(0, tamanho):
        print(f"{i} {sequencia_original[i]} {sequencia_mutante[i]}")


# verifica se o número de argumentos é válido
if len(sys.argv) != 3:
    print("USAGE: python3 <sequencias> <mutacoes>") 
    exit()

lista_original = le_arquivo_sequencia(sys.argv[1]) # lê a sequência original do arquivo na posição 1
mut = le_arquivo_mutacoes(sys.argv[2]) # lê as mutações do arquivo na posição 2

lista_mut = lista_original.copy() # cria uma cópia da lista original
faz_substituicoes(lista_mut, mut) # faz as substituições na lista mutante
faz_delecoes(lista_mut, mut) # faz as deleções na lista mutante
faz_insercoes(lista_mut, mut) # faz as inserções na lista mutante

# print(lista_original[67], lista_mut[67]) # imprime o aminoácido original e o mutante na posição 67 -> A V

sequencia_final = gerar_sequencia_final(lista_mut) # gera a sequência final mutante

imprimir_comparativo(lista_original, sequencia_final) # imprime o comparativo entre a sequência original e a mutante