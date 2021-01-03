"""
Linked List Definition:
A data simple data structure that represents a sequence of nodes. In a single linked list each node points to the next node in the linked list. As a result, unlike an array a linked list does not  provide constant time access to a particular "index" within the list. This means that if you'd like to find the "Kth" element  you will need to iterate through "K" elements.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def add_first(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def add_last(self, new_node):
        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("Linked List Is Empty")

        current_node = self.head
        while current_node is not None:
            if current_node.data == target_node_data:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

        raise Exception(f"Target Node Data Not Found: {target_node_data}")

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        previous_node = self.head
        current_node = previous_node.next
        while current_node is not None:
            if current_node.data == target_node_data:
                previous_node.next = new_node
                new_node.next = current_node
                return
            previous_node = current_node
            current_node = current_node.next

        raise Exception(f"Target Node Data Not Found: {target_node_data}")

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("Linked List Is Empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        current_node = previous_node.next
        while current_node is not None:
            if current_node.data == target_node_data:
                previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next

        raise Exception(f"Target Node Data Not Found: {target_node_data}")

    def node_count(self):
        node = self.head
        node_count = 0
        while node is not None:
            node_count += 1
            node = node.next
        return node_count

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


"""
Problem Set: Assume you have a single linked list:

n1 >> n2 >> n3 >> ... n(k-1) >> n(k)

Write an algorithm to rearrange the single linked list in the following format so that good performance (min cost + fastest speed):

n1 >> n(k) >> n2 >> n(k-1)...
"""
from collections import deque


def solve(node_llist):
    if not node_llist.head:
        raise Exception("Linked List Is Empty")

    nodes = deque()
    node = node_llist.head
    while node is not None:
        nodes.append(node.data)
        node = node.next

    rearranged = LinkedList()
    while len(nodes) > 1:
        min_node = Node(data=nodes.popleft())
        max_node = Node(data=nodes.pop())
        rearranged.add_last(new_node=min_node)
        rearranged.add_last(new_node=max_node)
        if len(nodes) == 1:
            rearranged.add_last(new_node=Node(nodes.pop()))
    return rearranged


if __name__ == "__main__":
    node_list = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p".split(",")
    llist = LinkedList(nodes=node_list)
    print(f'<Problem Set> Starting Linked List: ', llist)

    answer = solve(node_llist=llist)
    print(f'\nAnswer> Rearranged Linked List: ', answer)