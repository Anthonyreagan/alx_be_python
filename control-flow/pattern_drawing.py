size = int(input("Enter the size of the pattern: "))
row = 0


while row < size:
    for i in range(size):
        asterics = i * '*'
        print(f"{asterics}", end="")
    print()
    row += 1


