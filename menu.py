from os import system
from calculator import calc
import time
from history import history

def menu():
    print ("----------------------------------------------------------\n")
    print ("\tBem vindo a Calculadora Orientada a Objeto\n\n")
    opcao = input ("O que deseja fazer?\n1 - Operação\n2 - Historico de contas\n3 - Sair\t")

    print(opcao)

    if opcao == '1':
        calc()

    elif opcao == '2':
        history()

    elif opcao == '3':
        exit() 

    else :  
        print("Não entendi.\nPoderia repetir.\n")
        print ("----------------------------------------------------------\n")
        system("pause")
        system('clear')
        menu()