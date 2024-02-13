import re

# match() 문자열의 처음부터 검사
m = re.match('[a-z]+', 'pythoN')    # 소문자가 1개 이상
print(m)

m = re.match('[a-z]+', 'PYthon')    # 소문자가 1개 이상
print(m)

print(re.match('[a-z]+','regex python'))
print(re.match('[a-z]+', 'regexpythoN'))

print(re.match('[a-z]+', 'regexpythoN'))
print(re.match('[a-z]+$', 'regexpythoN'))

print(re.match('[a-z]+', 'regexPython'))
print(re.match('[a-z]+$', 'regexpython'))
