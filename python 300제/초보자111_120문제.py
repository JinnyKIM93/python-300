# 파이썬 분기문(111-120)
# user = input("입력:")
# print(user * 2)
#
# num = input("숫자를 입력하세요:")
# print(int(num) + 10)
# # print에서 num + 10 사용하면 오류가 뜬다.
#
# num = input("짝수? 홀수? :")
# if int(num) % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")
#
# num = input("입력값:")
# num_ = 20 + int(num)
# if num_ > 255:
#     print(255)
# else:
#     print(num_)
#
# nums = input("입력값:")
# num = int(nums) - 20
# if num > 255:
#     print(255)
# elif num < 0:
#     print(0)
# else:
#     print(num)
#
# time = input("현재시간: ")
# if time[-2:] == "00":
#     print("정각입니다.")
# else:
#     print("정각이 아닙니다.")
#
#
# fruit = ["사과", "포도", "홍시"]
# data = input("좋아하는 과일은?")
# if data in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")
#
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao",
#                         "SANSUNG", "LG"]
# list_ = input("종목명:")
# if list_ in warn_investment_list:
#     print("투자 경고 종목 입니다.")
# else:
#     print("투자경고 종목이 아닙니다.")
#
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# season = input("내가 좋아하는 계절은?")
# if season in fruit.keys():
#     print("정답입니다.")
# else:
#     print("오답입니다.")
#
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# season = input("내가 좋아하는 계절은?")
# if season in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")