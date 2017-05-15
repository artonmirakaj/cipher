
key = {
       'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s',
       'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y',
       'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e',
       's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m',

       'A':'N', 'B':'O', 'C':'P', 'D':'Q','E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y',
       'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
       'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K',
       'Y':'L', 'Z':'M'
}

count = 0

sentence = list(raw_input('encode: '))

for item in sentence:
    if item not in key:
        sentence[count] = item
        count = count + 1

    elif item in key:
        item = key.keys()[key.values().index(item)]
        sentence[count] = item
        count = count + 1

print ''.join(sentence)


count = 0

decoder = list(raw_input('decode: ' ))

for item in decoder:
    if item not in key:
        decoder[count] = item
        count = count + 1

    if item in key:
        item = key[item]
        decoder[count] = item
        count = count + 1

print ''.join(decoder)