from random import randrange

def tah_pc(herni_pole, symbol):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    
    while True: 
        cislo_policka = randrange(0,20)
        print("pc:",cislo_policka)
        if herni_pole[cislo_policka] != "-":
            print("jiz obsazene, PC pokracuje...")      
        else:    
            return tah(herni_pole, cislo_policka, symbol)

def tah(herni_pole, cislo_policka, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici"""
    return herni_pole[:cislo_policka] + symbol + herni_pole[cislo_policka + 1:]


symbol = "o"
herni_pole = ("--------------------")
tah_pc(herni_pole, symbol)
