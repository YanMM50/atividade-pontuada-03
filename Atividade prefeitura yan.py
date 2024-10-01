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

def menu ():
    print("""
   === MENU ===

1. Adicionar família          
2. Exibir os resultados          
3. Sair             
          """)
    


def opcoes():
    menu()
    opcao = (input("Resposta: "))
    lista_total = []
    contador = 0
    while True:
        
        match opcao:
            case "1":
                cliente = Cliente(
            qnt_filhos = int(input("Quantos filhos você tem: ")),
            salarios = float(input("Seu salário: "))
        )
                lista_total.append(cliente)
                contador += 1
            case "2":
                print("\n==== Resultados ====")
                print(f"Total de famílias: {total_familias}")
                print(f"Média do salário: {media_salario}")
                print(f"Média do número de filhos: {media_filhos}")
                print(f"Maior Salário: {maior_salario}")
                print(f"Menor Salário: {menor_salario}")
                                
                
            case "3":
                break
                
            case _:
                print("Opção inválida")
                continue
            
        menu()
        opcao2 = input("Resposta: ")

        


    return lista_total, contador

        



lista_total, contador = opcoes()


def lendo_e_mostrando_arquivo():
    nome_arquivo_cliente = "pesquisa_prefeitura.txt"
    with open(nome_arquivo_cliente, "w") as lista_clientes:
        for cliente in lista_total:
            lista_clientes.write(f"{cliente.qnt_filhos}, {cliente.salarios}\n")
        
    with open(nome_arquivo_cliente, "r") as arquivo_clientes:
        for linha in arquivo_clientes:
            qnt_filhos, salarios = linha.strip() .split(",")
            lista_total.append(Cliente(qnt_filhos=int(qnt_filhos), salarios=float(salarios)))

        lista_clientes.close()
        
    return lista_clientes, arquivo_clientes


 



    