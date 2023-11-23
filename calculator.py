from os import system
from history import hist
from history import op_his
from history import valor1
from history import valor2

num=[0,0]
def number():
    print("Digite dois números para a operação:")
    num[0]=(float(input("Primeiro número: ")))
    num[1]=(float(input("Segundo número: ")))

def calc():
    op=input('Digite qual operação:\n1 - Adição\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n:::')
    
    number()

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



def mat():
    resul = num[0] + num[1]
    print("A soma dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valor1.append(num[0])
    valor2.append(num[1])
    op_his.append("1")


def sub():
    resul = num[0] - num[1]
    print("A subtração dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valor1.append(num[0])
    valor2.append(num[1])
    op_his.append("2")

def div():
    resul = num[0] / num[1]
    print("A divisão dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valor1.append(num[0])
    valor2.append(num[1])
    op_his.append("3")

def mul():
    resul = num[0] * num[1]
    print("A multiplicação dos númerou deu: " + str(resul))
    print("\n\nSalvando resultado........\n\n")
    system("pause")
    hist.append(resul)
    valor1.append(num[0])
    valor2.append(num[1])
    op_his.append("4")