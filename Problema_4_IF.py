varsta1=int(input("Dati varsta primei persoane: "))
varsta2=int(input("Dati varsta persoanei a doua: "))
varsta3=int(input("Dati varsta persoanei a treia: "))
if((varsta1>18)and(varsta1<60)and(varsta2>18)and(varsta2<60)and(varsta3>18)and(varsta3<60)):
    print(varsta1,"",varsta2,"",varsta3)
elif((varsta1>18)and(varsta1<60)and((varsta2>60)or(varsta2<18))and(varsta3>18)and(varsta3<60)):
    print(varsta1,"",varsta3)
elif((varsta1>18)and(varsta1<60)and(varsta2<60)and(varsta2>18)and((varsta3<18)or(varsta3>60))):
    print(varsta1,"",varsta2)
elif(((varsta1<18)or(varsta1>60))and(varsta2>18)and(varsta2<60)and(varsta3>18)and(varsta3<60)):
    print(varsta2,"",varsta3)
elif((varsta1>18)and(varsta1<60)and((varsta2<18)or(varsta2>60))and((varsta3<18)or(varsta3>60))):
    print(varsta1)
elif(((varsta1<18)or(varsta1>60))and(varsta2>18)and(varsta2<60)and((varsta3<18)or(varsta3>60))):
    print(varsta2)
else:
    print(varsta3)


