# 함수를 사용하는 이유 

# 함수를 사용하지 않은 경우
print("안녕하세요. 수경님")
print("현재 프리미엄 서비스 사용기간이 30일 남았습니다.")

print("안녕하세요. 레디님")
print("현재 프리미엄 서비스 사용기간이 17일 남았습니다.")

print("안녕하세요. 규동님")
print("현재 프리미엄 서비스 사용기간이 7일 남았습니다.")

# 함수를 사용한 경우 
def printMessage(name, data):
    print("안녕하세요. ", name, "님")
    print("현재 프리미엄 서비스 사용긴간이 ", data, "일 남았습니다.")

printMessage("수경", 30)
printMessage("레디", 17)
printMessage("규동", 7)