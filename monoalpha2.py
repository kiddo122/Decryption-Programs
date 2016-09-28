import string


with open('cyphertext.txt', 'r') as myfile:
    data=myfile.read()

    mystr = ""
    for letter in data:
    	if (letter == 'H'):
            mystr+=str('e')
        elif(letter == 'K'):
            mystr+=str('a')
        elif (letter == 'E'):
            mystr+=str(' t')
        elif (letter == 'G'):
            mystr+=str('o')

        elif (letter == 'Y'):
            mystr+=str('h')
        elif (letter == 'U'):
            mystr+=str('s')
        
        elif (letter == 'X'):
            mystr+=str('n')
        
        else:
            mystr += str(letter)

    print mystr