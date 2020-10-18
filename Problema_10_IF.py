nr_gaini=int(input("Dati numarul de gaini la ferma: "))
boabe=int(input("Dati numarul de boabe care trebuie repartizate: "))
if((boabe%nr_gaini)!=0):
    curcan=boabe%nr_gaini
    boabe_1_gaina=boabe//nr_gaini
    if(curcan>boabe_1_gaina):
        print("Curcanul are cu",curcan-boabe_1_gaina,"boabe mai multe")
    elif(curcan<boabe_1_gaina):
        print("Gainile au cu",boabe_1_gaina-curcan,"boabe mai multe")
    else:
        print("Fiecare are primit cate",boabe_1_gaina,"boabe""\n""Egalitate")
else:
    print("Gainile au primit cu",boabe//nr_gaini,"boabe mai mult decat curcanul")