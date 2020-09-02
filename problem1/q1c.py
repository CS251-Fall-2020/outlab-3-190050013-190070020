from ring import *

class Series:
	def __init__(self, k, x, n):
		self.k = int(k)
		self.x = int(x)
		self.n = int(n)

	def __iter__(self):
		self.term = RingInt(1, self.n)
		self.index = 0
		return self

	def __next__(self):
		term = self.term
		index = self.index

		if index >= self.k+1:
			raise StopIteration

		self.index = index + 1
		self.term = term * RingInt(self.x, self.n) / RingInt(self.index, self.n)

		return self.term

def main():

	in_str = str(input())
	in_list = in_str.split(' ')
	k, x, n = in_list[0], in_list[1], in_list[2]
	
	for ele in Series(k, x, n):
		print(ele)


if __name__=="__main__":
	main()

