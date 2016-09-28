#!/usr/bin/env python 
import os, sys
import zlib
import string
import random
import time
import smtplib

def email_finish(time, str_value):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("kaiboma@gmail.com", "Kaiboma12!")
 
	msg = "Took:" + str(time) + " seconds. \n The String value that generated the same CRC value is:" + str_value
	server.sendmail("kaiboma@gmail.com", "kaiboma@gmail.com", msg)
	server.quit()

def email_start():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("kaiboma@gmail.com", "Kaiboma12!")
 
	msg = "Search began!"
	server.sendmail("kaiboma@gmail.com", "kaiboma@gmail.com", msg)
	server.quit()

def intToHexString32(num):
	return "{:032X}".format(num)

def crc(checkstr):
    
    temp = zlib.crc32(checkstr, 0)
    return format(temp & 0xFFFFFFFF, '08x')

std_number = '3FF8D07459EC440628F2811207257C9E'
std_crc = crc(std_number)
counter = 16203072428
email_start()
start = time.time()
while(1):
	string = intToHexString32(counter)
	crc_value = crc(string)
	if(std_crc == crc_value):
		end = time.time()
		print counter, "different strings checked.\nThe CRC32 Value:", crc_value, "\n The two strings that returned the collision:", string, ", ", std_number
		print "---- %s seconds ----" %(end - start)
		email_finish((end - start), string )
		break
	else:
		if(counter % 100000 == 0):
			print "Strings searched:", counter
		counter += 1