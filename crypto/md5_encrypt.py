import hashlib

for i in range(100000000):
    m = hashlib.sha1()
    m.update(str(i).encode("utf-8"))
    if m.hexdigest() == "a58dc2cfc5a93134666c607fbc5d6e961254214a":
        print(i)
