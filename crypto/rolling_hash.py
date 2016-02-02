x = 1317748575983887541099
s = ""

while x != 0:
    s = s + str(x % 2)
    x //= 2

for i in range(8):
    x += 256 ** i

s1 = ""
for i in range(len(s)):
    if i % 8 == 0:
        print(s1[::-1])
        s1 = ""
    s1 += s[i]
print(s1[::-1])

s = ""

while x != 0:
    s = s + str(x % 2)
    x //= 2

print(s[::-1])
