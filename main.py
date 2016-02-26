#
# =====================================================================================
#
#    Project Name:  Mini-Project 2
#
# Project Descrip:  
#                             Encryption: Ek(m) = m + K mod 26
#                             Decryption: Ek(m) = m - K mod 26
#
#        Filename:  main.py
#
#         Created:  02/25/2016
# 
#          Author:  Jake Suddock, Student KUID #: 2610736
#          School:  University of Kansas, School of Engineering
#          Course:  EECS 565, Professor: Bo Luo
#         
# =====================================================================================
#

from sys import argv
import itertools
import time

# Handles input arguments
script, cipherText, var1, var2 = argv

keySize = int(var1)
firstWordLength = int(var2)

# Letter To Number Lookup
ldict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
	    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
		'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
# Number To Letter Lookup
ndict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
		10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
		19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'};

wdict = []
# Initialize dictionary lists (index by length)
for i in range(0,30):
	wdict.append([])

# Read in dictionary
f = file("dict.txt").read()
for word in f.split():
	wdict[len(word)].append(word)

print "Read In Dictionary"

# Generate every possible key of certain length
# possibleKeys = [''.join(i) for i in itertools.product("ABCDEFGHIJKLMNOPQRSTUVWXYZ",repeat=keySize)]

print ""

# Starts Timer
start_time = time.time()

for key in itertools.product("ABCDEFGHIJKLMNOPQRSTUVWXYZ",repeat=keySize):
	cipherNum = []
	keyNum = []
	plainNum = []
	plainTxt = ""

	# Convert all letters to numbers in cipher and key
	for a in cipherText:
		cipherNum.append(ldict[a])
	for a in key:
		keyNum.append(ldict[a])

	keycount = 0 # initialize key counter

	# Vigenere cipher decryption (Ek(m) = m - k mod 26)
	for i in range(len(cipherNum)):
		plainNum.append((cipherNum[i] - keyNum[keycount]) % 26);
		keycount += 1
		if keycount == len(keyNum):
			keycount = 0

	# Convert all numbers to letters in plain text
	for a in plainNum:
		plainTxt += ndict[a]

	for word in wdict[firstWordLength]:
		if plainTxt[0:firstWordLength] == word:
			print "Key: " + ''.join(key)
			print "Plain Text: " + plainTxt
			print ""
			break

print ""

print("Program took %s seconds" % (time.time() - start_time))