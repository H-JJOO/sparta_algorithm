class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # None은 NULL과 같아요


# # 3을 가진 Node 를 만드려면 아래와 같이 하면 됩니다!
# node = Node(3)  # 현재는 next 가 없이 하나의 노드만 있어요!


# 주의할 점은 노드를 만들 때 next까지 세팅을 하는 것이 아니에요!
# 이것은 링크드리스트 자료구조 클래스에서 해주는 역할인 것을 인지하셔야 합니다!

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)  # head 에 시작하는 Node 를 연결합니다.

    def append(self, value):  # LinkedList 가장 끝에 있는 노드에 새로운 노드를 연결합니다.
        curr = self.head
        while curr.next is not None:  # curr의 다음이 끝에 갈 때까지 이동합니다.
            curr = curr.next
        curr.next = Node(value)

    def get_node(self, index):  # 원래 강의노트에 작성된 코드를 그대로 가져왔어요!

        node = self.head  # 링크드리스트의 Head를 처음 노드로 지정합니다!

        curr_idx = 0  # 현재 순회하고 있는 index를 나타냅니다!
        # 현재 순회하고 있는 index가 원하는 위치보다 작다면 계속 루프를 돌아요!
        while curr_idx < index:
            # if node.next is None:
            #     print('올바른 인덱스를 입력하세요')
            #     return
            try:
                node = node.next  # 원하는 위치에 당도할 때 까지 다음 노드로 이동!
                curr_idx += 1  # 인덱스도 갱신!
            except:
                print('올바른 인덱스를 입력하세요')
                quit()

        return node  # 원하는 인덱스의 노드를 리턴해요!

    def add_node(self, index, value):
        new_node = Node(value)  # 일단 새로운 값을 기준으로 새 노드를 만들어요!
        if index == 0:  # 0번째에 추가를 하고 싶다면!
            new_node.next = self.head  # 원래 Head였던 노드를 새 노드의 next로 지정해요!
            self.head = new_node  # 그리고, Head를 새 노드로 바꾸어줍니다!
            return
        try:
            # [3] - [4] - [5]에서 [3] - [4] - [6] - [5]로 6을 중간에 넣는다고 할게요!
            # 추가하고 싶은 index의 이전 노드 정보를 갖고옵니다! 여기선 [4] 입니다.
            node = self.get_node(index - 1)
            # 1. 이전 노드([4])의 포인터([5])를 next_node로 임시 저장해요!
            next_node = node.next
            # 2. 이전 노드([4])의 포인터를 [6]으로 지정합니다!
            node.next = new_node
            # 3. 새로 삽입한 노드([6])의 포인터를 next_node인 [5]으로 지정합니다!
            new_node.next = next_node
        except:
            print('올바른 인덱스를 입력해주세요')
            quit()

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next

    def print_all(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next


linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)

linked_list.add_node(4, 1)

linked_list.delete_node(2)

linked_list.print_all()
