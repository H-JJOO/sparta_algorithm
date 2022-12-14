class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        cnt = 0
        while cnt < index:
            node = node.next
            cnt += 1
        return node

    # index    next_node
    # ['자갈] ['밀가루'] -> ['우편']
    #          new_node
    #        -> ['흑연'] ->
    # index.next = new_node
    # new_node.next = next_node

    def add_node(self, index, value):
        new_node = Node(value)  # [6]
        if index == 0:
            new_node.next = self.head  # [6] -> [5]
            self.head = new_node # head -> [6] -> [5] -> ...
            return

        new_node = Node(value)  # [6]
        node = self.get_node(index - 1)  # [5]
        next_node = node.next  # [12]
        node.next = new_node  # [5] -> [6]
        new_node.next = next_node  # [6] -> [12]

    # ['자갈] ['밀가루'] -> ['우편']

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return  # 아래 코드가 실행되지 않도록
        node = self.get_node(index - 1)
        node.next = node.next.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.delete_node(0)
linked_list.print_all()
