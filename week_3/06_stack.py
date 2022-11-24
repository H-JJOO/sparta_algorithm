class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    # 맨 위에 데이터 넣기
    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # 맨 위의 데이터 보기 및 삭제
    def pop(self): # 가장 위에서 뽑은 데이터를 반환해줘야함
        if self.is_empty():
            return "Stack is Empty"
        delete_head = self.head # 그래서 해드 값을 다른 변수에 저장
        self.head = self.head.next
        return delete_head  # 출력

    # 가장 꼭대기 있는 데이터 보기
    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.head.data

    # 스택이 비었는지 안 비었는지 여부
    def is_empty(self):
        return self.head is None # 비었다면 None 이니까 True 반환


stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop().data)
print(stack.peek())
print(stack.is_empty())
print(stack.pop().data)
print(stack.is_empty())
