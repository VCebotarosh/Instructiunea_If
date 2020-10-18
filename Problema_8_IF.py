numar1=int(input("Dati primul numar: "))
numar2=int(input("Dati al doilea numar: "))
if(((numar1%2)==0)and((numar2%2)==0)):
    if(numar1>numar2):
        print("Cel mai mare numar par este",numar1)
    else:
        print("Cel mai mare numar par este",numar2)
elif(((numar1%2)!=0)and((numar2%2)!=0)):
    print("Printre aceste numere nu exista numere pare")
elif(((numar1%2)==0)and((numar2%2)!=0)):
    print("Cel mai mare numar par este",numar1)
else:
    print("Cel mai mare numar par este",numar2)