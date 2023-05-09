from random import *
import json

def racine(consonne, voyelle, forme, nombre, sufTab, prefTab, nomJSON):
    x = 0
    y = 0
    res = {}
    mot = ""
    loCon = len(consonne) - 1
    loVoy = len(voyelle) - 1
    loSuf = len(sufTab) - 1
    loPref = len(prefTab) - 1
    
    while x <= int(nombre):
        while y < len(forme):
            if forme[y] == "c":
                n = randint(0, loCon)
                mot += consonne[n]
            elif forme[y] == "v":
                n = randint(0, loVoy)
                mot += voyelle[n]
            y+=1

        #Suffixes
        if sufTab[0] == "123":
            pass
        else:
            n = randint(0, loSuf)
            mot += sufTab[n]
        
        #Préfixes
        if prefTab[0] == "123":
            pass
        else:
            n = randint(0, loPref)
            mot = prefTab[n] + mot

        mot = mot.replace(" ", "")
        res[f"R{x}"] = mot
        mot = ""
        y = 0
        print(f"                                                     Mot === {x}")
        x += 1

    print(res)

    with open(f"{nomJSON}.json", "w") as f:
        json.dump(res, f, indent = 4)

def ajouter_espace(tab, nbEspace):
    x = 0
    while x < int(nbEspace):
        tab.append(" ")
        x += 1