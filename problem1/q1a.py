import argparse
from ring import *

def calc_sum1(k, x, n):
	term = RingInt(0, n) 
	sum = RingInt(0, n)
	for i in range(0, k):
		term_x = RingInt(x, n)
		term_x = term_x^i
		term_i = RingInt(1, n)
		for j in range(2, i+1):
			term_i *= RingInt(j, n)
		term = term_x/term_i
		sum += term
	return sum

def comb(n, k, m):
	fact_n = RingInt(1, m)
	fact_k = RingInt(1, m)
	fact_n_k = RingInt(1, m)
	for i in range(2, n+1):
		fact_n*=RingInt(i, m)
	for i in range(2, k+1):
		fact_k*=RingInt(i, m)
	for i in range(2, n-k+1):
		fact_n_k*=RingInt(i, m)
	return fact_n/(fact_k*fact_n_k)

def calc_sum2(k, x, n):
	sum = RingInt(1, n)
	for i in range(0, k):
		term = RingInt(0, n)
		for j in range(0, i+1):
			term+=comb(x+i-1, j, n)
		sum*=term
	return sum

def calc_sum3(k, x, n):
	sum = RingInt(0, n)
	for i in range(1, k+1):
		term = RingInt(i, n)
		for j in range(0, x):
			term*=term
		sum+=term
	return sum

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-in","--infile")
	parser.add_argument("-out","--outfile")
	args = parser.parse_args()
	fin = open(args.infile, 'r')
	fout = open(args.outfile, 'w')

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
	fin.close
	fout.close

if __name__=="__main__":
	main()
