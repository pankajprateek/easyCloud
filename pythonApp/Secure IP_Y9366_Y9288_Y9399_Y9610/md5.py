import define
import struct
from binascii import hexlify

S11, S12, S13, S14, S21, S22, S23, S24, S31, S32, S33, S34, S41, S42, S43, S44 = 7, 12, 17, 22, 5, 9, 14, 20, 4, 11, 16, 23, 6, 10, 15, 21


def F(x, y, z):
    return (x & y) | ((~x) & z)

def G(x, y, z):
    return (x & z) | (y & (~z))

def H(x, y, z):
    return x ^ y ^ z

def I(x, y, z):
    return y ^ (x | (~z))
    
class MD5:

# MD5 initialization -- of count, state and lengths 
	msg_digest_len = 16


	def __init__(self):
	
		self.count = [0, 0]  

		self.A = 0x67452301L 
		self.B = 0xefcdab89L
		self.C = 0x98badcfeL
		self.D = 0x10325476L
		
		self.buffer= [ ]

	def transform(self, inp):

	        a, b, c, d = A, B, C, D = self.A, self.B, self.C, self.D
	        # Round 1 calculation:

	        a = define.XX(F, a, b, c, d, inp[ 0], S11, 0xD76AA478L) # 1 
	        d = define.XX(F, d, a, b, c, inp[ 1], S12, 0xE8C7B756L) # 2 
	        c = define.XX(F, c, d, a, b, inp[ 2], S13, 0x242070DBL) # 3 
	        b = define.XX(F, b, c, d, a, inp[ 3], S14, 0xC1BDCEEEL) # 4 
	        a = define.XX(F, a, b, c, d, inp[ 4], S11, 0xF57C0FAFL) # 5 
	        d = define.XX(F, d, a, b, c, inp[ 5], S12, 0x4787C62AL) # 6 
	        c = define.XX(F, c, d, a, b, inp[ 6], S13, 0xA8304613L) # 7 
	        b = define.XX(F, b, c, d, a, inp[ 7], S14, 0xFD469501L) # 8 
	        a = define.XX(F, a, b, c, d, inp[ 8], S11, 0x698098D8L) # 9 
	        d = define.XX(F, d, a, b, c, inp[ 9], S12, 0x8B44F7AFL) # 10 
	        c = define.XX(F, c, d, a, b, inp[10], S13, 0xFFFF5BB1L) # 11 
	        b = define.XX(F, b, c, d, a, inp[11], S14, 0x895CD7BEL) # 12 
	        a = define.XX(F, a, b, c, d, inp[12], S11, 0x6B901122L) # 13 
	        d = define.XX(F, d, a, b, c, inp[13], S12, 0xFD987193L) # 14 
	        c = define.XX(F, c, d, a, b, inp[14], S13, 0xA679438EL) # 15 
	        b = define.XX(F, b, c, d, a, inp[15], S14, 0x49B40821L) # 16 

	        # Round 2 calculation:


	        a = define.XX(G, a, b, c, d, inp[ 1], S21, 0xF61E2562L) # 17 
	        d = define.XX(G, d, a, b, c, inp[ 6], S22, 0xC040B340L) # 18 
	        c = define.XX(G, c, d, a, b, inp[11], S23, 0x265E5A51L) # 19 
	        b = define.XX(G, b, c, d, a, inp[ 0], S24, 0xE9B6C7AAL) # 20 
	        a = define.XX(G, a, b, c, d, inp[ 5], S21, 0xD62F105DL) # 21 
	        d = define.XX(G, d, a, b, c, inp[10], S22, 0x02441453L) # 22 
	        c = define.XX(G, c, d, a, b, inp[15], S23, 0xD8A1E681L) # 23 
	        b = define.XX(G, b, c, d, a, inp[ 4], S24, 0xE7D3FBC8L) # 24 
	        a = define.XX(G, a, b, c, d, inp[ 9], S21, 0x21E1CDE6L) # 25 
	        d = define.XX(G, d, a, b, c, inp[14], S22, 0xC33707D6L) # 26 
	        c = define.XX(G, c, d, a, b, inp[ 3], S23, 0xF4D50D87L) # 27 
	        b = define.XX(G, b, c, d, a, inp[ 8], S24, 0x455A14EDL) # 28 
	        a = define.XX(G, a, b, c, d, inp[13], S21, 0xA9E3E905L) # 29 
	        d = define.XX(G, d, a, b, c, inp[ 2], S22, 0xFCEFA3F8L) # 30 
	        c = define.XX(G, c, d, a, b, inp[ 7], S23, 0x676F02D9L) # 31 
	        b = define.XX(G, b, c, d, a, inp[12], S24, 0x8D2A4C8AL) # 32 

	        # Round 3 calculation:


	        a = define.XX(H, a, b, c, d, inp[ 5], S31, 0xFFFA3942L) # 33 
	        d = define.XX(H, d, a, b, c, inp[ 8], S32, 0x8771F681L) # 34 
	        c = define.XX(H, c, d, a, b, inp[11], S33, 0x6D9D6122L) # 35 
	        b = define.XX(H, b, c, d, a, inp[14], S34, 0xFDE5380CL) # 36 
	        a = define.XX(H, a, b, c, d, inp[ 1], S31, 0xA4BEEA44L) # 37 
	        d = define.XX(H, d, a, b, c, inp[ 4], S32, 0x4BDECFA9L) # 38 
	        c = define.XX(H, c, d, a, b, inp[ 7], S33, 0xF6BB4B60L) # 39 
	        b = define.XX(H, b, c, d, a, inp[10], S34, 0xBEBFBC70L) # 40 
	        a = define.XX(H, a, b, c, d, inp[13], S31, 0x289B7EC6L) # 41 
	        d = define.XX(H, d, a, b, c, inp[ 0], S32, 0xEAA127FAL) # 42 
	        c = define.XX(H, c, d, a, b, inp[ 3], S33, 0xD4EF3085L) # 43 
	        b = define.XX(H, b, c, d, a, inp[ 6], S34, 0x04881D05L) # 44 
	        a = define.XX(H, a, b, c, d, inp[ 9], S31, 0xD9D4D039L) # 45 
	        d = define.XX(H, d, a, b, c, inp[12], S32, 0xE6DB99E5L) # 46 
	        c = define.XX(H, c, d, a, b, inp[15], S33, 0x1FA27CF8L) # 47 
	        b = define.XX(H, b, c, d, a, inp[ 2], S34, 0xC4AC5665L) # 48 

	        # Round 4 calculation:


	        a = define.XX(I, a, b, c, d, inp[ 0], S41, 0xF4292244L) # 49 
	        d = define.XX(I, d, a, b, c, inp[ 7], S42, 0x432AFF97L) # 50 
	        c = define.XX(I, c, d, a, b, inp[14], S43, 0xAB9423A7L) # 51 
	        b = define.XX(I, b, c, d, a, inp[ 5], S44, 0xFC93A039L) # 52 
	        a = define.XX(I, a, b, c, d, inp[12], S41, 0x655B59C3L) # 53 
	        d = define.XX(I, d, a, b, c, inp[ 3], S42, 0x8F0CCC92L) # 54 
	        c = define.XX(I, c, d, a, b, inp[10], S43, 0xFFEFF47DL) # 55 
	        b = define.XX(I, b, c, d, a, inp[ 1], S44, 0x85845DD1L) # 56 
	        a = define.XX(I, a, b, c, d, inp[ 8], S41, 0x6FA87E4FL) # 57 
	        d = define.XX(I, d, a, b, c, inp[15], S42, 0xFE2CE6E0L) # 58 
	        c = define.XX(I, c, d, a, b, inp[ 6], S43, 0xA3014314L) # 59 
	        b = define.XX(I, b, c, d, a, inp[13], S44, 0x4E0811A1L) # 60 
	        a = define.XX(I, a, b, c, d, inp[ 4], S41, 0xF7537E82L) # 61 
	        d = define.XX(I, d, a, b, c, inp[11], S42, 0xBD3AF235L) # 62 
	        c = define.XX(I, c, d, a, b, inp[ 2], S43, 0x2AD7D2BBL) # 63 
	        b = define.XX(I, b, c, d, a, inp[ 9], S44, 0xEB86D391L) # 64 

	        A = (A + a) & 0xffffffffL
	        B = (B + b) & 0xffffffffL
	        C = (C + c) & 0xffffffffL
	        D = (D + d) & 0xffffffffL

	        self.A, self.B, self.C, self.D = A, B, C, D

	def update(self, input_msg): # self is like context in rfc1321

		# Though we would not be using the input directly here, we need its length.
		# Repeated calls are equivalent to a single call with concatenation of the arguments

		input_len = long(len(input_msg))
		index = ((self.count[0] >> 3) & 0x3FL) # number of bytes mod 64

		#update the number of bits
		self.count[0] += (input_len << 3)

		if self.count[0] < (input_len << 3):
			self.count[1] += 1

		self.count[1] += (input_len >> 29)
		part_len = 64 - index

		# Transform as many times as possible
		if input_len >= part_len:
			temp = list(input_msg)
			self.buffer[index:] = temp[:part_len]
			self.transform(define.decode(self.buffer))
	
			i = part_len
			while i + 63 < input_len:
				self.transform(define.decode(temp[i:i+64]))
				i += 64
			else:
				index = 0
                		#self.input = list(input_msg[i:input_len])
		else:
			i= 0
			#temp_im = list(input_msg)
			self.buffer += list(input_msg)

	def final_digest (self):

		# MD5 finalization: ends an MD5 message-digest operation returning the 16 byte digest

		# Performs the function of encode func of rfc1321
		A = self.A
        	B = self.B
        	C = self.C
        	D = self.D

        	input = [ ] + self.buffer 
        	count = [ ] + self.count 

		# Padding out to 56 mod 64
		index = (self.count[0] >> 3) & 0x3fL
		if index < 56:
			padding_len = 56 - index
		else:
			padding_len = 120 - index

		padding = ['\200'] + ['\000'] * 63
       		self.update(padding[:padding_len]) # Call to update here does padding.

        	bits = define.decode(self.buffer[:56]) + count
		self.transform(bits)
	
        	# Store state in digest.
        	digest = struct.pack("<IIII", self.A, self.B, self.C, self.D)

        	self.A = A 
        	self.B = B
        	self.C = C
        	self.D = D

      		self.buffer = input 
        	self.count = count 

        	return hexlify(digest)

def return_digest (strg):

	k = MD5()
	k.update(strg)
	DIGEST = k.final_digest()
	print DIGEST
	return DIGEST
