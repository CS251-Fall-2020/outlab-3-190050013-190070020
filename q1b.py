from ring import *
import re
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', type=argparse.FileType('r', encoding='UTF-8'), required=True)
	args = parser.parse_args()
	fin = args.m
	n = int(fin.readline())
	found_at_least_one_matching_pattern = False
	for line in fin:
		pattern = re.compile(r"\$\(.+\)\#\(.+\)\$")
		r = pattern.search(line)
		if(r==None):
			continue
		starts = []
		end = 0
		while r:
			starts.append(r.start())
			end = r.end()
			r = pattern.search(line,r.start() + 2)
		starts.append(end)
		matches =[]
		for i in range(0, len(starts)-1):
			m = pattern.search(line, starts[i], starts[i+1])
			if(m):
				matches.append(m)
		for i in range(0, len(matches)):
			m = matches[i]
			m_temp = m
			while(m):
				m_temp = m
				m = pattern.search(line, m.start(), m.end()-2)
			matches[i] = m_temp


		for match in matches:
			# print(match)
			combinations = match.group()[2:-2]
			# print(combinations)
			combination_list = combinations.split(')#(')
			# print(combination_list)
			for single_list in combination_list:
				single_list_split = single_list.split(',')
				try:
					for i in range(0, len(single_list_split)):
						single_list_split[i] = int(single_list_split[i])
				except:
						break
				# print(single_list_split)
				found_at_least_one_matching_pattern = True
				for i in range(0, len(single_list_split)):
					if single_list_split[i]>=n or single_list_split[i]<0:
						print("CORRUPTED")
						return 0
				sum = RingInt(0, n)
				for i in range(1, len(single_list_split)+1):
					sum += RingInt(i, n)*RingInt(single_list_split[i-1], n)
				if sum!=RingInt(0, n):
					print("CORRUPTED")
					return 0
	# if(found_at_least_one_matching_pattern==True):
	print("OK")
	fin.close()

if __name__=="__main__":
	main()