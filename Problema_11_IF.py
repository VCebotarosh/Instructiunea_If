numar1=int(input("Dati primul numar:"))
numar2=int(input("Dati al doilea numar:"))
numar3=int(input("Dati al treilea numar:"))
if(((numar1%2)==0)and((numar2%2)==0)and((numar3%2)==0)):
    print(numar1,"Par\n",numar2,"Par\n",numar3,"Par")
elif(((numar1%2)!=0)and((numar2%2)==0)and((numar3%2)==0)):
    print(numar1,"Impar\n",numar2,"Par\n",numar3,"Par")
elif(((numar1%2)!=0)and((numar2%2)!=0)and((numar3%2)==0)):
    print(numar1,"Impar\n",numar2,"Impar\n",numar3,"Par")
elif(((numar1%2)!=0)and((numar2%2)!=0)and((numar3%2)!=0)):
    print(numar1,"Impar\n",numar2,"Impar\n",numar3,"Impar")
elif(((numar1%2)==0)and((numar2%2)!=0)and((numar3%2)==0)):
    print(numar1,"Par\n",numar2,"Impar\n",numar3,"Par")
elif(((numar1%2)==0)and((numar2%2)==0)and((numar3%2)!=0)):
    print(numar1,"Par\n",numar2,"Par\n",numar3,"Impar")                                                                                     
elif(((numar1%2)!=0)and((numar2%2)==0)and((numar3%2)!=0)):
    print( numar1,"Impar\n",numar2,"Par\n",numar3,"Impar")
else:
    print(numar1,"Par\n",numar2,"Impar\n",numar3,"Impar")