tah_pocitace = "kamen"

while True:
    tah_cloveka = input("Zadej: kamen / nuzky / papir: ")
    if tah_cloveka == tah_pocitace:
        print("Je to plichta! Tah pocitace byl:", tah_pocitace)    
    elif (tah_pocitace == "kamen" and tah_cloveka == "nuzky") or (tah_pocitace == "nuzky" and tah_cloveka == "papir") or (tah_pocitace == "papir" and tah_cloveka == "kamen"):
        print("Pocitac vyhral :( Tah pocitace byl:", tah_pocitace)     
    elif (tah_pocitace == "nuzky" and tah_cloveka == "kamen") or (tah_pocitace == "papir" and tah_cloveka == "nuzky") or (tah_pocitace == "kamen" and tah_cloveka == "papir"):
        print("Vyhrala jsi :) Tah pocitace byl:", tah_pocitace)         
    elif tah_cloveka == "konec":
        print("KONEC")
        break
    else:
        print("spatne zadane, opakuj!")
