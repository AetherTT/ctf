s = input()
for i in range(26):
    for j in s:
        if j == " ":
            print(" ", end="")
        else:
            print(chr(ord('a') + (ord(j) - ord('a') + i) % 26), end="")
    print("\n", end="\n")
