nota1=int(input("Dati prima nota primita de Andrei: "))
nota2=int(input("Dati a doua nota primita de Andrei: "))
nota3=int(input("Dati a treia nota primita de Andrei: "))
if(nota3>=8):
    print("Andrei a primit azi nota",nota1,"nota",nota2,"si nota",nota3)
elif(nota3<8):
    if(nota1>nota2):
        print("Andrei a primit azi doar nota",nota1)
    else:
        print("Andrei a primit azi doar nota",nota2)
    
