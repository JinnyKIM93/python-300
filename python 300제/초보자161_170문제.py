# 파이썬 반복문(161-170)
# for i in range(10):
#     print(i)
#
# for i in range(2002, 2052, 4):
#     print(i)
#
# for i in range(3, 31, 3):
#     print(i)
#
# for i in range(10):
#     print(9-i)
#
# for i in range(10):
#     print(i / 10)
#
# for i in range(10):
# # (1, 10)으로 들어가면 1부터 출력, 10으로 넣으면 0부터 출력
#     print(3, "x", i, "=", 3 * i)
#
# for i in range(1, 10, 2):
# #(3, 10, 3)으로 넣으면 3의 배수만, (0,10,2)넣으면 짝수
#     print(3, 'x', i, '=', 3 * i)
# #조건문으로 만들기
# num = 3
# for i in range(1, 10):
#     if i % 2 == 1:
#         print(num, 'x', i, '=', num*i)
#
# sum_ = 0
# for i in range(1, 11):
#     sum_ += i  # sum_= sum_ + i 코드 축약 한 것
# print("합:", sum_)
#
# sum_ = 0
# for i in range(1, 10, 2):
#     # print(i)
#     sum_ += i
# print(sum_)
#
# s = 1  #곱하기라서 0으로 두면 결과값이 0으로 나온다.
# for i in range(1, 11):
#     # print(i)
#     S = s * i
# print(S)