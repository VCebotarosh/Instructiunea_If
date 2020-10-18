latura1=int(input("Dati lungimea primei laturi: "))
latura2=int(input("Dati lungimea laturii a doua: "))
latura3=int(input("Dati lungimea laturii a treia: "))
if((latura1<32000)and(latura2<32000)and(latura3<32000)):
    if(((latura1+latura2)>latura3)and((latura2+latura3)>latura1)and((latura1+latura3)>latura2)):
        print("DA")
    else:
        print("NU")
else:
    print("Datele dumneavoastra nu satisfac conditia problemei")