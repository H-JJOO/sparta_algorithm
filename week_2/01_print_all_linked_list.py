class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)  # head 에 시작하는 Node 를 연결

    def append(self, data):
        if self.head is None:  # head 의 값이 Node 일때
            self.head = Node(data)  # self.head 에 새로운 데이터 추가
            return  # 함수 종료

        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next



linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)

linked_list.print_all()