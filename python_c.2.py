def cisla(X):
    for i in range(1, 2 * X):
        for j in range(1, 2 * X):
            value = X - max(abs(X - i), abs(X - j))
            print(value, end=" ")
        print()

X = int(input("Zadejte číslo: "))
if X % 2 == 0 or X <= 0:
    print("Zadejte liché kladné číslo.")
else:
    cisla(X)
