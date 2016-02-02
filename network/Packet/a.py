inp = open("f.in", "r")
out = open("f.out", "w")

def to_int(s):
    b = 128
    res = 0
    print("\n", "s: ", s)
    for i in range(len(s)):
        print(s[i], end="")
        res += (ord(s[i]) - ord('0')) * b
        b //= 2
    print("\n")

    return res

for line in inp:
    for i in range(0, len(line) - 1, 8):
        x = to_int(line[i:i+8])
        print(i, len(line))
        out.write(str(chr(x)))

inp.close()
out.close()
