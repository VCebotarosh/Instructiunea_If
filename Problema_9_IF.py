bile_albe_mari=int(input("Dati numarul de bile albe mari: "))
bile_albe_mici=int(input("Dati numarul de bile albe mici: "))
bile_rosii_mari=int(input("Dati numarul de bile rosii mari: "))
bile_rosii_mici=int(input("Dati numarul de bile rosii mici: "))
bile_verzi_mari=int(input("Dati numarul de bile verzi mari: "))
bile_verzi_mici=int(input("Dati numarul de bile verzi mici: "))
total=bile_albe_mari+bile_albe_mici+bile_rosii_mari+bile_rosii_mici+bile_verzi_mari+bile_verzi_mici
print("In total sunt",total,"bile")
bile_mari=bile_albe_mari+bile_rosii_mari+bile_verzi_mari
bile_mici=bile_albe_mici+bile_rosii_mici+bile_verzi_mici
bile_albe=bile_albe_mari+bile_albe_mici
bile_rosii=bile_rosii_mari+bile_rosii_mici
bile_verzi=bile_verzi_mari+bile_verzi_mici
if(bile_mari>bile_mici):
    print("Mari",bile_mari)
else:
    print("Mici",bile_mici)
if((bile_albe>bile_rosii)and(bile_albe>bile_verzi)):
    print("Bile albe",bile_albe)
elif((bile_rosii>bile_albe)and(bile_rosii>bile_verzi)):
    print("Bile rosii",bile_rosii)
elif((bile_verzi>bile_albe)and(bile_verzi>bile_rosii)):
    print("Bile verzi",bile_verzi)
elif((bile_verzi==bile_albe)and(bile_verzi>bile_rosii)):
    print("Bile verzi sunt tot atatea cat si cele albe",bile_verzi)
elif((bile_rosii==bile_albe)and(bile_rosii>bile_verzi)):
    print("Bile rosii sunt tot atatea cat si cele albe",bile_rosii)
elif((bile_verzi==bile_rosii)and(bile_verzi>bile_albe)):
    print("Bile verzi sunt tot atatea cat si cele rosii",bile_verzi)
else:
    print("Sunt acelasi numar de bile",bile_albe)


