from collections import Counter
import string
import csv

def count_letters(data, letter):
    return data.count(letter)

with open('cyphertext.txt', 'r') as myfile:
    data=myfile.read()

    alpha = string.ascii_uppercase
    mystr = ""
    mylist = [None]
    totalletter = len(data)
    print data
    for letter in alpha:
    	mystr += str(100.0 * float(count_letters(data, letter))/totalletter)
    	mylist.append(str(100.0 * float(count_letters(data, letter))/totalletter))
    	print letter + ":" + str(count_letters(data, letter)) + "  (" + str(100.0 * float(count_letters(data, letter))/totalletter) + "%)"
    print mystr
    print totalletter

    with open('countresult3.csv','wb') as myfile:
    	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    	wr.writerow(mylist)