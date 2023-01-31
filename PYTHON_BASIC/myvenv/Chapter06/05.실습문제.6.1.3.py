# 실습문제 6.1.3
# 로또 번호 추출기 

# 로또에 당첨되서 퇴사를 하고 싶었던 김로또는 로또 예상 번호 추출 프로그램을 파이썬으로 작성하려고 한다. 
# 다음 조건에 따라 김로또의 프로그램을 완성해보자. 
# 1. 로또 번호 6개를 생성한다. 
# 2. 로또 번호는 1 ~ 45 까지의 랜덤한 번호다. 
# 3. 6개의 숫자 모두 달라야 한다. 
# getRandomNumber() 함수를 사용해서 구현한다. 
# (random 모듈의 sample 함수는 사용하지 않는다.)

# import random

# def getRandomNumber():
#     number = random.randint(1, 45)
#     return number
# 표준 출력 : 1 8 11 13 26 42

# 반복문, 조건문 사용, 리스트 사용하면 쉽게 구현 가능 

# import random 

# def getRandomNumber():
#     number = random.randint(1, 45)
#     for i in number:
#         if i == 6:
#             return number
        


# 최종 답안 
import random

def get_random_number():
    number = random.randint(1, 45)
    return number

# 로또 번호 리스트에 저장
lotto_num = []

# 숫자 중복이 되어도 상관 없는 프로그래밍 
for i in range(6):
    random_number = get_random_number()
    lotto_num.append(random_number)

lotto_num.sort()
for num in lotto_num:
    print(num, end=" ")


# -------------------------------------------------------
# 숫자 중복되지 않도록 하는 프로그래밍

import random

def get_random_number():
    number = random.randint(1, 45)
    return number

# 로또 번호 리스트에 저장
lotto_num = []

count = 0 # 현재 뽑은 숫자 개수 

# 숫자 중복이 되어도 상관 없는 프로그래밍 
while True:
    if count == 6: # or count > 5:
        break
    random_number = get_random_number()
    # 조건 추가 : 중복이 되는가?
    # random_number에 포함 되어 있지 않다면, lotto_num 리스트에 안쪽 명령문 실행
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count += 1

