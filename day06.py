def l_bin_search(l, r, check, opts):
	while l < r:
		m = (l + r) // 2
		print('m:', m)
		if check(m, opts):
			r = m
		else:
			l = m + 1
		print('l:', l, 'r:', r)
	return l

def r_bin_search(l, r, check, opts):
	while l < r:
		m = (l + r + 1) // 2
		# print('l:', l, 'r:', r, 'm:', m)
		if check(m, opts):
			l = m
		else:
			r = m - 1
	return l

def check_end_parents(m, opts):
	n, k = opts
	# print((k + m) * 3, '>=', n + m)
	return (k + m) * 3 >= n + m

def check_stickers(size, opts):
	n, w, h = opts
	return (w // size) * (h // size) >= n

def ex1():
	n = 500	# человек
	k = 50	# родителей
	print(l_bin_search(0, n, check_end_parents, (n, k)))

def ex3():
	n = 5	# стикеров нужно разместить
	w = 50	# ширина доски
	h = 20	# высота доски
	print(r_bin_search(0, w, check_stickers, (n, w, h)))

# ex1()
# ex3()

########
def bin_search(l, r, check, opts):
	arr, x = opts
	idx = -1
	while l <= r and idx == -1:
		m = (l + r) // 2
		# print('l:', l, 'r:', r, 'idx:', idx, 'm:', m)
		# print('arr[m]:', arr[m], 'x:', x)
		if arr[m] == x:
			idx = m
		elif arr[m] < x:
			l = m + 1
		elif arr[m] > x:
			r = m - 1
	return idx

########
def ex_classic_bin_search():
	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(bin_search(0, len(arr) - 1, 0, (arr, 4)))

# ex_classic_bin_search()

def ex_a():
	n, k = list(map(int, input().split()))
	arr_n = list(map(int, input().split()))
	arr_k = list(map(int, input().split()))
	for i in arr_k:
		if bin_search(0, n - 1, 0, (arr_n, i)) != -1:
			print('YES')
		else:
			print('NO')

# ex_a()

# def ex_b():
# 	def check_le(m, opts):
# 		arr, x = opts
# 		return arr[m] <= x

# 	def check_ge(m, opts):
# 		arr, x = opts
# 		return arr[m] >= x

# 	def l_bin_search(l, r, check, opts):
# 		while l < r:
# 			m = (l + r) // 2
# 			if check(m, opts):
# 				r = m
# 			else:
# 				l = m + 1
# 		return l

# 	def r_bin_search(l, r, check, opts):
# 		while l < r:
# 			m = (l + r + 1) // 2
# 			if check(m, opts):
# 				l = m
# 			else:
# 				r = m - 1
# 		return l

# 	n, k = list(map(int, input().split()))
# 	arr_n = list(map(int, input().split()))
# 	arr_k = list(map(int, input().split()))
# 	known = {}
# 	for i in arr_k:
# 		if i in known:
# 			print(known[i])
# 		else:
# 			a = arr_n[r_bin_search(0, n - 1, check_le, (arr_n, i))]
# 			b = arr_n[l_bin_search(0, n - 1, check_ge, (arr_n, i))]
# 			if abs(a - i) <= abs(b - i):
# 				print(a)
# 				known[i] = a
# 			else:
# 				print(b)
# 				known[i] = b

# ex_b()

def ex_b():
	def l_bin_search(l, r, arr, x):
		while l < r:
			m = (l + r) // 2
			if arr[m] >= x:
				r = m
			else:
				l = m + 1
		return l

	def r_bin_search(l, r, arr, x):
		while l < r:
			m = (l + r + 1) // 2
			if arr[m] <= x:
				l = m
			else:
				r = m - 1
		return l

	n, k = list(map(int, input().split()))
	arr_n = list(map(int, input().split()))
	arr_k = list(map(int, input().split()))
	known = {}
	for i in arr_k:
		if i in known:
			print(known[i])
		else:
			a = arr_n[r_bin_search(0, n - 1, arr_n, i)]
			b = arr_n[l_bin_search(0, n - 1, arr_n, i)]
			if abs(a - i) <= abs(b - i):
				print(a)
				known[i] = a
			else:
				print(b)
				known[i] = b

# ex_b()

def ex_c():
	def check(size, opts):
		n, w, h = opts
		return (size // w) * (size // h) >= n

	def l_bin_search(l, r, check, opts):
		while l < r:
			m = (l + r) // 2
			if check(m, opts):
				r = m
			else:
				l = m + 1
		return l

	w, h, n = list(map(int, input().split()))
	print(l_bin_search(0, n * h, check, (n, w, h)))

# ex_c()

def ex_d():
	def check(size, opts):
		n, w, h, a, b = opts
		return (w // (a + 2 * size)) * (h // (b + 2 * size)) >= n or \
				(h // (a + 2 * size)) * (w // (b + 2 * size)) >= n

	def r_bin_search(l, r, check, opts):
		while l < r:
			m = (l + r + 1) // 2
			if check(m, opts):
				l = m
			else:
				r = m - 1
		return l

	n, a, b, w, h = list(map(int, input().split()))
	print(r_bin_search(0, w, check, (n, w, h, a, b)))

# ex_d()

def ex_e():
	def check(m, opts):
		a, b, c = opts
		result = 2 * a + 3 * b + 4 * c + 5 * m
		count = a + b + c + m
		return result >= 3.5 * count
		# return round(result * 1.0 / count) >= 4

	def l_bin_search(l, r, check, opts):
		while l < r:
			m = (l + r) // 2
			if check(m, opts):
				r = m
			else:
				l = m + 1
		return l

	a = int(input())
	b = int(input())
	c = int(input())
	print(l_bin_search(0, a + a + b, check, (a, b, c)))

# ex_e()

def ex_f():
	def check(m, opts):
		n, x, y = opts
		min_p = min(x, y)
		max_p = max(x, y)
		count = m // min_p + (m - min_p) // max_p
		return count >= n

	def l_bin_search(l, r, check, opts):
		while l < r:
			m = (l + r) // 2
			if check(m, opts):
				r = m
			else:
				l = m + 1
		return l

	n, x, y = list(map(int, input().split()))
	print(l_bin_search(0, min(x, y) * n, check, (n, x, y)))

# ex_f()

def ex_g():
	def check(size, opts):
		n, m, t = opts
		if size * 2 > n or size * 2 > m:
			return False
		count = 2 * n * size + 2 * m * size - 4 * size * size
		return count <= t

	def r_bin_search(l, r, check, opts):
		while l < r:
			m = (l + r + 1) // 2
			if check(m, opts):
				l = m
			else:
				r = m - 1
		return l

	n = int(input())
	m = int(input())
	t = int(input())
	print(r_bin_search(0, t, check, (n, m, t)))

# ex_g()

def ex_h():
	def check(l, opts):
		k, arr = opts
		if l == 0:
			return True
		count = 0
		for i in arr:
			count = count + i // l
		return count >= k

	def r_bin_search(l, r, check, opts):
		while l < r:
			m = (l + r + 1) // 2
			if check(m, opts):
				l = m
			else:
				r = m - 1
		return l

	n, k = list(map(int, input().split()))
	arr = []
	for _ in range(n):
		arr.append(int(input()))
	result = r_bin_search(0, 10000000, check, (k, arr))
	print(result)

ex_h()
