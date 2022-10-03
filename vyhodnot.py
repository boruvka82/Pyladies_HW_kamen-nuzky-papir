def vyhodnot(herni_pole):
    """vrátí jednoznakový řetězec podle stavu hry:"""
    if "xxx" in herni_pole: 
        #Vyhrál hráč s křížky (pole obsahuje "xxx")
        return "x"
    elif "ooo" in herni_pole: 
        #Vyhrál hráč s kolečky (pole obsahuje "ooo")
        return "o"
    elif "-" not in herni_pole: 
        #Remíza (pole neobsahuje "-", a nikdo nevyhrál)
        return "!"
    else: 
        # Ani jedna ze situací výše (t.j. hra ještě neskončila)
        return "-"
       
print(vyhodnot("---x-o-x-o---xx--oo-"))
