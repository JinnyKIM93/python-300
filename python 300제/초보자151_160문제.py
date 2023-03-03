# 파이썬 반복문(151-160)
# list = [3, -20, -3, 44]
# for a in list:
#     if a < 0:  #음수 출력
#         print(a)
#     # if a > 0:   #양수 출력
#     #     print(a)
#
# list = [3, 100, 23, 44, 12, 33, 66, 24]
# for num in list:
#     if num % 3 == 0:
#         print(num)
#
# list = [13, 21, 12, 14, 30, 18]
# for num in list:
#     if num < 20 and num % 3 == 0:
#         print(num)
#
# list = ['I', 'study', 'python', 'language', '!']
# for length in list:
#     if len(length) > 3:
#         print(length)  #리스트에 3글자 이상의 문자 출력
#
# list = ['A', 'b', 'c', 'D', 'E']
# for 변수 in list:
#     if 변수.isupper():  #isupper()는 대문자 여부 판별
#         print(변수)
#
# list = ['A', 'b', 'c', 'D', 'E']
# for 변수 in list:
#     if not 변수.isupper():  #not 붙이면 소문자 출력
#         print(변수)
#
# #소문자1
# list = ['A', 'b', 'c', 'D', 'E']
# for 변수 in list:
#     if 변수.isupper()  != True:
#         print(변수)
# #소문자2
# list = ['A', 'b', 'c', 'D', 'E']
# for 변수 in list:
#     if 변수.isupper()  == False:
#         print(변수)
#
# list = ['dog', 'cat', 'parrot']
# for animal in list:
#     print(animal[0].upper()+animal[1:]) #앞글자만 대문자로 변경하는거니까,
# for animal in list:
#     first = animal[0]
#     B = first.upper()
#     print(B + animal[1:])
#
# list = ['hello.py', 'ex01.py', 'intro.hwp']
# for a in list:
#     s = a.split('.')  #문자열을 분할,
#     print(s[0])  #0번 인덱스만 출력
#
# list = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for list_ in list:
#     split = list_.split('.')
#     # print(split)
#     if split[1] == 'h' or split[1] == 'c':
#         print(list_)