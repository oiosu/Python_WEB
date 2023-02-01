# 딕셔너리 
# : 사전 형태의 자료형 

stock_a = {"삼성전자" : 82000, "lg전자" : 15000}

stock_b = {
    "삼성전자" : [81000, 30000, 40000, 50300, 34533],
    "lg전자" : (45222, 33333, 74444, 456345)
}

# 중첩 딕셔너리
stock_c = {
    "삼성전자" : {
        "현재가" : 56999, 
        "보유수량" : 5, 
        "매수단가" : 340000, 
    }
}

# ail+shift 
# print(stock_a)
# print(stock_b)
# print(stock_c)

# 딕셔너리 접근하기 
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])


# 딕셔너리 할당하기 
stock_a["삼성전자"] = 45000
print(stock_a)

# 딕셔너리 삭제하기 
del stock_a["lg전자"]
print(stock_a)

# 딕셔너리 함수 
stock_d = {
    "삼성전자" : 45000, 
    "sk하이닉스" : 34555,
    "NAVER" : 342222,
    "카카오" : 342342
}

# items() : 키와 데이터 쌍
print(stock_d.items())

# for 문과 결합 
for item in stock_d.items():
    print(item) #튜플 형태로 키와 데이터 값을 확인할 수 있다. 
    print(item[1])

# key() : 키
for key in stock_d.keys():
    print(key) #키만 출력

# values() : 데이터
for value in stock_d.values():
    print(value) #데이터만 출력