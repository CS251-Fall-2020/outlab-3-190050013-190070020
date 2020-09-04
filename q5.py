def rotate(m):
	n = len(m)
	l = []
	for i in range(0, n):
		ll = []
		for j in range(0, n):
			ll.append(m[j][i])
		l.append(ll)
	return l


def main():
	l = []
	s = input()
	ss = s.split()
	m = len(ss)
	l.append(ss)
	for i in range(1, m):
		s = input()
		ss = s.split()
		l.append(ss)
	m = rotate(l)
	for i in range(0, len(m)):
		for j in range(0, len(m[i])):
			if j==len(m[i])-1:
				print(m[i][j], end='')
			else:
				print(m[i][j], end=' ')
		print()

if __name__ == '__main__':
	main()