# 문자열 인덱싱1
# letters = 'python'
# print(letters[0],letters[2])  # 어디서 몇번째 글자 출력하는지 쓰기(0부터 시작한다.)
#
# license_plate = "24가 2210"
# #문자열에서 여러글자를 가져오는 것을 '슬라이싱'이라고 한다.
# print(license_plate[-4:]) # -숫자가 들어가면 뒤에서부터 출력되는 것
# print(license_plate[4:])  # 4번째 자리부터 쭉 출력
#
# string = "홀짝홀짝홀짝"
# print(string[0], string[2], string[4])
# print(string[::2])   #[::2] 시작인덱스:끝인덱스:오프셋
#
# string = "PYTHON"
# print(string[::-1])   # [:-1]로 입력시, 뒤로 하나씩 지워지면서 출력
#                       # [::-1] 문자열이 뒤부터 출력
#
# phone_number = "010-123-4567"
# phone_number1 = phone_number.replace("-", ".")  #replace 메서드 사용하면 문자열 일부 치환
# # 문자열은 수정을 할 수 없는 자료형, 치환으로 새로운 문자열이 리턴
# print(phone_number1)
#
# Phone = "010-111-2222"
# Phone1 = Phone.replace("-", "")
# print(Phone1)
#
# url = "www.sharebook.kr"
# print(url[-2:])
# #문자열은 '.' 기준으로 분리된다.
# url_split = url.split('.')
# print(url_split[-1])  #-2, -3 입력하면 한덩어리씩 나온다.
#
# string = 'abcdfe2a354a32a'
# string1 = string.replace('a', 'A')
# print(string1)
#
# string = 'abcd'
# string.replace('b', 'B')
# print(string)   # 'aBcd'가 아닌 'abcd'가 출력 되는 이유, 문자열은 변경 할 수 없는 자료형이므로!