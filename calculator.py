from os import system

num = []

def calc():
    op=input('Digite qual operação:\n1 - Adição\n2 - Subtração\n3 - Divisão\n4 - Multiplicação')
    
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

def number():
    print("Digite dois números para a operação:")
    num.append(float(input("Primeiro número: ")))
    num.append(float(input("Segundo número: ")))

def mat():
    resul = num[0] + num [1]
    print(resul)

def sub():
    resul = num[0] - num [1]
    print(resul)
    

def div():
    resul = num[0] / num [1]
    print(resul)
    

def mul():
    resul = num[0] * num [1]
    print(resul)
    