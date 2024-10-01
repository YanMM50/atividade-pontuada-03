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

def coletando_dados():
    quantidade_filhos = []
    salario = []
    while True:
        cliente = Cliente(
            qnt_filhos = int(input("Quantos filhos você tem: "))
            salario = float(input("Seu salário: "))
        )
        quantidade_filhos.append()
    return lista_de_alunos, cliente

lista_atualizada_clientes, cliente = coletando_dados()
    