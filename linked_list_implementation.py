class Node:
	def __init__(self, data): 
		self.data = data
		self.next_node = None

class LinkedList:
	def __init__(self, first_node=None):
		self.first_node = first_node
	def read(self, index): 
		current_node = self.first_node 
		current_index = 0
		while current_index < index:
			current_node = current_node.next_node 
			current_index += 1	
			if not current_node: 
				return None
		return current_node.data		


node_1 = Node("once")
node_2 = Node("upon")
node_3 = Node("a")
node_4 = Node("time")
node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

list = LinkedList(node_1)
