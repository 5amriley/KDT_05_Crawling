'''
    전화번호 분석 예제
'''

import re

# ^ .. $ 를 명시해야 정확한 자리수 검사가 이루어짐
tel_checker = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})$')   # 타입 : <class 're.Pattern'>

print(tel_checker.match('02-123-4567').group())
print(tel_checker.match('02-123-4567'))
print(tel_checker.match('053-950-45678'))
print(tel_checker.match('053950-4567'))

print('-'*50)

m = tel_checker.match('02-123-4567')

print(m.groups())
print('group(): ', m.group())
print('group(0): ', m.group(0))
print('group(1): ', m.group(1))
print('group(2, 3): ', m.group(2, 3))
print('start(): ', m.start())   # 매칭된 문자열의 시작 인덱스
print('end(): ', m.end())       # 매칭된 문자열의 마지막 인덱스 + 1

print(type(tel_checker))

print('-'*50)

cell_phone = re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$')

print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))
