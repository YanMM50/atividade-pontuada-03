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
class Familia:
    quantidade_de_filhos = int
    salario = float



def coletando_dados():
    quantidade_filhos = []
    salario = []
    while True:
        filhos = Familia(
            qnt_filhos = int(input("Quantos filhos você tem: "))

        )
        salarios = Familia(
            salarios = float(input("Seu salário: "))

            )
        quantidade_filhos.append(filhos)
        salario.append(salarios)

        continuar = input("deseja continuar: ").strip().lower().upper()
        if continuar == "sim":
            continue
        elif continuar == "não":
            break

        
    return quantidade_filhos, salario


qnt_filhos_lista, salario_lista = coletando_dados()


def coletando_dados():
    quantidade_filhos = []
    salario = []
    while True:
        filhos = Cliente(
            qnt_filhos = int(input("Quantos filhos você tem: "))

        )
        salarios = Cliente(
            salarios = float(input("Seu salário: "))

            )
        quantidade_filhos.append(filhos)
        salario.append(salarios)

        continuar = input("deseja continuar: ").strip().lower().upper()
        if continuar == "sim":
            continue
        elif continuar == "não":
            break

        
    return quantidade_filhos, salario


qnt_filhos_lista, salario_lista = coletando_dados()
def menu ():
    print("""
    
código | descrição

1.       Adicionar família          
2.       Exibir os resultados          
3.       Sair             
          """)
    
def opcoes(n1):
    opcao = (input("Digite a sua opção: "))

    while True:
        menu()
        opcao = input("Digite a sua opção: ")
        
        match opcao:
            case "1":
                n1.append("Adicionar a família")
            case "2":
                n1.append("Exibir os dados")
            case "3":
                n1.append("Sair")
            case _:
                print("Opção inválida")
                continue



#  Definindo o nome do arquivo
nome_do_arquivo = "pesquisa_prefeitura.txt"

# Abrindo arquivo e definindo que será feita a escrita de dados.

print("\n=== Acessando dados de um arquivo ===")
with open(nome_do_arquivo, "w") as arquivo_da_prefeitura:
    for linha in arquivo_da_prefeitura:
        quantidade_filhos, salario = linha.strip().split(",")
        lista_de_alunos.append(Aluno(nome=nome, idade= int(idade)))



print("\n==== Resultados ====")
print("Total de famílias: {total_familias}")
print("Média do salário: {media_salario}")
print("Média do número de filhos: {media_filhos}")
print("Maior Salário: {maior_salario}")
print("Menor Salário: {menor_salario}")