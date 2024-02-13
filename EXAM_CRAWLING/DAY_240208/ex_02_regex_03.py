import re

# findall() 함수 : 일치하는 모든 문자열을 리스트로 리턴
p = re.compile('[a-z]+')
print(p.findall('life is too short! Regular expression test'))

# search() 함수
result = p.search('I like apple 123')   # 타입 : <class 're.Match'>
print(result)   # 'like'
print(result.group())   # group() : 일치하는 전체 문자열 리턴

result = p.findall('I like apple 123')
print(result)
