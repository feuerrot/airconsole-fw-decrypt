#!/usr/bin/env python3
import struct

class XTEA():
	rounds = 32

	"""yet another xtea implementation"""
	def __init__(self, key, iv, rounds=None):
		self.key = key
		self.iv = iv
		if rounds != None:
			self.rounds = rounds

	def xtea_encrypt(self, v):
		y = v[0]
		z = v[1]
		delta = 0x9E3779B9
		mask = 0xFFFFFFFF
		sum = 0
		for i in range(self.rounds):
			y += ((((z << 4) ^ (z >> 5)) + z) ^ (sum + self.key[sum & 3]))
			y &= mask
			sum += delta
			sum &= mask
			z += ((((y << 4) ^ (y >> 5)) + y) ^ (sum + self.key[(sum >> 11) & 3]))
			z &= mask
		return (y & mask, z & mask)

	def xtea_decrypt(self, v):
		y = v[0]
		z = v[1]
		delta = 0x9E3779B9
		mask = 0xFFFFFFFF
		sum = delta * self.rounds & mask
		for i in range(self.rounds):
			z -= ((((y << 4) ^ (y >> 5)) + y) ^ (sum + self.key[(sum>>11) & 3]))
			z &= mask
			sum -= delta
			sum &= mask
			y -= ((((z << 4) ^ (z >> 5)) + z) ^ (sum + self.key[sum & 3]))
			y &= mask
		return (y & mask, z & mask)

	# does xtea in cbc mode
	def xtea_cbc_encrypt(self, data):
		data = bytearray(data)
		ptr = 0
		iv = self.iv
		while ptr < len(data):
			for i in range(8):
				data[ptr + i] ^= iv[i]
			encrypt = self.xtea_encrypt(struct.unpack_from(">II", data, offset=ptr))
			struct.pack_into(">II", data, ptr, encrypt[0], encrypt[1])
			iv = data[ptr:ptr+8]
			ptr += 8
		return data

	def xtea_cbc_decrypt(self, data):
		out = bytearray(len(data))
		ptr = 0
		iv = self.iv
		while ptr < len(data):
			buf8 = data[ptr:ptr+8]
			# is there a better solution?
			decrypt = self.xtea_decrypt(struct.unpack_from(">II", data, offset=ptr))
			decrypt = struct.pack(">II", decrypt[0], decrypt[1])
			for i in range(8):
				out[ptr + i] = decrypt[i] ^ iv[i]
			ptr += 8
			iv = buf8
		return out

if __name__ == "__main__":
	iv   = b'\x00\x00\x00\x00\x00\x00\x00\x00'
	key  = (0x00000000, 0x00000000, 0x00000000, 0x00000000)
	data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
	x = XTEA(key, iv)
	print("XTEA TEST")
	print("KEY:  {0[0]:08X} {0[1]:08X} {0[2]:08X} {0[3]:08X}".format(key))
	print("IV:   {}".format(iv))
	print("DATA: {}".format(data))
	e = x.xtea_cbc_encrypt(data)
	print("ENCRYPTION")
	print("DATA: {} ".format(e))
	d = x.xtea_cbc_decrypt(e)
	print("DECRYPTION")
	print("DATA: {}".format(d))
	
