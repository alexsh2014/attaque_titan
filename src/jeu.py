# from random import randint
# mystere = randint(0, 1024)
# nb = int(input("devinez! (le nombre est compris entre 0 et 1024): "))
# print(mystere)
# nbCoupsGagne = 0
# for i in range(1, 10):
#     if nb == mystere:
#         nbCoupsGagne = i
#         break
#     elif nb > 1024:
#         print("valeur trop grande")
#         nb = int(input("recommencez avec un nombre plus petit: "))
#     elif nb < 0:
#         print("valeur trop petite")
#         nb = int(input("recommencez avec un nombre positif: "))
#     elif nb < mystere:
#         print("valeur mystere est plus grande ")
#         nb = int(input("un autre nombre: "))
#     elif nb > mystere:
#         print("valeur mystere est plus petite")
#         nb = int(input("un autre nombre: "))


# if(nbCoupsGagne == 0):
#     print("grosse burne tu n'a pas trouve le nombre mystere :", mystere)
# else:
#     print("bien joué, vous avez trouvé en", nbCoupsGagne, "essais")


# initialisation des donnees
# gagne = False
# nbEssai = int(1)

# tant que je n'ai pas gagne ou  que le nb essais est <=10
# je demande le nb a utilisateur
# je compare sa réponse avec le nb mystere
# si le nb mystere est trouve, alors je passe gagne a true
# inon j'incrimente le nb essai

# while((not gagne) and (nbEssai <= 10)):
#     nb = int(input("devinez! (le nombre est compris entre 0 et 1024): "))
#     print(nb, mystere, nbEssai)
#     if(nb == mystere):
#         gagne = True
#     else:
#         nbEssai = nbEssai+1

# if(gagne):
#     print("bravo vous avez trouve le nombre",
#           mystere, " en ", nbEssai, " essai(s)")
# else:
#     print("grosse burne, il fallait trouver le nombre ", mystere)


u = 5
for k in range(1, 7):
    u = u+k
print(k)


a = 12
b = 5
b = a*b
a = 3*a
print(a, b)
