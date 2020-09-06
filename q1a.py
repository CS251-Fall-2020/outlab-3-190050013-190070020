import argparse
from ring import *

def calc_sum1(k, x, n):
	term = RingInt(0, n)
	sum = RingInt(0, n)
	for i in range(0, k):
		term_x = RingInt(x, n)
		term_x = term_x**i
		term_i = RingInt(1, n)
		for j in range(2, i+1):
			term_i *= RingInt(j, n)
		term = term_x/term_i
		sum += term
	return sum

def calc_sum2(k, x, n):
	sum = RingInt(1, n)
	for i in range(0, k):
		term = RingInt(0, n)
		for j in range(0, i+1):
			fact_xi = RingInt(1, n)
			fact_j = RingInt(1, n)
			fact_xi_j = RingInt(1, n)
			for i in range(1, x+i+1):
				fact_xi*=RingInt(i, n)
			for i in range(1, j+1):
				fact_j*=RingInt(i, n)
			for i in range(1, x+i-j+1):
				fact_xi_j*=RingInt(i, m)
			comb = fact_xi/(fact_j*fact_xi_j)
			term+=comb
		sum*=term
	return sum

def calc_sum3(k, x, n):
	sum = RingInt(0, n)
	for i in range(1, k+1):
		term = RingInt(i, n)
		term = term**x
		sum+=term
	return sum

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-inp', type=argparse.FileType('r', encoding='UTF-8'), required=True)
	parser.add_argument('-out', type=argparse.FileType('w', encoding='UTF-8'), required=True)
	args = parser.parse_args()
	fin = args.inp
	fout = args.out

	for line in fin:
		linelist = line.split();
		for i in range(0, len(linelist)):
			linelist[i] = int(linelist[i])
		if linelist[3] == 1:
			try:
				fout.write(str(calc_sum1(linelist[0], linelist[1], linelist[2]))+"\n")
			except:
				fout.write("UNDEFINED"+"\n")
		elif linelist[3] == 2:
			try:
				fout.write(str(calc_sum2(linelist[0], linelist[1], linelist[2]))+"\n")
			except:
				fout.write("UNDEFINED"+"\n")
		elif linelist[3] == 3:
			try:
				fout.write(str(calc_sum3(linelist[0], linelist[1], linelist[2]))+"\n")
			except:
				fout.write("UNDEFINED"+"\n")
	fin.close()
	fout.close()

if __name__=="__main__":
	main()
