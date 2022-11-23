class Person:
    def __init__(self, param_name):
        print("i am created! ", self)
        self.name = param_name

    def talk(self):
        print('안녕하세요, 제 이름은', self.name, '입니다.')


person_1 = Person('유재석')  # 생성자
print(person_1.name)
person_1.talk()
print(person_1)  # <__main__.Person object at 0x1090c76d0>
person_2 = Person('박명수')
print(person_2.name)
person_2.talk()
print(person_2)  # <__main__.Person object at 0x1034354f0>

# 연관성 있는 데이터들을 클래스 내에서 관리하면서 다양한 객체를 쉽게 생성하기 위해서는 클래스라는 개념을 잘 이용해야한다.
