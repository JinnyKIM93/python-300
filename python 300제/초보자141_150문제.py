# 파이썬 반복문(141-150)
# list = [100, 200, 300]
# for 부가세 in list:
#     print(부가세 + 10)  #list에 10을 더해서 출력 가능
#
# menu = ["김밥", "라면", "튀김"]
# for 메뉴 in menu:
#     print("오늘의 메뉴: ", 메뉴)
#
# list = ['SK하이닉스', '삼성전자', 'LG전자']
# for stock in list:
#     length = len(stock)
#     print(length)
#
# list = ['dog', 'cat', 'parrot']
# for animal in list:
#     length = len(animal)
#     print(animal, length)
#     # print(animal, len(anumal))
#
# list = ['dog', 'cat', 'parrot']
# for animal in list:
#     print(animal[0])  #이름 앞자리만 출력
#
# list = [1, 2, 3]
# for A in list:
#     # print("3 x" + str(A))  #문자니까 'str' 쓰기
#     print('3 x',+ A)
#
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for 변수 in list:
#     print("9 x", + 변수, "=", 9*변수)  #구구단 만들기
#
# list = ['가', '나', '다', '라']
# for 한글 in list[1:]: #'가'를 빼고 출력하는 법
#     print(한글)
#
# list = ['가', '나', '다', '라']
# for a in list[::2]:  #리스트 슬라이싱에서 [시작:끝:증감폭]
#     print(a)
#
# list = ['가', '나', '다', '라', '마', '바']
# for a in list[::-1]: #리스트 슬라이싱 [시작:끝:증감폭] 에서 증감폭을 음수로 하면 끝부터 출력
#     print(a)