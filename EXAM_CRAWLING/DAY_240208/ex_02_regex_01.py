import re

# compile() 사용 안 함, 정규식 객체 생성 안 함
m = re.match('[a-z]+', 'Python')    # 매번 패턴 입력 (소문자)
print(m)
print(re.search('apple', 'I like apple!'))  # 매번 패턴 입력 (apple)

# compile() 사용, 정규식 객체(p) 생성
p = re.compile('[a-z]+')    # 알파벳 소문자 패턴, 여러 번 사용
m = p.match('python')
print(m)
print(p.search('I like apple 123'))
