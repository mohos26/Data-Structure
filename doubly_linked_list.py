# 22.01.2025


class doubly_linked_list:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

	def _check(self, i):
		if i < 0 or i >= self.length():
			raise IndexError("Index out of range")

	def find(self, data):
		current = self
		aid = 0
		while current != None:
			if current.data == data:
				return aid
			current = current.next
			aid += 1
		return -1

	def last_node(self):
		current = self
		while current.next != None:
			current = current.next
		return current

	def first_node(self):
		current = self
		while current.prev != None:
			current = current.prev
		return current

	def get(self, i):
		self._check(i)
		aid = 0
		current = self
		while aid != i:
			current = current.next
			aid += 1
		return current

	def length(self):
		length = 0
		current = self
		while current:
			current = current.next
			length += 1
		return length

	def merge(self, node):
		aid = self.last_node()
		aid.next = node
		node.prev = aid

	def add_last(self, data):
		self.merge(doubly_linked_list(data))

	def copy(self):
		res = doubly_linked_list(self.data)
		current = self.next
		while current != None:
			res.add_last(current.data)
			current = current.next
		return res

	def add_beginning(self, data):
		aid = doubly_linked_list(data)
		copy = self.copy()
		self.data = aid.data
		self.prev = None
		self.next = copy
		copy.prev = self

	def add_in(self, data, i):
		self._check(i)
		if i == 0:
			self.add_beginning(data)
		else:
			aid = self.get(i)
			aid2 = doubly_linked_list(data)
			aid2.prev = aid.prev
			aid2.next = aid
			aid.prev = aid2
			self.get(i-1).next = aid2

	def del_last(self):
		if self.last_node().prev == None:
			self.data = None
		else:
			self.last_node().prev.next = None

	def del_beginning(self):
		if self.next == None:
			self.data = None
		else:
			aid = self.next
			self.data = aid.data
			self.next = aid.next

	def del_in(self, i):
		self._check(i)
		if i == 0:
			self.del_beginning()
		else:
			aid = self.get(i)
			aid.prev.next = aid.next
