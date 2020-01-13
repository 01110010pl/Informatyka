def potegowanie(x, y):
    if y >= 0:
        if y == 0: return 1
        else: return  potegowanie(x, y - 1)*x
    else:
        return 0
    
while True:
    x = 0
    y = 0
    while True:
        try:
            x = int(input("Podstawa: "))
            y = int(input("Wykładnik: "))
            break
        except:
            print("Błędne dane!")
    print("Wynik: ", potegowanie(x, y))
