#변수 사용(11-20)
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print("총 평가 금액 : ", 총평가금액)

시가총액 = '298조'
현재가 = '50,000원'
PER = 15.97
print('시가총액:', 시가총액,
      '현재가:', 현재가,
      'PER:', PER)

s = "Hello"
t = "Python"
print(s+'!', t)

s = 2 + 2 * 3
print(s)

a = 128
print(type(a))   # <class 'int'>
A = "132"
print(type(A))     # <class 'str'>

num_str = "720"
num_int = int(num_str)  # str -> int 변경
#num_int 라는 변수를 지정해서 int로 변환
print(num_int, type(num_int))

data = "15.79"  #문자열로 입력한 "15.79"를 float 변환
data = float(data)   # 위에서 변환한 것과 같은 방법으로!
print(data, type(data))

year = "2020"
Year = int(year)
print(Year+1, Year+2, Year+3)
#다른 방식으로, 변수 없이 바로 print에서 지정하고 출력 할 수 있다
print(int(year)-1)
print(int(year)-2)
print(int(year)-3)
print(int(year)+3)

DATA = 48584
A = DATA * 36
print("에어컨 가격:", A)