# 실습문제 5.2.2

# 빈 리스트 생성 
data = []

x = int(input("1일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("2일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("3일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("4일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("5일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("6일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("7일차 턱걸이 횟수 >>>"))
data.append(x)

# 인덱스를 이용하여 합하기 
total = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6]

# 평균 구하기 
avg = total /7
# 실수형이 아닌 정수형으로 출력되기 위해 int 포함 
print(int(avg))

# indexerror : list index out of range 오류 
# => 인덱스가 범위에 벗어나다. 
# => 자주 나타나는 오류 


# x = int(input("1일차 턱걸이 횟수 >>>"))
# data.append(x)
# 1일차 라는 것 외에 코드가 반복 되기 때문에 이를 줄이기 위해 반복문을 배울 예정