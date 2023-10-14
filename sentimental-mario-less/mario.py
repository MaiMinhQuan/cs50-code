try:
    n = int(input("Height: "))
    if n <= 0 or n > 8:
        sys.exit()
except:
    sys.exit()
for i in range(n):
    print(" " * (n - 1 - i), end = "")
    print("#"* (i + 1))
