class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # 맨 뒤에 데이터 추가
    def enqueue(self, value):
        new_node = Node(value)  # [3] 새로운 노드 생성
        if self.is_empty():  # head, tail 이 None 인지 아닌지에 따른 예외 처리
            self.head = new_node  # 새로운 노드가 들어오면 head 이자
            self.tail = new_node  # tail 이다. 딱 하나만 있으면 head 이자 tail 이다.
            return

        self.tail.next = new_node  # 현재 tail 의 다음 노드가 new_node 로
        self.tail = new_node  # 현재 tail 을 new_node 로 변경

    # 맨 위의 데이터 뽑기
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        delete_head = self.head  # 반환할 사라질 head 값을 다른 변수에 넣어넣고
        self.head = self.head.next  # head 값에 head 의 다음 값을 대입하고
        return delete_head.data  # 기존 head 값 반환

    # 맨 위의 데이터 보기
    def peek(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    # 큐가 비었는지 안 비었는지 여부 반환
    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())

