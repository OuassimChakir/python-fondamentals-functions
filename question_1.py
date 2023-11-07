def somme(n, m):
    somme = 0
    for x in range(n, m + 1):
        somme += x
        print(x)
    return somme


print("somme =", somme(5, 8))
