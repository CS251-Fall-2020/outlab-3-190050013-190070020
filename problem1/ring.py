# Enter your code here

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
		val = (self.value - other.value+self.characteristic)%self.characteristic
		return RingInt(val, self.characteristic)

	def __mul__(self, other):
		if self.characteristic != other.characteristic:
			raise ValueError("Characteristics of the operands don't match")
		val = (self.value * other.value)%self.characteristic
		return RingInt(val, self.characteristic)

	def __truediv__(self, other):
		if self.characteristic != other.characteristic:
			raise ValueError("Characteristics of the operands don't match")
		elif other.value==0 or self.gcd(other.value, other.characteristic)!=1:
			raise ValueError("Modular division Not defined")
		a = other.value 
		inv = 1
		for x in range(1, other.characteristic) : 
			if ((a * x) % other.characteristic == 1) : 
				inv = x
				break
		return RingInt((inv*self.value)%self.characteristic, other.characteristic)

	def __eq__(self, other):
		if self.characteristic==other.characteristic and self.value==other.value:
			return True
		else:
			return False

	def __pow__(self, a): 
		res = 1
		x = self.value 
		if x==0: 
			return RingInt(0, self.characteristic)

		while a>0 :
			if (a & 1)==1: 
				res = (res * x) % self.characteristic 
			a = a >> 1
			x = (x * x) % self.characteristic          
		return RingInt(res, self.characteristic)

	def gcd(self, a, b):
		if(a%b==0):
			return b
		else:
			return self.gcd(b, a%b)