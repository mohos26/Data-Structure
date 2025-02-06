# 06.02.2024

class queue:
	def __init__(self, size):
		self._size = size
		self._lst = [None] * size
		self._is_empty = True
		self._is_full = False
		self._front = 0
		self.peek = self.front

	def enqueue(self, data):
		self._lst = [data] + self._lst[:-1]
		if not self._is_full:
			self._front += 1
			self._is_empty = False
			self._is_full = (self._size -1) == self._front

	def dequeue(self):
		aid = self._lst[self._front]
		self._lst[self._front] = None
		self._is_full = False
		self._is_empty = not self._front
		return aid

	def front(self):
		return self._lst[self._front]

	def rear(self):
		return self._lst[0]

	def is_empty(self):
		return self._is_empty

	def is_full(self):
		return self._is_full

	def length(self):
		return self._size
