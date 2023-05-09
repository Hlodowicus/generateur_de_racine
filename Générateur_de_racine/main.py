from random import *
from func import *

c = input("Consonne ? Écris toutes les consonnes sur une ligne. Sépare les consonnes par des espaces.\n")
v = input("Voyelle ? Écris toutes les voyelles sur une ligne. Sépare les consonnes par des espaces.\n")
ajouter_espace_consonne = input("Nombre d'espaces consonne ?\nAjout d'un espace dans la liste des consonnes ce qui rend la longueur du mot aléatoire.\nPlus le nombre est grand, plus la possibilité qu'une consonne soit remplacée par un espace est grand.\n")
ajouter_espace_voyelle = input("Nombre d'espaces voyelle ?\nAjout d'un espace dans la liste des voyelles ce qui rend la longueur du mot aléatoire.\nPlus le nombre est grand, plus la possibilité qu'une voyelle soit remplacée par un espace est grand.\n")
suf = input("Suffixe ? écris \"123\" si tu n'en veux pas.\n")
pref = input("Préfixe ? écris \"123\" si tu n'en veux pas.\n")
forme = input("Forme des racines à générer ?\n")
nombre = input("Combien de racines voulez vous ?\n")
nomJSON = input("Nom du fichier JSON ? Permet de consulter les noms générés plus simplement.\n")
x = 0

prefTab = pref.split()
sufTab = suf.split()
cTab = c.split()
vTab = v.split()
formeTab = list(forme)

ajouter_espace(cTab, ajouter_espace_consonne)
ajouter_espace(vTab, ajouter_espace_voyelle)

racine(cTab, vTab, formeTab, nombre, sufTab, prefTab, nomJSON)

print(sufTab)
print(prefTab)