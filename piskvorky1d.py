from random import randrange
def tah(herni_pole, cislo_policka, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici"""
    return herni_pole[:cislo_policka] + symbol + herni_pole[cislo_policka + 1:]
    

def tah_hrace(herni_pole):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici"""
    #otazka na hrace x na pozici
    symbol = "x"
    while True:
        cislo_policka = int(input("Na jakou pozici chces hrat? zadej 0-19: "))
        if cislo_policka >= 0 and cislo_policka <=19:
            if herni_pole[cislo_policka] != "-":
                print("jiz obsazene, pokracuj...")
            else:    
                return tah(herni_pole, cislo_policka, symbol)
        else:
            print("spatne zadane, pokracuj...")


def tah_pc(herni_pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    symbol = "o"
    while True: 
        cislo_policka = randrange(0,20)
        print("pc:",cislo_policka)
        if herni_pole[cislo_policka] != "-":
            print("jiz obsazene, PC pokracuje...")      
        else:    
            return tah(herni_pole, cislo_policka, symbol)


def vyhodnot(herni_pole):
    """vrátí jednoznakový řetězec podle stavu hry:"""
    if "xxx" in herni_pole: 
        return "x"
    elif "ooo" in herni_pole: 
        return "o"
    elif "-" not in herni_pole: 
        return "!"
    else: 
        return "-"
       

def piskvorky1d():
    """vytvoří řetězec s herním polem a střídavě volá funkce tah_hrace a tah_pocitace, dokud někdo nevyhraje nebo nedojde k remíze"""
    herni_pole = ("--------------------")
    kolo = 0
    while True:
        kolo += 1    
        herni_pole = tah_hrace(herni_pole)
        print(kolo,".kolo:", herni_pole)  
        vysledek = vyhodnot(herni_pole)
        if vysledek != "-":
            if vysledek == "x":
                print("Vyhrál hráč s křížky (pole obsahuje 'xxx')")
            else:
                print("Remíza (pole neobsahuje '-', a nikdo nevyhrál)")
            break

        kolo += 1     
        herni_pole = tah_pc(herni_pole)
        print(kolo,".kolo:", herni_pole) 
        vysledek = vyhodnot(herni_pole)   
        if vysledek != "-":
            if vysledek == "o":
                print("Vyhrál hráč s kolečky (pole obsahuje 'ooo')")
            else:
                print("Remíza (pole neobsahuje '-', a nikdo nevyhrál)")
            break
                
piskvorky1d()

