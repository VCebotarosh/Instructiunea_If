loc=int(input("Dati locul lui Radu in urma mediilor: "))
if(loc<=125):
    if((loc>=1)and(loc<=25)):
        print("Radu va nimeri in clasa A")
    elif((loc>25)and(loc<=50)):
        print("Radu va nimeri in clasa B")
    elif((loc>50)and(loc<=75)):
        print("Radu va nimeri in clasa C")
    elif((loc>75)and(loc<=100)):
        print("Radu va nimeri in clasa D")
    else:
        print("Radu va nimeri in clasa E")
else:
    print("Radu nu a nimerit nici intr-o clasa")
