#cislo_policka(0,19)
#symbol "x" or "o"
def tah(herni_pole, cislo_policka, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici"""
    return herni_pole[:cislo_policka] + symbol + herni_pole[cislo_policka + 1:]
print(tah("-----------------", 19, "x"))
