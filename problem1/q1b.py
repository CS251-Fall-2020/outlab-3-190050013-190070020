from ring import *
import re
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', type=argparse.FileType('r', encoding='UTF-8'), required=True)
	args = parser.parse_args()
	fin = args.m
	n = int(fin.readline())
	for line in fin:
		m = re.search(r"\$\(.+\#.+\)\$", line)
		if(m):
			combination = line[m.start()+2:m.end()-2]
			combinationlist = combination.split(')#(')
			for i in range(0, len(combinationlist)):
				combinationlist[i] = combinationlist[i].split(',')
			for single_list in combinationlist:
				sum = RingInt(0, n)
				for i in range(1, len(single_list)+1):
					sum += RingInt(i, n)*RingInt(int(single_list[i-1]), n)
				if sum!=RingInt(0, n):
					Print("CORRUPTED")
					return 0
			print("OK")
			return 0

if __name__=="__main__":
	main()