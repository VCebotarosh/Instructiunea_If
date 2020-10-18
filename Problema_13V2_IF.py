locul=int(input("Dati locul pe care s-a plasat Ionel: "))
if(locul<=100):
    if((locul%4)==0):
        print("Ionel va primi tricou de culoare neagra")
    elif((locul%4)==1):
        print("Ionel va primi tricou de culoare alba")
    elif((locul%4)==2):
        print("Ionel va primi tricou de culoare rosie")
    else:
        print("Ionel va primi tricou de culoare albastra")
else:
    print("Ionul nu s-a plasat in primii 100")