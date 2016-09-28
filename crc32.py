#!/usr/bin/env python 
import os, sys
import zlib
import string
import random
import time

def crc(checkstr):
    
    prev = zlib.crc32(checkstr, 0)
    return format(prev & 0xFFFFFFFF, '08x')
    	
def randomString(size=32, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

hash_table = dict()
counter = 0
start = time.time()
while(1):
	string = randomString()
	crc_value = crc(string)
	if(hash_table.has_key(crc_value)):
		end = time.time()
		print counter, "different strings checked.\nThe CRC32 Value:", crc_value, "\n The two strings that returned the collision:", string, ", ", hash_table[crc_value]
		print "---- %s seconds ----" %(end - start)
		break
	else:
		hash_table.update({crc_value: string})
		counter += 1
		print "Strings searched:", counter