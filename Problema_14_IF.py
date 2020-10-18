locul=int(input("Dati numarul sosirii lui Ionel: "))
if((locul%4)==0):
    casuta=locul//4
else:
    casuta=(locul//4)+1
print("Ionel va nimeri in casuta cu numarul",casuta)