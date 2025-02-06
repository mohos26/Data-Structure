# 23.01.2025


class circular_singly_linked_list:
	def __init__(self, data):
		self.data = data
		self.next = self

	def length(self):
		current, length = self, 1
		while current.next != self:
			current = current.next
			length += 1
		return length

	def last_node(self):
		current = self
		while current.next != self:
			current = current.next
		return current

	def merge(self, node):
		node.last_node().next = self
		self.last_node().next = node

	def add_last(self, data):
		self.merge(circular_singly_linked_list(data))

	def copy(self):
		res = circular_singly_linked_list(self.data)
		current = self.next
		while current != self:
			res.add_last(current.data)
			current = current.next
		return res

	def add_beginning(self, data):
		copy = self.copy()
		copy.last_node().next = self
		self.data = data
		self.next = copy

	def find(self, data):
		aid = 0
		current = self
		while current.data != data:
			current = current.next
			aid += 1
			if current == self:
				break
		if current != self:
			return aid
		return -1

	def get(self, i):
		aid = 0
		current = self
		while aid != i:
			current = current.next
			aid += 1
		return current

	def del_last(self):
		pass

	def del_beginning(self):
		pass

	def del_in(self, i):
		pass

	def add_in(self, i):
		pass
