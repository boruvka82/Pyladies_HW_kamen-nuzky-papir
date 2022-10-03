from random import randrange

while True:

    tah_pocitace = randrange(2)

    if tah_pocitace == 0:
        tah_pc_slovy = "kamen"
    elif tah_pocitace == 1:
        tah_pc_slovy = "nuzky"
    else:
        tah_pc_slovy = "papir"    
    #print(tah_pocitace, tah_pc_slovy)

    tah_cloveka = input("Zadej: kamen / nuzky / papir: ")
    if tah_cloveka == tah_pc_slovy:
        print("Je to plichta! Tah pocitace byl:", tah_pc_slovy)    
    elif (tah_pc_slovy == "kamen" and tah_cloveka == "nuzky") or (tah_pc_slovy == "nuzky" and tah_cloveka == "papir") or (tah_pc_slovy == "papir" and tah_cloveka == "kamen"):
        print("Pocitac vyhral :( Tah pocitace byl:", tah_pc_slovy)     
    elif (tah_pc_slovy == "nuzky" and tah_cloveka == "kamen") or (tah_pc_slovy == "papir" and tah_cloveka == "nuzky") or (tah_pc_slovy == "kamen" and tah_cloveka == "papir"):
        print("Vyhrala jsi :) Tah pocitace byl:", tah_pc_slovy)         
    elif tah_cloveka == "konec":
        print("KONEC")
        break
    else:
        print("spatne zadane, opakuj!")
