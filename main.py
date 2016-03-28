#
# =====================================================================================
#
#    Project Name:  Mini-Project 2
#
# Project Descrip:  This project is designed to brute force crack a password
#                        for a given ciphertext knowing the key length and
#                        first word length. It is using Vigenere Cipher to 
#                        decrypt the ciphertext.
#                             Vigenere Cipher Decryption: Ek(m) = m - K mod 26
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
import sys
import itertools
import time

# update_progress() : Displays or updates a console progress bar
## Accepts a float between 0 and 1. Any int will be converted to a float.
## A value under 0 represents a 'halt'.
## A value at 1 or bigger represents 100%
def update_progress(progress, time):
    barLength = 30 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    # if progress >= 1:
    #     progress = 1
    #     status = "Done...\r\n"
    block = int(round(barLength*progress))
    timestatus = str(int(time)) + " sec runtime"
    text = "\rPercent: [{0}] {1}% {2}  {3}".format( "#"*block + "-"*(barLength-block), "{0:.4f}".format(progress*100), status, timestatus)
    sys.stdout.write(text)
    sys.stdout.flush()

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


# Initialize dictionary lists (index by length)
wdict = []
for i in range(0,30):
	wdict.append([])

# Read in dictionary from file
f = file("dict.txt").read()
for word in f.split():
	wdict[len(word)].append(word)

print "Read In Dictionary"
print ""

totnumofkeys = 26**keySize
keyssofar = 1;

# Starts Timer
start_time = time.time()

# Generate every possible key of certain length
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
        plainNum.append((cipherNum[i] - keyNum[keycount]) % 26)
        keycount += 1
        if keycount == len(keyNum):
            keycount = 0

    # Convert all numbers to letters in plain text
    for a in plainNum:
        plainTxt += ndict[a]

    # Compares every word of certain length in dictionary with
    # first word of cipher text. If a match, print the plaintext
    # and key.
    for word in wdict[firstWordLength]:
        if plainTxt[0:firstWordLength] == word:
            print ""
            print "Key: " + ''.join(key)
            print "Plain Text: " + plainTxt
            print ""
            break
    update_progress(keyssofar/float(totnumofkeys), time.time() - start_time)	
    keyssofar += 1

print ""

# Print runtime of the program
print("Program took %s seconds" % (time.time() - start_time))
