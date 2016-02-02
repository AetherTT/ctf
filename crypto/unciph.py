d = {}
d['u'] = 'e'
d['v'] = 't'
d['t'] = 'a'
d['b'] = 'i'
d['x'] = 'o'
d['f'] = 'n'
d['p'] = 'r'
d['k'] = 'h'
d['s'] = 's'
d['w'] = 'l'
d['q'] = 'd'
d['l'] = 'u'
d['e'] = 'c'
d['z'] = 'w'
d['n'] = 'm'
d['c'] = 'g'
d['d'] = 'y'
d['i'] = 'f'
d['h'] = 'b'
d['a'] = 'v'
d['o'] = 'k'
d['j'] = 'p'
d['g'] = 'z'
d['y'] = 'q'
d['m'] = 'j'
d['r'] = 'x'
d[' '] = ' '
d['\n'] = '\n'

inp = open("ciphertext", "r")
out = open("ciphertext_dec", "w")

for line in inp:
    for i in line:
        out.write(d[i])
    out.write("\n")

inp.close()
out.close()
