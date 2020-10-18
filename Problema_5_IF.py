#Presupun ca utilizatorul stie cate luni sunt si cate zile are fiecare luna
an_curent=int(input("Dati anul curent: "))
luna_curenta=int(input("Dati luna curenta: "))
zi_curenta=int(input("Dati ziua curenta: "))
an_nastere=int(input("Dati anul nasterii: "))
luna_nastere=int(input("Dati luna nasterii: "))
zi_nastere=int(input("Dati ziua nasterii: "))
if(((zi_curenta-zi_nastere)>=0)and((luna_curenta-luna_nastere)>=0)and((an_curent-an_nastere)>=0)):
    print(an_curent-an_nastere,"ani")
elif(((zi_curenta-zi_nastere)>=0)and((luna_curenta-luna_nastere)<0)and((an_curent-an_nastere)>0)):
    an_curent-=1
    print(an_curent-an_nastere,"ani")
elif(((zi_curenta-zi_nastere)<0)and(((luna_curenta-1)-luna_nastere)>=0)and((an_curent-an_nastere)>0)):
    print(an_curent-an_nastere,"ani")
elif(((zi_curenta-zi_nastere)<0)and(((luna_curenta-1)-luna_nastere)<0)and((an_curent-an_nastere)>0)):
    print((an_curent-1)-an_nastere,"ani")
else:
    print("Ati introdus datele gresit. Mai incercati")