tabuada=int(input("Digite um numero para exibit a tabuada: "))
print ("tabuada do número ", tabuada)
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada+valor)))