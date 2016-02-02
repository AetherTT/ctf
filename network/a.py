inp = open("arch2.hex", "r")
out = open("arch.zip", "wb")

line = inp.readline()

def to_16(ch):
    if ch >= '0' and ch <= '9':
        return ord(ch) - ord('0')
    else:
        return ord(ch) - ord('a') + 10

def to_byte(ch1, ch2):
    v1 = to_16(ch1)
    v2 = to_16(ch2)
    return 16 * v1 + v2

for i in range(0, len(line), 2):
    ch1 = line[i]
    ch2 = line[i+1]
    out.write(bytes(chr(to_byte(ch1, ch2)), 'UTF-8'))

inp.close()
out.close()
