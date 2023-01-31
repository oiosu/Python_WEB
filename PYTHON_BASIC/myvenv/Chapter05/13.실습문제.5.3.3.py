# 실습문제 5.3.2'
# 성민은 패스트대학교에 liLy라는 이름의 교환학생과 친해지게 되었다. 
# 영어를 잘하지 못했던 성미은, Lily에게 한국어를 가르쳐주기 위해 한국어 연습 프로그램을 만들게 되었다. 
# ----------- Learning Korean -------------------
# 1. 연습할 한국어가 담긴 리스트를 만든다. 
# 2. 리스트 순서대로 단어를 가져와 화면에 출력한다. 
# 3. 프로그램 사용자는 단어를 그대로 입력하고 
# 4. 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료



# 내가 푼 문제 
# korean = ["한복", "불고기", "냉면", "경북궁", "떡볶이"]

# print(korean)
# word = input("단어를 입력해주세요 >>>")

# for i in word:
#     if i == word[i]:
#         print(word(input))
#     else:
#         break

# ======================================================

# learning = input("Let's Learning Korean")
# for i in korean:
#     print(input(korean[0]))



# 최종 답안 

# 한국어 리스트
word_list = ["사랑해", "귀여워", "고마워", "행복해"]

print("Let's Learning Korean")
# 1개이니깐 word 단수형
for word in word_list:
    # 명령 실행 
    print(word) 
    data = input() # 공백 > 입력할때까지 기다려주기 
    if data != word: # 같지 않다면 break 같다면 계속 이어짐 
        break 


# _____응용________

# 전체 문제 개수 : 4개 
# 맞힌 문제 개수 : 2개 
# 틀린 문제 개수 : 2개 


