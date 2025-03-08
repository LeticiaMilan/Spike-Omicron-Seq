import sys

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
def substituicao(lista, aa1, pos, aa2):
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

            substituicao(lista, aa1, pos, aa2) # faz a substituição do aminoácido

# verifica se o número de argumentos é válido
if len(sys.argv) != 3:
    print("USAGE: python3 <sequencias> <mutacoes>") 
    exit()

lista_original = le_arquivo_sequencia(sys.argv[1]) # lê a sequência original do arquivo na posição 1
mut = le_arquivo_mutacoes(sys.argv[2]) # lê as mutações do arquivo na posição 2

lista_mut = lista_original.copy() # cria uma cópia da lista original
faz_substituicoes(lista_mut, mut) # faz as substituições na lista mutante