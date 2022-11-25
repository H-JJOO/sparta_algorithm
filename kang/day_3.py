class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack

class Stack:
    def __init__(self):
        self.head = None

    # 맨 위에 데이터 넣기
    def push(self, value):
        if self.head is None:
            return "Stack is empty"
        new_head = Node(value)  # 새로운 노드 생성
        new_head.next = self.head  # 기존 head 노드를 head.next 로 이동
        self.head = new_head  # head 노드에 새로운 노드 대입

    # 맨 위의 데이터 보기 및 삭제
    def pop(self):  # 가장 위에서 뽑은 데이터를 반환해줘야함
        if self.head is None:  # 만약 비어있다면
            return "Stack is empty"  # 메세지 리턴 말고 None 리턴
        delete_head = self.head  # 제거할 node 를 변수에 대입, 반환위해서
        self.head = self.head.next  # head 를 현재 head 의 다음으로 대입
        return delete_head  # 반환

    # 가장 꼭대기 있는 데이터 보기
    def peek(self):
        if self.head is None:
            return None
        # 위의 리턴 코드는 좋지 않아요.
        # 예외를 던지는 것도 아닌데다가 본인이 메시지를 결정해요!
        # 스택이 비어있을 때 나오는 메시지를 결정하는 것은 이 함수 호출부가 해야해요!
        # 따라서, 이 때는 return None으로 None을 던지고 호출부를 아래처럼 작성해요!

        ### peek() 호출부 시작
        # top = stack.peek()
        # if top is None:
        #   print("Stack is empty!")
        #   ...
        ### peek() 호출부 끝
        return self.head.data

    # 스택이 비었는지 안 비었는지 여부
    def is_empty(self):
        return self.head is None


# stack = Stack()
# stack.push(3)
# print(stack.peek())
# stack.push(4)
# print(stack.peek())
# # print(stack.pop().data)
# print(stack.peek())
# print(stack.is_empty())
# print(stack.pop().data)
# print(stack.is_empty())

# Queue

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # 맨 뒤에 데이터 추가
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None: # 비어있다면
            self.head = new_node # head에 new_node
            self.tail = new_node # tail에 new_node 대입
            return

        # 비어있지 않다면 기존 tail에 새 노드를 포인터로 연결
        self.tail.next = new_node
        # 새 노드를 tail 로 설정
        self.tail = new_node

    # 맨 위의 데이터 뽑기
    def dequeue(self):
        if self.head is None:
            return None
        delete_head = self.head # 제거할 node 를 변수에 대입
        self.head = self.head.next # head를 현재 head 의 다음걸로 대입
        return delete_head # 제거할 node 반환


    # 맨 위의 데이터 보기
    def peek(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    # 큐가 비었는지 안 비었는지 여부 반환
    def is_empty(self):
        return self.head is None


# queue = Queue()
# queue.enqueue(3)
# print(queue.peek())
# queue.enqueue(4)
# print(queue.peek())
# queue.enqueue(5)
# print(queue.peek())
# print(queue.dequeue())
# print(queue.peek())
# print(queue.is_empty())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.is_empty())

