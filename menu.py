from os import system
from calculator import calc
import time
from history import history

def menu():
    print ("----------------------------------------------------------\n")
    print ("\tBem vindo a Calculadora Orientada a Objeto\n\n")
    opcao = input ("Deseja fazer uma operação?\n1- Sim\n2 -Não\t")
    if opcao == '2':
        opcao = input ("Deseja Verificar o historico?\n1- Sim\n2 -Não\t")

        if opcao == '1':
            calc()

        elif opcao == '2':
            history()

        else :  
            print("Não entendi.\nPoderia repetir.\n")
            print ("----------------------------------------------------------\n")
            exit()
    elif opcao == '1':
        calc()
    else :  
        print("Não entendi.\nPoderia repetir.\n")
        print ("----------------------------------------------------------\n")
        exit()