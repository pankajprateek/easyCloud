# AES algorithm in python
# Author: Pankaj Jindal
# Last Modified: Nov 4, 2011 at 1:50am
# Encryption done
# Decryption done
# Working :D

import math
from server import *
from md5 import *

base = 5
prime = 23
dhKey = False
key = [0]*16
inVect = [0]*16

rcon = [
0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 
0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 
0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 
0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 
0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 
0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 
0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 
0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 
0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 
0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 
0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 
0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 
0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 
0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 
0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 
0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d]

sbox =  [
0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16 ]

sboxInv = [ 
0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d ]
		
def scheduleCore(t1, iteration):
		c = t1[0]
		for i in range(0, 3):			# rotate the 32-bit word 8 bits to the left
			t1[i] = t1[i+1]
		t1[3] = c
		for i in range(0, 4):			# apply S-Box substitution on all 4 parts of the 32-bit word
			t1[i] = sbox[t1[i]]
		t1[0] = t1[0]^rcon[iteration]		# XOR the output of the rcon operation with i to the first part (leftmost) only
		return t1
	
def keyExpansion(key, expandedKeySize):
	size = len(key)
	expandedKey = [0]*expandedKeySize
	for i in range(size):
		expandedKey[i] = key[i]
	mySize = size
	rconIter = 1
	t = [0, 0, 0, 0]		#We create a 4-byte temporary variable, t
	while(mySize<expandedKeySize):
		for i in range(0, 4):			#We assign the value of the previous four bytes in the expanded key to t
			t[i] = expandedKey[mySize-4+i]
		if(mySize%size==0):
			t = scheduleCore(t, rconIter)		#We perform the key schedule core (see above) on t, with i as the rcon iteration value
			rconIter +=1					#We increment i by 1
		elif(size>6 and mySize%size==4):
			for l in range(0, 4): 
				t[l] = sbox[t[l]]
		for i in range(0, 4):			#We exclusive-or t with the four-byte block n bytes before the new expanded key. This becomes the next 4 bytes in the expanded key
			expandedKey[mySize] = expandedKey[mySize - size] ^ t[i]
		mySize += 4
	return expandedKey
	
# XOR the round keys to the state
def addRoundKey(state, roundKey):
	for i in range(16):
		state[i] = state[i]^roundKey[i]
	return state
	
# Creates a round key from the given expanded key and the position within the expanded key.
def createRoundKey(expandedKey, keyPointer):
	roundKey = [0]*16
	for i in range(0, 4):
		for j in range(0, 4):
			roundKey[j*4+i] = expandedKey[keyPointer + i*4 + j]
	return roundKey
		
def galois_mult(a, b):
	p = 0
	for counter in range(0, 8):
		if (b & 1) == 1: p ^= a
		if p > 0x100: p ^= 0x100
		# keep p 8 bit
		hi_bit_set = (a & 0x80)
		a <<= 1
		if a > 0x100:
			# keep a 8 bit
			a ^= 0x100
		if hi_bit_set == 0x80:
			a ^= 0x1b
		if a > 0x100:
			# keep a 8 bit
			a ^= 0x100
		b >>= 1
		if b > 0x100:
			# keep b 8 bit
			b ^= 0x100
	return p
	
def subBytes(state):
	#print state[0]
	for i in range(0, 16):
		state[i] = sbox[state[i]]
	return state
	
def shiftRows(state):
	for i in range(0, 4):
		state = shiftRow(state, i)
	return state
	
def shiftRow(state, shifts):
	pos = 4*shifts
	for i in range(0, shifts):
		c = state[pos]
		for j in range(0, 3):
			state[pos+j] = state[pos+j+1]
		state[pos+3] = c
	return state
	
def mixColumns(state):
	column = [0]*4
	for i in range(0, 4):
		for j in range(0, 4): 			# construct columns one by one
			column[j] = state[(j*4)+i]
		column = mixColumn(column)			# send it to multipy according to galios fields
		for k in range(0, 4): 
			state[(k*4)+i] = column[k]
	return state;
	
# matrix to be multiplied with
# [2, 3, 1, 1] 
# [1, 2, 3, 1]
# [1, 1, 2, 3]
# [3, 1, 1, 2]
# multiplication by 1 means leaving unchanged
# multiplication by 2 means shifting byte to the left
# multplication by 3 means shifting to the left and then performing xor with the initial unshifted value.
# After shifting, a conditional xor with 0x11B should be performed if the shifted value is larger than 0xFF.
def mixColumn(column):
	mult = [1,1,2,3]
	temp = [0,0,0,0]
	for i in range(0, 4): 
		temp[i] = column[i]
	column[0] = galois_mult(temp[0],mult[2]) ^ galois_mult(temp[1],mult[3]) ^ galois_mult(temp[2],mult[0]) ^ galois_mult(temp[3],mult[1])
	column[1] = galois_mult(temp[0],mult[0]) ^ galois_mult(temp[1],mult[2]) ^ galois_mult(temp[2],mult[3]) ^ galois_mult(temp[3],mult[1])
	column[2] = galois_mult(temp[0],mult[0]) ^ galois_mult(temp[1],mult[1]) ^ galois_mult(temp[2],mult[2]) ^ galois_mult(temp[3],mult[3])
	column[3] = galois_mult(temp[0],mult[3]) ^ galois_mult(temp[1],mult[0]) ^ galois_mult(temp[2],mult[0]) ^ galois_mult(temp[3],mult[2])
	return column
	
def subBytesInv(state):
	for i in range(0, 16):
		state[i] = sboxInv[state[i]]
	return state

def shiftRowInv(state, shifts):
	#print "shiftRowinv"
	#print state
	pos = 4*shifts
	for i in range(0, shifts):
		c = state[pos + 3]
		j = 3
		while j > 0:
			state[pos + j] = state[pos + j-1]
			j -= 1
		state[pos] = c
	return state
	
def shiftRowsInv(state):
	#print "shiftrows"
	#print state
	for i in range(0, 4):
		state = shiftRowInv(state, i)
	return state
		
def mixColumnInv(column):
	mult = [9,11,13,14]
	temp = [0,0,0,0]
	for i in range(0, 4): 
		temp[i] = column[i]	
	column[0] = galois_mult(temp[0],mult[3]) ^ galois_mult(temp[1],mult[1]) ^ galois_mult(temp[2],mult[2]) ^ galois_mult(temp[3],mult[0])
	column[1] = galois_mult(temp[0],mult[0]) ^ galois_mult(temp[1],mult[3]) ^ galois_mult(temp[2],mult[1]) ^ galois_mult(temp[3],mult[2])
	column[2] = galois_mult(temp[0],mult[2]) ^ galois_mult(temp[1],mult[0]) ^ galois_mult(temp[2],mult[3]) ^ galois_mult(temp[3],mult[1])
	column[3] = galois_mult(temp[0],mult[1]) ^ galois_mult(temp[1],mult[2]) ^ galois_mult(temp[2],mult[0]) ^ galois_mult(temp[3],mult[3])
	return column

def mixColumnsInv(state):
	column = [0]*4
	for i in range(0, 4):
		for j in range(0, 4): 			# construct columns one by one
			column[j] = state[(j*4)+i]
		column = mixColumnInv(column)			# send it to multipy according to galios fields
		for k in range(0, 4): 
			state[(k*4)+i] = column[k]
	return state

def aes_round(state, roundKey):
	#print state
	state = subBytes(state)
	#print state
	state = shiftRows(state)
	#print state
	state = mixColumns(state)
	#print state
	state = addRoundKey(state, roundKey)
	return state
		
def aes_roundInv(state, roundKey):
	#print "aes_rdinv"
	#print state
	state = shiftRowsInv(state)
	state = subBytesInv(state)
	state = addRoundKey(state, roundKey)
	state = mixColumnsInv(state)
	return state
	
def aes_fn(state, expandedKey, nbrRounds):
	state = addRoundKey(state, createRoundKey(expandedKey, 0))		# each byte of the state is combined with the round key using bitwise xor
	i = 1
	while i < nbrRounds:
		state = aes_round(state, createRoundKey(expandedKey, 16*i))	# rounds step
		i += 1
	# final round
	state = subBytes(state)
	state = shiftRows(state)
	state = addRoundKey(state, createRoundKey(expandedKey,16*nbrRounds))
	return state
	
	
def aes_fnInv(state, expandedKey, nbrRounds):
	#print "NBR_state"
	#print nbrRounds
	#print state
	state = addRoundKey(state, createRoundKey(expandedKey, 16*nbrRounds))
	#print state
	i = nbrRounds - 1
	while i > 0:
		state = aes_roundInv(state, createRoundKey(expandedKey, 16*i))
		#print i
		#print state
		i -= 1
	state = shiftRowsInv(state)
	state = subBytesInv(state)
	state = addRoundKey(state, createRoundKey(expandedKey, 0))
	return state


def str2arr(string,start,end):
	ar = [0]*16
	i = start
	j = 0
	while i < end:			# takes care of padding in case of text
		ar[j] = ord(string[i])
		j += 1
		i += 1
	return ar

def arr2arr(string,start,end):
	ar = [0]*16
	i = start
	j = 0
	while i < end:			# takes care of padding in case of text
		ar[j] = int(string[i])
		j += 1
		i += 1
	return ar

def arr2str(arr):
	strTemp = ''
	for a in range(0, len(arr)):
		strTemp +=chr(arr[a])
	return strTemp

def encrypt(inp, keyin):
	inputs = []
	if(len(inp)>16):
		for a in range(0, 16):
			inputs.append(int(inp[a]))
	else:
		for a in range(0, len(inp)):
			inputs.append(int(inp[a]))
		while len(inputs) < 16:
			inputs.append(0)
	
	#inputs = [103,35,148,239,76,213,47,118,255,222,123,176,106,134,98,92]
	#inputs = [0, 1, 1, 0, 1,1,1,1,0,1,1,0,1,0,1,1]
	key = []
	for a in range(0, len(keyin)):
		key.append(int(keyin[a]))
	
	#key = [1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,1]
	output = [0]*16
	block = [0]*16			# the 128 bit block to encode

	if(len(keyin)==16):			# 16*8 = 128 keysize
		nbrRounds = 10
	elif(len(keyin)==24):
		nbrRounds = 12
	else:
		nbrRounds = 14
		
	expandedKeySize = (16*(nbrRounds+1)) 			# The expanded key will be of length (blockSize * (num rounds+1))
	
	# Set the block values, for the block:
	# a0,0 a0,1 a0,2 a0,3
	# a1,0 a1,1 a1,2 a1,3
	# a2,0 a2,1 a2,2 a2,3
	# a3,0 a3,1 a3,2 a3,3
	# the mapping order is a0,0 a1,0 a2,0 a3,0 a0,1 a1,1 ... a2,3 a3,3
	
	for i in range(0, 4):
		for j in range(0, 4):
			block[(i+(j*4))] = inputs[(i*4)+j]			#putting cols first and then moving on like this
	
	expandedKey = keyExpansion(key, expandedKeySize)
	block = aes_fn(block, expandedKey, nbrRounds)
	for k in range(0, 4):
		for l in range(0, 4):
			output[(k*4)+l] = block[(k+(l*4))]
	return output
	
def decrypt(inp, keyin):
	inputs = []
	if(len(inp)>16):
		for a in range(0, 16):
			inputs.append(int(inp[a]))
	else:
		for a in range(0, len(inp)):
			inputs.append(int(inp[a]))
		while len(inputs) < 16:
			inputs.append(0)

	key = []
	for a in range(0, len(keyin)):
		key.append(int(keyin[a]))

	output = [0]*16
	block = [0]*16			# the 128 bit block to encode

	if(len(keyin)==16):			# 16*8 = 128 keysize
		nbrRounds = 10
	elif(len(keyin)==24):
		nbrRounds = 12
	else:
		nbrRounds = 14
		
	expandedKeySize = (16*(nbrRounds+1)) 			# The expanded key will be of length (blockSize * (num rounds+1))
	
	for i in range(0, 4):
		for j in range(0, 4):
			block[(i+(j*4))] = inputs[(i*4)+j]			#putting cols first and then moving on like this
	
	expandedKey = keyExpansion(key, expandedKeySize)
	block = aes_fnInv(block, expandedKey, nbrRounds)
	for k in range(0, 4):
		for l in range(0, 4):
			output[(k*4)+l] = block[(k+(l*4))]
	return output
	
	
def encryption(inTxt, key, inVect):
	if len(inVect)!=16:
		print "Initialisation Vector not 16 bytes"
		return None
	if len(key)!=16 and len(key)!=24 and len(key)!=32:
		print "Key length is not matching"
		return None

	plaintext = []
	inputs = [0]*16
	cipherTemp = [0]*16
	cipherTxt = []

	firstRound = True
	if len(inTxt)>0:
		initVect = arr2arr(inVect, 0, 16)			#init vect is always 16
		#initVect = inVect
		for j in range(0, int(math.ceil(float(len(inTxt))/16))):
			start = j*16
			end = j*16+16
			if j*16+16 > len(inTxt):
				end = len(inTxt)
			plaintext = str2arr(inTxt,start,end)
			for i in range(0, 16):
				if firstRound:
					inputs[i] =  plaintext[i] ^ initVect[i]
				else:
					inputs[i] =  plaintext[i] ^ cipherTemp[i]
			firstRound = False
			cipherTemp = encrypt(inputs, key)
			
			for k in range(0, 16):				# always 16 bytes because padding done in str2arr
				cipherTxt.append(cipherTemp[k])
	return cipherTxt

def decryption(cipherTxt, key, inVect):
	if len(inVect)!=16:
		print "Initialisation Vector not 16 bytes"
		return None
	if len(key)!=16 and len(key)!=24 and len(key)!=32:
		print "Key length is not matching"
		return None
		
	inputs = [0]*16
	decipherTemp = [0]*16
	decipherTxt = []
	output = [0]*16
	plaintext = [0]*16

	firstRound = True
	if len(cipherTxt)>0:
		initVect = arr2arr(inVect, 0, 16)	
		for j in range(0, int(math.ceil(float(len(cipherTxt))/16))):
			start = j*16
			end = j*16+16
			if j*16+16 > len(cipherTxt):
				end = len(cipherTxt)
			inputs = cipherTxt[start:end]
			output = decrypt(inputs, key)
			for i in range(16):
				if firstRound:
					decipherTemp[i] = initVect[i] ^ output[i]
				else:
					decipherTemp[i] = plainText[i] ^ output[i]
			firstRound = False
			if len(cipherTxt) < end:
				for k in range(0, len(cipherTxt) - end +16 ):
					decipherTxt.append(decipherTemp[k])
			else:
				for k in range(0, 16):
					decipherTxt.append(decipherTemp[k])
			#plainText = inputs
			inps = []
			if(len(inputs)>16):
				for a in range(0, 16):
					inps.append(int(inputs[a]))
			else:
				for a in range(0, len(inputs)):
					inps.append(int(inputs[a]))
				while len(inps) < 16:
					inps.append(0)
			plainText = inps
	return arr2str(decipherTxt)
	
def call2run():
	# test_key = [143,194,34,208,145,203,230,143,177,246,97,206,145,92,255,84]
	print "Enter DATA"
	inputs = raw_input()
	#print len(inputs)
	#print inputs[2]
	print "Enter KEY"
	key = raw_input().split(" ")
	print "Enter Initialisation vector"
	inVect = raw_input().split(" ")
	cipherText = encryption(inputs, key, inVect)
	print cipherText
	#print len(cipherText)
	decipherText = decryption(cipherText, key, inVect)
	print decipherText

#call2run()

def convertInt2arr(n):
	ar = [0]*16
	i = 16
	while i>0:
		i = i-1
		ar[i] = n%256
		n = n/256
	return ar
	
def receive_string(server_sock, client):
	recv = receive(server_sock, client)
	#print 'string read in network layer : ',recv
	#if recv==-1 or recv == None:
		#if(dhKey==False):
			#dhKey = True
			#print "Enter your exponent_server"
			#exponent = int(raw_input())
			#dhkeyPublic = pow(base, exponent)%prime
			#send_string(server_sock, client, dhkeyPublic)
			#dhkeyPrivate = pow(recv, exponent)%prime
			#key = convertInt2arr(dhkeyPrivate)
		#else:
			#decipherText = decryption(recv, key, inVect)
			#return decipherText
	global key
	global inVect
	if recv!=None and recv!=-1:
		if return_digest(recv[0:len(recv)-32]) == recv[ len(recv) - 32: len(recv)] :
			strg = recv[0:len(recv)-32]
			cipherT = strg.split(",")
			print "CipherText"
			print cipherT
			decipherText = decryption(cipherT, key, inVect)
			return decipherText
		else:
			print 'md5 failed!!!'
	else:
		return recv

def list2str(inp):
	out = ""
	for a in range(0, len(inp)):
		if a < len(inp)-1:
			out = out+str(inp[a])
			out = out+","
		else:
			out = out+str(inp[a])
	return out

def send_string(server_sock, client, strg):
	global key
	global inVect
	cipherText = encryption(strg, key, inVect)
	cipherT = list2str(cipherText)
	cipherT_auth = return_digest(cipherT)
	packet = cipherT + cipherT_auth	
	success = send(server_sock, client, packet)
	return success
	
def check_for_requests_and_connect_network(server_sock):
	client=check_for_requests_and_connect(server_sock)
	if client!=None:
		recv=receive_blocking(server_sock,client)
		print "Enter your exponent_server"
		global base
		global prime
		global key
		global inVect
		exponent = int(raw_input())
		dhkeyPublic = pow(base, exponent)%prime
		send(server_sock, client, str(dhkeyPublic))
		dhkeyPrivate = pow(int(recv), exponent)%prime
		key = convertInt2arr(dhkeyPrivate)
		inVect = key
		return client
