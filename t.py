from singly_linked_list import singly_linked_list


def ft_aid(lst, k):
	res = None

	for i in range(lst.length()):
		if (i + 1) % k:
			if res == None:
				res = singly_linked_list(lst.get(i).data)
			else:
				res.add_last(lst.get(i).data)
	return res

def ft_aid2(lst, n):
	return singly_linked_list(lst.get(lst.length()//2).data)

def ft_aid3(lst, key):
	res = 0
	while lst:
		if lst.data == key:
			res += 1
		lst = lst.next
	return res

lst = singly_linked_list(1)

for i in range(2, 7):
	lst.add_last(i)

print()

aid = ft_aid2(lst, 2)

while aid:
	print(aid.data)
	aid = aid.next
