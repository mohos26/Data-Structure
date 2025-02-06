# 03.02.2024

from singly_linked_list import singly_linked_list

class stack:
	def __init__(self):
		self.top = None

	def is_empty(self):
		return self.top is None

	def push(self, data):
		if self.is_empty():
			self.top = singly_linked_list(data)
		else:
			self.top.add_beginning(data)

	def pop(self):
		if self.is_empty():
			raise ValueError("Stack is Empty")
		self.top.del_beginning()

	def length(self):
		return self.top.length()

