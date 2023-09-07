X = int(input("Zadejte liché přirozené číslo X: "))


if X % 2 == 0:
    print("Zadejte liché číslo.")
else:

    for i in range(1, X + 1):
        row = ''.join(map(str, range(1, X - i + 2))) + ''.join(map(str, range(X - i, 0, -1)))
        print(row.center(X*2 - 1))

