def ex_a():
	elements = input().split()
	lst = list(map(int, elements))[:len(elements)]
	if len(lst) == 0:
		return 'YES'
	n = lst[0]
	for i in range(1, len(lst)):
		if (lst[i] > n):
			n = lst[i]
		else:
			return 'NO'
	return 'YES'

# print(ex_a())

# def ex_b():
# 	var_const = True
# 	var_ASC = True
# 	var_weak_ASC = True
# 	var_DESC = True
# 	var_weak_DESC = True

# 	n = int(input())
# 	if n == -2000000000:
# 		return 'RANDOM'
# 	while True:
# 		a = int(input())
# 		if a == -2000000000:
# 			break
# 		if (var_const):
# 			var_const = n == a
# 		if (var_ASC):
# 			var_ASC = n < a
# 		if (var_weak_ASC):
# 			var_weak_ASC = n <= a
# 		if (var_DESC):
# 			var_DESC = n > a
# 		if (var_weak_DESC):
# 			var_weak_DESC = n >= a
# 		n = a

# 	pass


def ex_b():
	def is_constant(a, b):
		if a == b:
			return 1
		return -1

	def is_ASC(a, b):
		if a < b:
			return 1
		return -1

	def is_weak_ASC(result, a, b):
		if a < b:
			return 1
		elif a == b:
			return result
		return -1

	def is_DESC(a, b):
		if a > b:
			return 1
		return -1

	def is_weak_DESC(result, a, b):
		if a > b:
			return 1
		elif a == b:
			return result
		return -1

	def print_result(flags):
		if flags[0] == 1:
			print('CONSTANT')
		elif flags[1] == 1:
			print('ASCENDING')
		elif flags[2] == 1:
			print('WEAKLY ASCENDING')
		elif flags[3] == 1:
			print('DESCENDING')
		elif flags[4] == 1:
			print('WEAKLY DESCENDING')
		else:
			print('RANDOM')

	flags = [0, 0, 0, 0, 0]

	n = int(input())
	if n == -2000000000:
		print('RANDOM')
		return
	while True:
		a = int(input())
		if a == -2000000000:
			break
		if (flags[0] != -1): flags[0] = is_constant(n, a)
		if (flags[1] != -1): flags[1] = is_ASC(n, a)
		if (flags[2] != -1): flags[2] = is_weak_ASC(flags[2], n, a)
		if (flags[3] != -1): flags[3] = is_DESC(n, a)
		if (flags[4] != -1): flags[4] = is_weak_DESC(flags[4], n, a)
		n = a
	print_result(flags)

ex_b()

def ex_c():
	n = int(input())
	elements = input().split()
	lst = list(map(int, elements))[:n]
	x = int(input())
	dx = abs(lst[0] - x)
	y = lst[0]
	for i in range(1, n):
		if abs(lst[i] - x) < dx:
			dx = abs(lst[i] - x)
			y = lst[i]
	return y

# print(ex_c())


def ex_d():
	elements = input().split()
	lst = list(map(int, elements))[:len(elements)]
	count = 0
	for i in range(1, len(lst) - 1):
		if (lst[i] > lst[i - 1] and lst[i] > lst[i + 1]):
			count = count + 1
	return count

# print(ex_d())

def ex_g():
	elements = input().split()
	lst = list(map(int, elements))[:len(elements)]
	min1 = min(lst[0], lst[1])
	min2 = max(lst[0], lst[1])
	max1 = min2
	max2 = min1
	for i in range(2, len(lst)):
		x = lst[i]
		if x >= max1:
			max2 = max1
			max1 = x
		elif x > max2:
			max2 = x
		if x <= min1:
			min2 = min1
			min1 = x
		elif x < min2:
			min2 = x
	if (min1 * min2 > max1 * max2):
		print(min(min1, min2), max(min1, min2))
	else:
		print(min(max1, max2), max(max1, max2))

# ex_g()

def ex_h():
	def sort_three(lst):
		for i in range(2):
			if lst[i] > lst[i + 1]:
				tmp = lst[i + 1]
				lst[i + 1] = lst[i]
				lst[i] = tmp
		if lst[0] > lst[1]:
			tmp = lst[1]
			lst[1] = lst[0]
			lst[0] = tmp

	elements = input().split()
	lst = list(map(int, elements))[:len(elements)]
	sort_three(lst)
	min1 = lst[0]
	min2 = lst[1]
	max0 = lst[2]
	max1 = lst[1]
	max2 = lst[0]
	for i in range(3, len(lst)):
		x = lst[i]
		if x > max0:
			tmp = max0
			max0 = x
			x = tmp
		if x >= max1:
			max2 = max1
			max1 = x
		elif x > max2:
			max2 = x
		if x <= min1:
			min2 = min1
			min1 = x
		elif x < min2:
			min2 = x
	if (min1 * min2 * max0 > max1 * max2 * max0):
		print(max0, min1, min2)
	else:
		print(max0, max1, max2)

# ex_h()

