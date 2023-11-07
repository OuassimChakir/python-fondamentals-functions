import math


def delta(a, b, c):
    return (b ** 2) - (4 * a * c)


def NombreRacine(delta):
    if delta > 0:
        return 2
    elif delta < 0:
        return 0
    else:
        return 1


def AfficheNombreRacine(delta):
    print("le Nombre des Racines: {}".format(NombreRacine(delta)))


def Racine1(delta, a, b):
    return (-b - math.sqrt(delta)) / (2 * a)


def Racine2(delta, a, b):
    return (-b + math.sqrt(delta)) / (2 * a)


def Racine0(a, b):
    return (-b) / (2 * a)


a = float(input("Donner a = "))
b = float(input("Donner b = "))
c = float(input("Donner c = "))

delta = delta(a,b,c)
if NombreRacine(delta) == 2:
    print("X1 =",Racine1(delta,a,b))
    print("X2 =",Racine2(delta,a,b))
elif NombreRacine(delta) == 1:
    print("X =", Racine0(a, b))
else:
    print("C'est equation n'a aucune solution")