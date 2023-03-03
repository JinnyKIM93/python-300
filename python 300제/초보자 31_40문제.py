# 문자열 인덱싱 2(31-40)
# a = "3"
# b = "4"
# print(a + b)  #문자열 자체로 34 로 나온다.
# A = 3
# B = 4
# print(A + B) # 문자열이 아니 int 로 쓰면 7이라는 결과값이 나온다.
#
# print("HI " * 3) # 당연히 HI 3번 나오겠지?
#
# print("-" * 30)
#
# t1 = 'python'
# t2 = 'java'
# t3 = t1+ ' ' + t2+ ' '
# # print((t1 + t2)* 4)
# print(t3 * 4)
#
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름: ", name1,
#       "나이: ", age1 )
# print("이름: ", name2,
#       "나이: ", age2)
# print("이름: %s 나이: %d" % (name1, age1))
# print("이름: %s 나이: %d" % (name2, age2))
#
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름 : {} 나이 : {}".format(name1, age1),
#       "이름 : {} 나이 : {}".format(name2, age2))
#
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print(f"이름 : {name1}, 나이 : {age1}")
# print(f"이름 : {name2}, 나이 : {age2}")
#
# A = "5,969,782,550"
# 상장_주식수 = A.replace(',' , '')
# 상장주식수 = int(상장_주식수)
# print("상장주식수:", 상장주식수, type(상장주식수))
# #다른방식
# 상장주식수 = "5,454,367,212"
# 컴마제거 = 상장주식수.replace(",", "")
# 타입변환 = int(컴마제거)
# print(타입변환, type(타입변환))
#
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])
#
# data = "   삼성전자    "
# data1 = data.strip()
# print(data1))