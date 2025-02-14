# 13.02.2025


class Tree:
	def __init__(self, data):
		self.data = data
		self.children = []
		self.parent = None

	def is_root(self):
		return self.parent == None

	def add_edge(self, data):
		aid = Tree(data)
		aid.parent = self
		self.children.append(aid)

	def search_child(self, data):
		for node in self.children:
			if node.data == data:
				return node
		return None

# Sells. Shells. Shore.

root = Tree("s")

root.add_edge("h")
root.add_edge("e")

root.search_child("h").add_edge("e")
root.search_child("h").add_edge("o")
root.search_child("e").add_edge("l")
root.search_child("e").add_edge("a")

root.search_child("h").search_child("e").add_edge(".")
root.search_child("e").search_child("l").add_edge("l")
root.search_child("e").search_child("a").add_edge(".")
root.search_child("h").search_child("e").add_edge("l")
root.search_child("h").search_child("o").add_edge("r")

root.search_child("e").search_child("l").search_child("l").add_edge("s")
root.search_child("h").search_child("e").search_child("l").add_edge("l")
root.search_child("h").search_child("o").search_child("r").add_edge("e")

root.search_child("e").search_child("l").search_child("l").search_child("s").add_edge(".")
root.search_child("h").search_child("e").search_child("l").search_child("l").add_edge("s")
root.search_child("h").search_child("o").search_child("r").search_child("e").add_edge(".")

root.search_child("h").search_child("e").search_child("l").search_child("l").search_child("s").add_edge(".")

def aid(node):
	if node.data == ".":
		print()
	else:
		for arg in node.children:
			if node.is_root:
				print(node.data, end="")
			print(arg.data, end="")
			aid(arg)

aid(root)
