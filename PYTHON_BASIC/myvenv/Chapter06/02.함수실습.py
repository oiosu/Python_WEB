#기본형 
# 1. 정의하기 
def printHello():
    print("Hello")

# 2. 호출하기 
printHello()

# 3. 매개변수가 있는 함수 
def sum(a, b):
    print(a + b)

# 3은 매개변수 a에 들어가고 
# 4는 매개 변수 b에 들어간다. 
# 매개변수들은 함수 안에서 자유롭게 사용할 수 있다.
sum(3, 4)

# 4. 반환값이 있는 함수 
# 모듈 
import random

def getRandomNumber():
    number = random.randint(1, 10)
    return number # 함수가 끝나고 나서 number라는 값을 가지고 있는 데이터를 반환해주는 것이다. 

print(getRandomNumber())

# 5. 매개변수와 반환값이 있는 함수 
def add(a, b):
    result = a + b
    return result

print(add(5, 6))


