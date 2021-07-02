def ex_a():
	def add(root, n):
		if root[0] == None:
			root[0] = n
		elif root[0] == n:
			return
		elif root[0] > n:
			if root[1] == None:
				root[1] = [None, None, None]
			add(root[1], n)
		elif root[0] < n:
			if root[2] == None:
				root[2] = [None, None, None]
			add(root[2], n)

	def height(root):
		if root[0] == None:
			return 0
		if root[1] == None and root[2] == None:
			return 1
		if root[1] == None and root[2] != None:
			return 1 + height(root[2])
		elif root[1] != None and root[2] == None:
			return 1 + height(root[1])
		else:
			return 1 + max(height(root[1]), height(root[2]))

	nums = list(map(int, input().split()))
	tree = [None, None, None]
	for i in nums:
		if i == 0:
			break
		add(tree, i)
	# print(tree)
	return height(tree)

# print(ex_a())

def ex_b():
	def add(root, n, level):
		if root[0] == None:
			root[0] = n
			return level + 1
		elif root[0] == n:
			return None
		elif root[0] > n:
			if root[1] == None:
				root[1] = [None, None, None]
			return add(root[1], n, level + 1)
		elif root[0] < n:
			if root[2] == None:
				root[2] = [None, None, None]
			return add(root[2], n, level + 1)

	nums = list(map(int, input().split()))
	tree = [None, None, None]
	ans = []
	for i in nums:
		if i == 0:
			break
		level = add(tree, i, 0)
		if level != None:
			ans.append(level)
	return ans

# print(*ex_b())

def ex_c():
	def add(root, n, level):
		if root[0] == None:
			root[0] = n
			return level + 1
		elif root[0] == n:
			return None
		elif root[0] > n:
			if root[1] == None:
				root[1] = [None, None, None]
			return add(root[1], n, level + 1)
		elif root[0] < n:
			if root[2] == None:
				root[2] = [None, None, None]
			return add(root[2], n, level + 1)

	def get_max(root):
		if root[2] == None:
			return (root[0])				
		return get_max(root[2])

	def get_2_max(root, max2 = None):
		if root[2] == None:
			if root[1] == None:
				return (root[0], max2)
			else:
				return (root[0], get_max(root[1]))
		return get_2_max(root[2], root[0])

	nums = list(map(int, input().split()))
	tree = [None, None, None]
	for i in nums:
		if i == 0:
			break
		level = add(tree, i, 0)
	result = get_2_max(tree)
	# print(result)
	return result[1]

# print(ex_c())

def ex_d():
	def add(root, n, level):
		if root[0] == None:
			root[0] = n
			return level + 1
		elif root[0] == n:
			return None
		elif root[0] > n:
			if root[1] == None:
				root[1] = [None, None, None]
			return add(root[1], n, level + 1)
		elif root[0] < n:
			if root[2] == None:
				root[2] = [None, None, None]
			return add(root[2], n, level + 1)

	def apply_infix(root, f):
		if root != None:
			apply_infix(root[1], f)
			if root[0] != None:
				f(root[0])
			apply_infix(root[2], f)

	nums = list(map(int, input().split()))
	tree = [None, None, None]
	for i in nums:
		if i == 0:
			break
		level = add(tree, i, 0)
	apply_infix(tree, print)

# ex_d()

def ex_e():
	def add(root, n, level):
		if root[0] == None:
			root[0] = n
			return level + 1
		elif root[0] == n:
			return None
		elif root[0] > n:
			if root[1] == None:
				root[1] = [None, None, None]
			return add(root[1], n, level + 1)
		elif root[0] < n:
			if root[2] == None:
				root[2] = [None, None, None]
			return add(root[2], n, level + 1)

	def apply_infix(root, f):
		if root != None:
			apply_infix(root[1], f)
			if root[0] != None and root[1] == None and root[2] == None:
				f(root[0])
			apply_infix(root[2], f)

	nums = list(map(int, input().split()))
	tree = [None, None, None]
	for i in nums:
		if i == 0:
			break
		level = add(tree, i, 0)
	apply_infix(tree, print)

# ex_e()

def ex_f():
	def add(root, n, level):
		if root[0] == None:
			root[0] = n
			return level + 1
		elif root[0] == n:
			return None
		elif root[0] > n:
			if root[1] == None:
				root[1] = [None, None, None]
			return add(root[1], n, level + 1)
		elif root[0] < n:
			if root[2] == None:
				root[2] = [None, None, None]
			return add(root[2], n, level + 1)

	def apply_infix(root, f):
		if root != None:
			apply_infix(root[1], f)
			if root[0] != None and root[1] != None and root[2] != None:
				f(root[0])
			apply_infix(root[2], f)

	nums = list(map(int, input().split()))
	tree = [None, None, None]
	for i in nums:
		if i == 0:
			break
		level = add(tree, i, 0)
	apply_infix(tree, print)

# ex_f()

def ex_g():
	def add(root, n, level):
		if root[0] == None:
			root[0] = n
			return level + 1
		elif root[0] == n:
			return None
		elif root[0] > n:
			if root[1] == None:
				root[1] = [None, None, None]
			return add(root[1], n, level + 1)
		elif root[0] < n:
			if root[2] == None:
				root[2] = [None, None, None]
			return add(root[2], n, level + 1)

	def apply_infix(root, f):
		if root != None:
			apply_infix(root[1], f)
			# if root[0] != None and (root[1] != None and root[2] == None or root[1] == None and root[2] != None):
			if bool(root[0]) & (bool(root[1]) ^ bool(root[2])):
				f(root[0])
			apply_infix(root[2], f)

	nums = list(map(int, input().split()))
	tree = [None, None, None]
	for i in nums:
		if i == 0:
			break
		level = add(tree, i, 0)
	apply_infix(tree, print)

# ex_g()

def ex_h():
	def add(root, n, level):
		if root[0] == None:
			root[0] = n
			return level + 1
		elif root[0] == n:
			return None
		elif root[0] > n:
			if root[1] == None:
				root[1] = [None, None, None]
			return add(root[1], n, level + 1)
		elif root[0] < n:
			if root[2] == None:
				root[2] = [None, None, None]
			return add(root[2], n, level + 1)

	def height(root):
		if root == None or root[0] == None:
			return 0
		if root[1] == None and root[2] == None:
			return 1
		if root[1] == None and root[2] != None:
			return 1 + height(root[2])
		elif root[1] != None and root[2] == None:
			return 1 + height(root[1])
		else:
			return 1 + max(height(root[1]), height(root[2]))

	def apply_infix(root, f):
		if root != None:
			result = apply_infix(root[1], f)
			if result != None:
				return result
			if abs(f(root[1]) - f(root[2])) > 1:
				return('NO')
			return apply_infix(root[2], f)

	nums = list(map(int, input().split()))
	tree = [None, None, None]
	for i in nums:
		if i == 0:
			break
		level = add(tree, i, 0)
	if apply_infix(tree, height) == None:
		print('YES')
	else:
		print('NO')

ex_h()
