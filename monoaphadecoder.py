from collections import Counter
import string


with open('cyphertext.txt', 'r') as myfile:
    data=myfile.read()

    mystr = ""
    for letter in data:
    	if (letter == 'H'):
            mystr+=str('E')
        elif (letter == 'K'):
            mystr+=str('O')
        elif (letter == 'E'):
            mystr+=str('N')
        elif (letter == 'G'):
            mystr+=str('A')
        elif (letter == 'M'):
            mystr+=str('T')
        elif (letter == 'L'):
            mystr+=str('H')
        elif (letter == 'S'):
            mystr+=str('I')
        elif (letter == 'J'):
            mystr+=str('M')
        elif (letter == 'W'):
            mystr+=str('R')
        elif (letter == 'Y'):
            mystr+=str('C')
        elif (letter == 'U'):
            mystr+=str('D')
        elif (letter == 'Q'):
            mystr+=str('S')
        elif (letter == 'X'):
            mystr+=str('L')
        elif (letter == 'V'):
            mystr+=str('F')
        elif (letter == 'A'):
            mystr+=str('G')
        elif (letter == 'N'):
            mystr+=str('P')
        elif (letter == 'T'):
            mystr+=str('U')
        elif (letter == 'C'):
            mystr+=str('W')
        elif (letter == 'O'):
            mystr+=str('B')
        elif (letter == 'R'):
            mystr+=str('Y')
        elif (letter == 'I'):
            mystr+=str('V')
        elif (letter == 'B'):
            mystr+=str('K')
        elif (letter == 'P'):
            mystr+=str('J')]
        else:
            mystr += str(letter)

    print mystr