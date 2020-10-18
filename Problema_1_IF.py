nr1=int(input("Dati numarul curent de elev: "))
punctaj1=int(input("Dati punctajul elevului respectiv: "))
nr2=int(input("Dati numarul curent de elev: "))
punctaj2=int(input("Dati punctajul elevului respectiv: "))
nr3=int(input("Dati numarul curent de elev: "))
punctaj3=int(input("Dati puctajul elevului respectiv: "))
if((punctaj1>punctaj2)and(punctaj1>punctaj3)):
    print("Punctajul maxim are elevul cu numarul",nr1)
elif((punctaj2>punctaj1)and(punctaj2>punctaj3)):
    print("Punctajul maxim are elevul cu numarul",nr2)
elif((punctaj3>punctaj1)and(punctaj3>punctaj2)):
    print("Punctajul maxim are elevul cu numarul",nr3)
elif((punctaj1==punctaj2)and(punctaj1>punctaj3)):
    print("Punctajul maxim il au elevii",nr1,"si",nr2)
elif((punctaj1==punctaj3)and(punctaj1>punctaj3)):
    print("Punctajul maxim il au elevii",nr1,"si",nr3)
elif((punctaj2==punctaj3)and(punctaj2>punctaj1)):
    print("Punctajul maxim il au elevii",nr2,"si",nr3)
else:
    print("Toti elevii au punctaj maximal")