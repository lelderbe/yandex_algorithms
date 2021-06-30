def ex_a():
	n, m = list(map(int, input().split()))
	events = []
	for _ in range(m):
		b, e = list(map(int, input().split()))
		events.append((b, -1))
		events.append((e, 1))
	events.sort()
	count = 0
	watchers = 0
	for i in range(len(events)):
		if watchers > 0:
			count = count + events[i][0] - events[i - 1][0]
		if events[i][1] == -1:
			watchers += 1
		elif events[i][1] == 1:
			watchers += -1
		if watchers == 0:
			count += 1
	return(n - count)

# print(ex_a())

def ex_b():
	n, m = list(map(int, input().split()))
	events = []
	for _ in range(n):
		a, b = list(map(int, input().split()))
		events.append((min(a, b), -1))
		events.append((max(a, b), 1))
	dots = list(map(int, input().split()))
	for x in dots:
		events.append((x, 0))
	events.sort()
	# print(dots)
	# print(events)
	count = 0
	ans = {}
	for event in events:
		if event[1] == -1:
			count += 1
		elif event[1] == 1:
			count -= 1
		elif event[1] == 0:
			ans[event[0]] = count
	# print(ans)
	result = []
	for i in dots:
		result.append(ans[i])
	return(result)

# print(*ex_b())

def ex_c():
	def get_ticket(tickets, last):
		for i in range(last, len(tickets)):
			if tickets[i] == 0:
				# tickets[i] = 1
				return(i)
		return(-1)

	n, d = list(map(int, input().split()))
	events = []
	coords = list(map(int, input().split()))
	for x in coords:
		events.append((x, -1))
		events.append((x + d, 1))
	events.sort()
	# print(coords)
	# print(events)
	count = 0
	max_count = 0
	for event in events:
		if event[1] == -1:
			count += 1
		elif event[1] == 1:
			count -= 1
		max_count = max(max_count, count)
	print(max_count)
	tickets = [0] * (max_count + 1)
	ticket = 1
	last = 1
	map1 = {}
	ans = {}
	for event in events:
		if event[1] == -1:
			# ticket, last = get_ticket(tickets, last)
			map1[event[0]] = ticket
			ans[event[0]] = ticket
			tickets[ticket] = 1
			ticket = get_ticket(tickets, ticket + 1)
		elif event[1] == 1:
			last = map1[event[0] - d]
			tickets[last] = 0
			del map1[event[0] - d]
			if ticket == -1 or ticket > last:
				ticket = last
		# print(map1)
		# print(tickets)
		# print(ticket)
	result = []
	for i in coords:
		result.append(ans[i])
	return(result)

print(*ex_c())
