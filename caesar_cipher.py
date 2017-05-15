
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


isValid = False
count = 0

while not isValid:

    choice = raw_input("E: encode / D: decode: ").upper()

    if choice == "E":

        isValid = True
        message = list(raw_input("encode: "))

        for item in message:
            if item not in key:
                message[count] = item
                count = count + 1

            elif item in key:
                item = key.keys()[key.values().index(item)]
                message[count] = item
                count = count + 1

        print "".join(message)

    elif choice == "D":

        isValid = True
        cipher = list(raw_input("decode: "))

        for item in cipher:
            if item not in key:
                cipher[count] = item
                count = count + 1

            if item in key:
                item = key[item]
                cipher[count] = item
                count = count + 1

        print "".join(cipher)

    else:
        print "try again"