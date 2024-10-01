"""
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos das famílias da cidade. Aprefeitura deseja saber

a) total de famílias que responderam a pesquisa;
b)média do salário da população;
c) média do números de filhos;
d) maior salário;
e) menor salário.

Crie um menu com as seguintes opções.
código | descrição
  1       Adicionar família
  2       Exibir rsultados
  3       Sair

Ao adicionar uma família, deve-se limpar o terminal e apresentar o menu novamente.
1. Salve os dados em um arquivo com nome: pesquisa_prefeitura.txt
2. O programa deve ler o arquivo para exibir os dados salvos.  

"""

import os
os.system("cls || clear")

from dataclasses import dataclass


@dataclass
class Cliente:
    quantidade_de_filhos : int
    salario : float

def menu ():
    print("""
   === MENU ===

1. Adicionar família          
2. Exibir os resultados          
3. Sair             

          """)
    
    
def criando_arquivo(a,b):
    with open(a, "a") as lista_clientes:
        for cliente in b:
            lista_clientes.write(f"{cliente.quantidade_de_filhos}, {cliente.salario}\n")


def lendo_arquivo(a):
    with open(a, "r") as arquivo_clientes:
        for linha in arquivo_clientes:
            quantidade_de_filhos, salario = linha.strip() .split(",")
            lista_total.append(Cliente(quantidade_de_filhos=int(quantidade_de_filhos), salario=float(salario)))
    return lista_total



def media_total(a):
    QNT =  len(a) 
    soma = sum(a)

    if QNT == 0:
        return 0
    else: 
        media = soma / QNT
        return media
lista_total = []


def limpar_tela():
    os.system("cls || clear ")

contador = 0
while True: 
    menu()
    opcao = (input("Resposta: "))
    match opcao:
        case "1":
            cliente = Cliente(
            quantidade_de_filhos = int(input("Quantos filhos você tem: ")),
            salario = float(input("Seu salário: "))
            )
            lista_total.append(cliente)
            nome_arquivo_cliente = "pesquisa_prefeitura.txt"
            criando_arquivo(nome_arquivo_cliente, lista_total)
            
        case "2":
            contador = 0
            nome_arquivo_cliente = "pesquisa_prefeitura.txt"
            lista_salario=[]
            lista_filhos = []
            lista_total_definitiva = lendo_arquivo(nome_arquivo_cliente)
            for cliente in lista_total_definitiva:
                lista_filhos.append(cliente.quantidade_de_filhos)
                lista_salario.append(cliente.salario)
                contador += 1
            media_salario = media_total(lista_salario)
            media_filhos = media_total(lista_filhos)
            maior_salario = max(lista_salario)
            menor_salario = min(lista_salario) 
            print("\n==== Resultados ====")
            print(f"Total de famílias: {contador}")
            print(f"Média do salário: {media_salario}")
            print(f"Média do número de filhos: {media_filhos}")
            print(f"Maior Salário: {maior_salario}")
            print(f"Menor Salário: {menor_salario}")
            
                            
            
        case "3":
            break
            
        case _:
            print("Opção inválida")
            continue
    






        




 



    