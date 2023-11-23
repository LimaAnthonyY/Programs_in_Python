from os import system


hist = []

def history():
    i = int(len(hist))
    while (i != 0):
        print("Resultado "+ str(i) + " = " + str(hist[i-1]))
        i-=1
    system("Pause")