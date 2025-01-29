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
		self.data = data
		self.next = circular_singly_linked_list(data)
		self.merge(copy)

	def find(self, data):
		pass

	def get(self, i):
		pass


node1 = circular_singly_linked_list("q")

for i in "qaxchjiop":
	node1.add_last(i)


Node1 = circular_singly_linked_list("gg")
Node2 = circular_singly_linked_list("dd")
Node3 = circular_singly_linked_list("ss")
Node4 = circular_singly_linked_list("ww")



Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node1

node1.merge(Node1)

print(node1)
print(node1.copy())

print("->", node1.length())
print("->", node1.last_node().data)

aid = node1

while True:
	print(aid.data)
	aid = aid.next
	if aid == node1:
		break
