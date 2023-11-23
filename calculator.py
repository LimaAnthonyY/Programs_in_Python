from os import system
from history import hist
from history import op_his
from history import valores

num = []

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

def number():
    print("Digite dois números para a operação:")
    num.append(float(input("Primeiro número: ")))
    num.append(float(input("Segundo número: ")))

def mat():
    number()
    resul = num[0] + num [1]
    print("A soma dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valores.append(num[0])
    valores.append(num[1])
    op_his.append("1")

def sub():
    number()
    resul = num[0] - num [1]
    print("A subtração dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valores.append(num[0])
    valores.append(num[1])    
    op_his.append("2")

def div():
    number()
    resul = num[0] / num [1]
    print("A divisão dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valores.append(num[0])
    valores.append(num[1])
    op_his.append("3")

def mul():
    number()
    resul = num[0] * num [1]
    print("A multiplicação dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valores.append(num[0])
    valores.append(num[1])    
    op_his.append("4")