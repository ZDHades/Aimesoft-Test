# Question 3: Assume you have a single linked list:

# n1 >> n2 >> n3 >> ... n(k-1) >> n(k)

# Write an algorithm to rearrange the single linked list in the following format so that good performance (min cost + fastest speed):

# n1 >> n(k) >> n2 >> n(k-1)...

# Making the Node and Linked List class + methods
class Node:
    def __init__(self, data=None):
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

    def swap_nodes(self, n1_data, n2_data):
        if not self.head:
            raise Exception("Linked List Is Empty")

        node1_found = False
        node2_found = False
        node1_swap = None
        node2_swap = None
        current_node = self.head
        while current_node is not None:
            if current_node.data == n1_data:
                node1_found = True
                node1_swap = current_node

            elif current_node.data == n2_data:
                node2_found = True
                node2_swap = current_node

            if (node1_found and node2_found):
                node1_swap.data, node2_swap.data = node2_swap.data, node1_swap.data
                return None

            current_node = current_node.next
        raise Exception(f"Node(s) Not Found >> n1: {node1_found}, n2: {node2_found}")

    def node_count(self):
        node = self.head
        node_count = 0
        while node is not None:
            node_count += 1
            node = node.next
        return node_count

    def reverse(self):
        if self.head is None:
            raise Exception("Linked List Is Empty")

        reversed_list = LinkedList()
        current_node = self.head
        while current_node is not None:
            reversed_list.add_first(new_node=Node(data=current_node.data))
            current_node = current_node.next
        return reversed_list

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)



if __name__ == "__main__":
    # Define Solver Function
    def solver(linked_list):
        print('\n<Init_Solver>')
        split_left = LinkedList()
        split_index = linked_list.node_count() // 2

        xfer_node = linked_list.head
        for i in range(split_index):
            split_left.add_last(new_node=Node(data=xfer_node.data))
            linked_list.remove_node(target_node_data=xfer_node.data)
            xfer_node = xfer_node.next
        print('<Left Split> ', split_left)
        print('<Right Split> ', linked_list)

        reverse_right = linked_list.reverse()
        print('<Right Split> Reversed: ', reverse_right)
        current_node = split_left.head
        while current_node is not None:
            insert_node = Node(data=reverse_right.head.data)
            split_left.add_after(target_node_data=current_node.data, new_node=insert_node)
            reverse_right.remove_node(target_node_data=insert_node.data)
            current_node = current_node.next.next

        if reverse_right.head is not None:
            split_left.add_last(new_node=Node(data=reverse_right.head.data))
        print('<Merged List> Solution: ', split_left)
        return split_left
        
    # Test Solution
    print('\nQuestion #3 - Single Linked List Algorithm\n')
    node_list = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p".split(",")
    llist = LinkedList(nodes=node_list)
    print(f'<Input> Linked List: ', llist)

    answer = solver(linked_list=llist)
    print(f'<Output> Solution: ', answer)