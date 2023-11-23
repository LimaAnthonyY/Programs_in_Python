from os import system
from history import hist
from history import op_his
from history import valor1
from history import valor2


def calc():
    op=input('Digite qual operação:\n1 - Adição\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n:::')
    

    if op == '1':
        mat()
    elif op == '2':
        sub()
    elif op == '3':
        div()
    elif op == '4':
        mul()
    else:
        print("Não entendi.\nPoderia repetir.")
        system('pause')
        calc()
num1 = 0 
num2 = 0
def number():
    print("Digite dois números para a operação:")
    num1 = (float(input("Primeiro número: ")))
    num2 = (float(input("Segundo número: ")))

def mat():
    number()
    resul = num1 + num2
    print("A soma dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valor1.append(num1)
    valor2.append(num2)
    op_his.append("1")

def sub():
    number()
    resul = num1 - num2
    print("A subtração dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valor1.append(num1)
    valor2.append(num2)    
    op_his.append("2")

def div():
    number()
    resul = num1 / num2
    print("A divisão dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valor1.append(num1)
    valor2.append(num2)
    op_his.append("3")

def mul():
    number()
    resul = num1 * num2
    print("A multiplicação dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valor1.append(num1)
    valor2.append(num2)   
    op_his.append("4")