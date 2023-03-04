# 파이썬 튜플  튜플은 '()'로 표시 (71-80)
my_varible = ()
print(type(my_varible))

movie_rank = ('닥터스트레인지', '스플릿', '럭키')
print(movie_rank)

number = (1)
print(type(number))
number = (1, )  #하나의 데이터가 저장되는 경우, 아래와 같은 쉼표만 입력
print(type(number))

t = 1, 2, 3, 4
print(type(t))  #tuple, 튜플은 괄호랑 함께 사용 되지만, 괄호 없이도 동작한다.

t = ('a', 'b', 'c')
#t[0] = 'A' -> 이와 같은 코드는 동작하지않는다, 튜플은 값 변경이 어렵기 때문에
T = ('A', 'b', 'c')
print(T)

interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)  #list로 변경하는 것
print(data)

interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
print(data)

temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

data = tuple(range(0, 10, 2))   #0부터 10까지 짝수만 저장하기
print(data)
