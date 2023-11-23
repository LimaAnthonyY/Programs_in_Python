from os import system

hist = []
op_his = []
valor1 = []
valor2 = []

def history():
    i = int(len(hist))
    while (i != 0):
        if op_his[i-1] == '1':
            print("Resultado da soma de "+ str(valor1[i-1]) + " + " + str(valor2[i-1]) + " = " + str(hist[i-1]))
            i-=1
            print(hist)
            print(i)
            print(valor1[i-1])
            print(valor2[i-1])

        if op_his[i-1] == '2':
            print("Resultado da subtração = " + str(valor1[i-1]) + " - " + str(valor2[i-1]) + " = " + str(hist[i-1]))
            i-=1

        if op_his[i-1] == '3':
            print("Resultado da divisão = " + str(valor1[i-1]) + " / " + str(valor2[i-1]) + " = " + str(hist[i-1]))
            i-=1

        if op_his[i-1] == '4':
            print("Resultado da multiplicação = " + str(valor1[i-1]) + " * " + str(valor2[i-1]) + " = " + str(hist[i-1]))                      
            i-=1

    system("Pause")