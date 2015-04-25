def mathparse(a):
	str(a)
	a = ''.join(a.split())
	a = a.replace("^", "**")
	for x in range(0, len(a)):
		if a[x].isalpha():
			test1 = x - 1
			if test1 >= 0:
				if a[test1].isdigit():
					a = a[:x] + '*' + a[x:]
	print a
	return a
