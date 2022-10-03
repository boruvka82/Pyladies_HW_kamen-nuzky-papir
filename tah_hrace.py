def tah_hrace(herni_pole):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici"""
    
    while True:
        cislo_policka = int(input("Na jakou pozici chces hrat? zadej 0-19: "))
        if cislo_policka >= 0 and cislo_policka <=19:
            if herni_pole[cislo_policka] != "-":
                print("jiz obsazene, pokracuj...")
            else:    
                herni_pole = tah(herni_pole, cislo_policka, symbol)
                return herni_pole
        else:
            print("spatne zadane, pokracuj...")
       
symbol = "x"
herni_pole = "x------------------o"
print(tah_hrace(herni_pole))
