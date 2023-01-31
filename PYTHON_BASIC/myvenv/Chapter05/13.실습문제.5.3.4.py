# _____응용________

# 전체 문제 개수 : 4개 
# 맞힌 문제 개수 : 2개 
# 틀린 문제 개수 : 2개 



# 한국어 리스트
word_list = ["사랑해", "귀여워", "고마워", "행복해"]

# 점수 
score = 0

print("Let's Learning Korean")
# 1개이니깐 word 단수형
for word in word_list:
    # 명령 실행 
    print(word) 
    data = input() # 공백 > 입력할때까지 기다려주기 
    if data == word: # 문제를 맞힌 경우
        score += 1 # 점수를 1를 증가

print("전체 문제 개수 : ", len(word_list))
print("맞힌 개수 : ", score)
print("틀린 개수 : ", len(word_list) - score)