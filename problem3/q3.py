import argparse
from collections import Counter

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-ca', type=argparse.FileType('r'), required=True)
	parser.add_argument('-ch', type=argparse.FileType('r'), required=True)
	args = parser.parse_args()
	fca = args.ca
	fch = args.ch

	M = int(fca.readline())
	types_counter = Counter(fca.readline().split())

	N = int(fch.readline())
	dict = {}
	for i in range(0, N):
		l = fch.readline().split()
		a = l[0]
		b = int(l[1])
		if a not in dict:
			dict[a] = [b]
		else:
			dict[a].append(b)
	profit = 0
	for item in dict.keys():
		dict[item].sort(reverse=True)
		if item in types_counter:
			if len(dict[item]) <= types_counter[item]:
				for money in dict[item]:
					profit+=money
			else:
				for i in range(0, types_counter[item]):
					profit+=dict[item][i]
	print(profit)

if __name__ == '__main__':
	main()