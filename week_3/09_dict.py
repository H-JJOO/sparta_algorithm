class Dict:
    def __init__(self):
        self.items = [None] * 8

    # 딕셔너리에 새로운 key 와 value 를 추가
    def put(self, key, value):
        index = hash(key) % len(self.items) # key 를 해싱해서 임의의 문자열로 만들고 그 값을 현재 배열의 최대 길이로 % 연산

        self.items[index] = value
        return

    # key 값에 따른 value 값을 얻기 월하는 메소드
    def get(self, key):
        index = hash(key) % len(self.items)  # key 를 해싱해서 임의의 문자열로 만들고 그 값을 현재 배열의 최대 길이로 % 연산
        return self.items[index] # key 로 이용해서 반환


my_dict = Dict()
my_dict.put("test", 3) # test 를 key 값으로 3 을 value 에 저장하고
print(my_dict.get("test")) # test 라는 key 값으로 value 가져와 출력