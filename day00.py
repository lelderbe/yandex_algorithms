
def ex_a():
	# taking two inputs at a time
	t_room, t_cond = input().split()
	t_room = int(t_room)
	t_cond = int(t_cond)
	mode = input()
	if mode == 'fan':
		return t_room
	if mode == 'auto':
		return t_cond
	if (mode == 'freeze' and t_room > t_cond) or (mode == 'heat' and t_room < t_cond):
		return t_cond
	else:
		return t_room

# print(ex_a())

def ex_b():
	def compare(x, y):
		return (x > y)

	a = int(input())
	b = int(input())
	c = int(input())
	if compare(a + b, c) and compare(a + c, b) and compare(b + c, a):
		return 'YES'
	return 'NO'

# print(ex_b())

def ex_c():
	def parse_phone(text):
		if text[0:2] == '+7':
			text = '8' + text[2:]
		text = text.replace('-', '')
		text = text.replace('(', '')
		text = text.replace(')', '')
		if len(text) < 11 and text[0:4] != '8495':
			text = '8495' + text
		return text

	def check(phone, new):
		if phone.find(new) == 0:
			print('YES')
		else:
			print('NO')

	new = parse_phone(input())
	n1 = parse_phone(input())
	n2 = parse_phone(input())
	n3 = parse_phone(input())
	check(n1, new)
	check(n2, new)
	check(n3, new)

# ex_c()

def ex_d():
	a = int(input())
	b = int(input())
	c = int(input())
	if c < 0:
		print('NO SOLUTION')
		return
	result = c * c - b;
	if a == 0:
		if result == 0:
			print('MANY SOLUTIONS')
		else:
			print('NO SOLUTION')
		return
	if result % a != 0:
		print('NO SOLUTION')
	else:
		print(result // a)

# ex_d()

from math import ceil

def ex_e():
	k2, e, k1, p1, e1 = input().split()
	k2 = int(k2)
	e = int(e)
	k1 = int(k1)
	p1 = int(p1)
	e1 = int(e1)

	# print('k2:', k2, 'e:', e, 'k1:', k1, 'p1:', p1, 'e1:', e1)

	if e1 > e or k2 <= 0 or e <= 0 or k1 <= 0 or p1 <= 0 or e1 <= 0:
		print(-1, -1)
		return
	if (e1 == 1 and p1 == 1):
		if (e == 1):
			print(0, 1)
			return
		if (e >= k2):
			print(1, 0)
			return
		if (k2 < k1):
			if (e1 == 1):
				print(1, 1)
			else:
				print(1, 0)
			return
		print(0, 0)
		return

	flats = []
	# count flats per level
	i = 1
	# for i in range (1, 100):
	while True:
		# print('i:', i)
		k_end = (p1 - 1) * e * i + e1 * i
		k_st = k_end - (i - 1)
		# print('k_st:', k_st, 'k1:', k1, 'k_end:', k_end)
		if ((k1 >= k_st) and (k1 <= k_end)):
			flats.append(i)
		if k1 < k_st:
			break
		i = i + 1

	# print(flats)
	p2 = -1
	e2 = -1
	# calc k2 data
	for i in range (len(flats)):
		e0 = ceil(1.0 * k2 / flats[i])
		p0 = ceil(1.0 * e0 / e)
		e0 = e0 % e
		if e0 == 0:
			e0 = e
		if p2 == -1 or p2 == p0:
			p2 = p0
		else:
			p2 = 0
		if e2 == -1 or e2 == e0:
			e2 = e0
		else:
			e2 = 0

	# print('end')
	print(p2, e2)

ex_e()

def ex_f():
	w1, h1, w2, h2 = input().split()
	w1 = int(w1)
	h1 = int(h1)
	w2 = int(w2)
	h2 = int(h2)
	pp = []

	pp.append(((w1 + w2), max(h1, h2)))
	pp.append(((w1 + h2), max(h1, w2)))
	pp.append(((h1 + w2), max(w1, h2)))
	pp.append(((h1 + h2), max(w1, w2)))
	# find smallest idx
	idx = 0
	p = pp[0][0] * pp[0][1]
	for i in range(1, len(pp)):
		p2 = pp[i][0] * pp[i][1]
		if p > p2:
			p = p2
			idx = i
	# print smallest P
	print(pp[idx][0], pp[idx][1])

# ex_f()

def ex_g():
	n, k, m = input().split()
	n = int(n)
	k = int(k)
	m = int(m)
	count = 0

	while n > 0:
		n = n - k
		if n >= 0:
			count = count + k // m
			n = n + k % m
		if count == 0:
			break
	print(count)

# ex_g()

def ex_i():
	def check(d, e, x, y):
		return (d >= x and e >= y) or (d >= y and e >= x)

	a = int(input())
	b = int(input())
	c = int(input())
	d = int(input())
	e = int(input())
	result = True
	if check(d, e, a, b) or check(d, e, b, c) or check(d, e, a, c):
		print('YES')
	else:
		print('NO')

# ex_i()

