def ex_a():
	return len(set(list(map(int, input().split()))))

# print(ex_a())

def ex_b():
	set1 = set(list(map(int, input().split())))
	set2 = set(list(map(int, input().split())))
	lst = list(set1 & set2)
	lst.sort()
	return lst

# print(*ex_b())

def ex_c():
	n, m = list(map(int, input().split()))
	set1 = set()
	set2 = set()
	for i in range(n):
		set1.add(int(input()))
	for i in range(m):
		set2.add(int(input()))
	lst = list(set1 & set2)
	lst.sort()
	print(len(lst))
	print(*lst)
	lst = list(set1 - set2)
	lst.sort()
	print(len(lst))
	print(*lst)
	lst = list(set2 - set1)
	lst.sort()
	print(len(lst))
	print(*lst)

# ex_c()

import sys
# import re

def ex_d():
	set1 = set()
	for line in sys.stdin:
		for part in line.split():
			set1.add(part)
		# for part in re.split('[ ,.\\n]', line):
		# 	if part != '':
		# 		set1.add(part)
	# print(set1)
	return len(set1)

# print(ex_d())

def ex_e():
	set1 = set(list(map(int, input().split())))
	set2 = set()
	n = input()
	for char in n:
		set2.add(int(char))
	lst = list(set2 - set1)
	return lst

# print(len(ex_e()))

def ex_f():
	gen1 = input()
	set2 = set()
	gen2 = input()
	for i in range (len(gen2) - 1):
		set2.add(gen2[i:i + 2])
	count = 0
	for i in range(len(gen1) - 1):
		if gen1[i:i + 2] in set2:
			count = count + 1
	return count

# print(ex_f())

def ex_g():
	n = int(input())
	set1 = set()
	for i in range(n):
		data = input()
		a, b = list(map(int, data.split()))
		if a + b + 1 != n:
			continue
		if a < 0 or b < 0:
			continue
		set1.add(data)
	return len(set1)

# print(ex_g())

def ex_h():
	n = int(input())
	set1 = set()
	for i in range(n):
		data = input()
		x, y = list(map(int, data.split()))
		if x <= 0 or y < 0:
			continue
		set1.add(x)
	return len(set1)

print(ex_h())
