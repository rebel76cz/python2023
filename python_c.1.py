def vytvor_trojuhelnik(X):
    if X % 2 == 0:
        X += 1  
    for i in range(1, X+1, 2):
      
        row = ' '.join(map(str, range(1, i+1)))
       
        print(row.center(X*2 - 1))

X = int(input("Zadejte liché číslo X pro trojúhelník: "))

vytvor_trojuhelnik(X)
