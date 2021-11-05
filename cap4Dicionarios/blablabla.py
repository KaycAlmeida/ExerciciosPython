n = int(input("fala um numero: "))
fib1,fib2,fib3= 0,0,1

while fib3 < 5000:
    if (n == fib3):
        print("esse number ta na lista")
        break
    fib1=fib2
    fib2=fib3
    fib3=fib1 + fib2
if (n != fib3):
    print("esse number não tá")