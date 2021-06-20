def ex_a():
	n = int(input())
	words = {}
	for i in range(n):
		w1, w2 = list(map(str, input().split()))
		words[w1], words[w2] = w2, w1
	return words[input()]

# print(ex_a())

import sys

def ex_b():
	map1 = {}
	for line in sys.stdin:
		for word in line.split():
			if word not in map1:
				map1[word] = 0
			map1[word] += 1
			print(map1[word] - 1, end=' ')

# ex_b()

import sys

def ex_c():
	result_str = None
	result_max = 0
	map1 = {}
	for line in sys.stdin:
		for word in line.split():
			if word not in map1:
				map1[word] = 0
			map1[word] += 1
			if map1[word] == result_max:
				if result_str > word:
					result_str = word
			if map1[word] > result_max:
				result_max = map1[word]
				result_str = word
	return result_str

# print(ex_c())

def ex_d():
	n = int(input())
	keys = list(map(int, input().split()))
	k = int(input())
	for key in list(map(int, input().split())):
		keys[key - 1] = keys[key - 1] - 1
	for i in range(n):
		if (keys[i] < 0):
			print('YES')
		else:
			print('NO')

# ex_d()

def ex_e():
	n = int(input())
	map1 = {}
	for i in range(n):
		w, h = list(map(int, input().split()))
		if w not in map1 or map1[w] < h:
			map1[w] = h
	count = 0
	for key in map1:
		count = count + map1[key]
	return count

# print(ex_e())

import sys

def ex_f():
	customers = {}
	for line in sys.stdin:
		customer, goods, count = list(map(str, line.split()))
		if customer not in customers:
			customers[customer] = {}
		if goods not in customers[customer]:
			customers[customer][goods] = 0
		customers[customer][goods] += int(count)
	for customer in sorted(customers.keys()):
		print(customer, end=':\n')
		for goods in sorted((customers[customer]).keys()):
			print(goods, customers[customer][goods])

# ex_f()

import sys

def ex_g():
	clients = {}

	def deposit(client, value):
		# print('DEPO', client, value)
		if client not in clients:
			clients[client] = 0
		clients[client] += value

	def withdraw(client, value):
		if client not in clients:
			clients[client] = 0
		clients[client] -= value

	def transfer(client_from, client_to, value):
		withdraw(client_from, value)
		deposit(client_to, value)

	def income(value):
		for client in clients:
			if clients[client] > 0:
				clients[client] += (clients[client] * value // 100)

	def balance(client):
		if client in clients:
			print(clients[client])
		else:
			print('ERROR')

	for line in sys.stdin:
		data = line.split()
		# print(data)
		if data[0] == 'DEPOSIT':
			deposit(data[1], int(data[2]))
		if data[0] == 'WITHDRAW':
			withdraw(data[1], int(data[2]))
		if data[0] == 'TRANSFER':
			transfer(data[1], data[2], int(data[3]))
		if data[0] == 'BALANCE':
			balance(data[1])
		if data[0] == 'INCOME':
			income(int(data[1]))

ex_g()

