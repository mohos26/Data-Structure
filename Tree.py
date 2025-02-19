# 13.02.2025


import weakref

class Tree:
	def __init__(self, data):
		self.data = data
		self.children = {}  # Use a dictionary for fast lookups
		self.parent = None  # Weak reference can be used

	def __repr__(self):
		return f"Tree({self.data})"

	def is_root(self):
		return self.parent is None

	def add_edge(self, data):
		"""Adds a child node only if it doesn't already exist."""
		if data not in self.children:
			child = Tree(data)
			child.parent = weakref.ref(self)  # Use a weak reference
			self.children[data] = child
		return self.children[data]  # Return child for chaining

	def search_child(self, data):
		"""O(1) lookup for a child."""
		return self.children.get(data, None)

	def remove_child(self, data):
		"""Removes a child node if it exists."""
		if data in self.children:
			del self.children[data]  # Remove from dictionary

root = Tree(12)

root.add_edge(8)
root.add_edge(18)

root.search_child(8).add_edge(5)
root.search_child(8).add_edge(11)

print(aid(root))
