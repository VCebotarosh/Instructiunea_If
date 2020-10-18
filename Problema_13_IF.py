locul=int(input("Dati locul pe care s-a plasat Ionel: "))
if((locul>=1)and(locul<=25)):
    print("Ionel va primi tricou de culoare alba")
elif((locul>25)and(locul<=50)):
    print("Ionel va primi tricou de culoare rosie")
elif((locul>50)and(locul<=75)):
    print("Ionel va primi tricou de culoare albastra")
elif((locul>75)and(locul<=100)):
    print("Ionel va primi tricou de coloare neagra")
else:
    print("Ionel nu va primi tricou")