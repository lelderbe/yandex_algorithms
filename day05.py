def ex_a():
	n = int(input())
	tops = list(map(int, input().split()))
	m = int(input())
	pants = list(map(int, input().split()))
	tops_idx = pants_idx = 0
	top = tops[tops_idx]
	pant = pants[pants_idx]
	diff = abs(top - pant)
	while diff != 0:
		if tops[tops_idx] < pants[pants_idx]:
			tops_idx = tops_idx + 1
		else:
			pants_idx = pants_idx + 1
		if tops_idx == n or pants_idx == m:
			break
		if abs(tops[tops_idx] - pants[pants_idx]) < diff:
			top = tops[tops_idx]
			pant = pants[pants_idx]
			diff = abs(top - pant)
	print(top, pant)

# ex_a()

# def ex_b():
# 	n, lucky = list(map(int, input().split()))
# 	cars = list(map(int, input().split()))
# 	count = 0
# 	for i in range(n):
# 		s = 0
# 		for j in range(i, n):
# 			s = s + cars[j]
# 			if s == lucky:
# 				count = count + 1
# 			if s >= lucky:
# 				break
# 	return count

def ex_b():
	n, lucky = list(map(int, input().split()))
	cars = list(map(int, input().split()))
	prefs = [0] * (len(cars) + 1)
	for i in range(1, n + 1):
		prefs[i] = prefs[i - 1] + cars[i - 1]
	count = 0
	l = 0
	r = 1
	for i in range(l, n + 1):
		for j in range(r, n + 1):
			s = prefs[j] - prefs[i]
			if s == lucky:
				count = count + 1
			if s >= lucky:
				break
			r = r + 1
	return count

# print(ex_b())

def ex_c():
	n = int(input())
	tops = [0] * (n + 1)
	up = [0] * (n + 1)
	down = [0] * (n + 1)
	for i in range(1, n + 1):
		x, y = list(map(int, input().split()))
		tops[i] = y
		if tops[i] > tops[i - 1]:
			up[i] = up[i - 1] + tops[i] - tops[i - 1]
			down[i] = down[i - 1]
		else:
			up[i] = up[i - 1]
			down[i] = down[i - 1] + tops[i - 1] - tops[i]
	m = int(input())
	for i in range(m):
		a, b = list(map(int, input().split()))
		if a > b:
			print(down[a] - down[b])
		elif a < b:
			print(up[b] - up[a])
		else:
			print(0)

# ex_c()

def ex_d():
	n, r = list(map(int, input().split()))
	seq = list(map(int, input().split()))
	count = 0
	right = 1
	for left in range(len(seq)):
		while right < len(seq):
			if seq[right] - seq[left] > r:
				count = count + len(seq) - right
				break
			right = right + 1
	return (count)

# print(ex_d())

def ex_e():
	n, k = list(map(int, input().split()))
	seq = list(map(int, input().split()))
	map2 = {}
	l = r = 0
	a = 0
	b = n - 1
	while l < n and r < n:
		if seq[r] not in map2:
			map2[seq[r]] = 0
		map2[seq[r]] += 1
		if len(map2) == k:
			if r - l + 1 == k:
				return (l + 1, r + 1)
			if r - l < b - a:
				b = r
				a = l
			if map2[seq[l]] == 1:
				del map2[seq[l]]
			else:
				map2[seq[l]] -= 1
			if map2[seq[r]] == 1:
				del map2[seq[r]]
			else:
				map2[seq[r]] -= 1
			l = l + 1
		else:
			r = r + 1
	return (a + 1, b + 1)

# print(*ex_e())

def ex_f():
	cond = {}

	def add(b, c):
		if b in cond and cond[b] < c:
			return
		for i in list(cond):
			if i < b and cond[i] >= c:
				del cond[i]
			if i > b and cond[i] < c:
				return
		cond[b] = c

	n = int(input())
	seq = {}
	for i in list(map(int, input().split())):
		if i not in seq:
			seq[i] = 0
		seq[i] += 1
	m = int(input())
	for i in range(m):
		b, c = list(map(int, input().split()))
		add(b, c)
	# print(seq)
	# print(cond)
	price = 0
	for i in seq:
		for j in sorted(cond):
			if j >= i:
				price = price + cond[j] * seq[i]
				break
	return (price)

print(ex_f())
