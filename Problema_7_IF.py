numar1=int(input("Dati primul numar: "))
numar2=int(input("Dati al doilea numar: "))
numar3=int(input("Dati al treilea  numar: "))
if((numar1>0)and(numar2>0)and(numar3>0)):
    if(numar2>numar3):
        print(numar2)
    else:
        print(numar3)
else:
    print(numar1+numar2)
