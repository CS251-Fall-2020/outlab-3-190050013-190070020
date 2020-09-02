# Enter your code here
import math

class RingInt:
	def __init__(self, value, characteristic):
		self.value = value%characteristic
		self.characteristic = characteristic

	def __str__(self):
		return str(self.value)+'['+str(self.characteristic)+']'

	def __add__(self, other):
		if self.characteristic != other.characteristic:
			raise ValueError("Characteristics of the operands don't match")
		val = (self.value + other.value)%self.characteristic
		return RingInt(val, self.characteristic)

	def __sub__(self, other):
		if self.characteristic != other.characteristic:
			raise ValueError("Characteristics of the operands don't match")
		val = (self.value - other.value)%self.characteristic
		return RingInt(val, self.characteristic)

	def __mul__(self, other):
		if self.characteristic != other.characteristic:
			raise ValueError("Characteristics of the operands don't match")
		val = (self.value * other.value)%self.characteristic
		return RingInt(val, self.characteristic)

	def __truediv__(self, other):
		if self.characteristic != other.characteristic:
			raise ValueError("Characteristics of the operands don't match")
		elif other.value==0 or math.gcd(other.value, other.characteristic)!=1:
			raise ValueError("Modular division Not defined")

		inv = pow(other.value, other.characteristic - 2, other.characteristic)
		return RingInt((inv*self.value)%self.characteristic, other.characteristic)

	def __eq__(self, other):
		if self.characteristic==other.characteristic and self.value==other.value:
			return True
		else:
			return False

	def __pow__(self, a): 
		res = 1
		if self.value==0: 
			return 0

		while a>0 : 
			if (a & 1)==1: 
				res = (res * self.value) % self.characteristic 
			a = a >> 1
			a = (a * a) % self.characteristic          
		return res