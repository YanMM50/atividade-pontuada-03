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
    quantidade_de_filhos = int
    salario = float

mport os
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Cliente:
    quantidade_de_filhos = int
    salario = float

def coletando_dados():
    quantidade_filhos = []
    salario = []
    while True:
        cliente = Cliente(
            qnt_filhos = int(input("Quantos filhos você tem: "))
            salario = float(input("Seu salário: "))
        )
        quantidade_filhos.append()
    return quantidade_filhos, salario

lista_atualizada_clientes, cliente = coletando_dados()
        

def menu ():
    print("""
    MENU

1. Adicionar família          
2. Exibir os resultados          
3. Sair             
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
                resultado = "Opção inválida"
                return n1,resultado



#  Definindo o nome do arquivo


    print("\n=== Acessando dados de um arquivo ===")
with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        nome, idade = linha.strip().split(",")
        lista_de_alunos.append(Aluno(nome=nome, idade= int(idade)))