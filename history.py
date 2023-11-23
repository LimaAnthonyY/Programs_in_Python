from os import system

hist = []
op_his = []
valores = []

def history():
    i = int(len(hist))
    while (i != 0):
        print (op_his)
        if op_his[i-1] == '1':
            print("Resultado da soma de "+ str(valores[i-1]) + str(valores[i-1]) + " = " + str(hist[i-1]))
        
        if op_his[i-1] == '2':
            print("Resultado da subtração = " + str(valores[i-1]) + str(valores[i-1]) + " = " + str(hist[i-1]))
        
        if op_his[i-1] == '3':
            print("Resultado da divisão = " + str(valores[i-1]) + str(valores[i-1]) + " = " + str(hist[i-1]))
        
        if op_his[i-1] == '4':
            print("Resultado da multiplicação = " + str(valores[i-1]) + str(valores[i-1]) + " = " + str(hist[i-1]))                      
        i-=1
    system("Pause")