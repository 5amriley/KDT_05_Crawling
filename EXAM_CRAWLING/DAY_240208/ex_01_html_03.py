'''
    트리 이동
    - 문서 내부에서 특정 위치를 기준으로 태그를 찾을 때
    - 단방향으로 트리 이동
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

table_tag = soup.find('table', {'id': 'giftList'})
print('child 개수: ', len(list(table_tag.children)))
for child in table_tag.children:
    print(child)    # <tr> 단위로 저장되어 있지만, 중간중간에 빈 값('\n')들도 있음
    print('-'*30)


# 자손 : descendants
desc = soup.find('table', {'id': 'giftList'}).descendants
list_desc = list(desc)
print('descendants 개수: ', len(list_desc))

for tag in list_desc:
    print(tag)


# next_siblings 속성
# 임의의 행을 선택하고 next_siblings 를 선택하면, 테이블의 다음 행들을 모두 선택 (모든 형제를 선택, 자기자신(선택된 행)은 제외)
for sibling in soup.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)

# previous_siblings 속성
for sibling in soup.find('tr', {'id': 'gift2'}).previous_siblings:
    print(sibling)


# next_sibling, previous_sibling
sibling1 = soup.find('tr', {'id': 'gift3'}).next_sibling
print('sibling1:', sibling1)    # sibling1 = '\n' 라 출력되지 않음
print(ord(sibling1))    # ord(문자) : 문자의 Unicode 정수를 리턴


# parent 속성
style_tag = soup.style
print(style_tag.parent)

# parent 속성 (2)
img1 = soup.find('img', {'src': '../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()  # 부모 태그의 이전 형제 태그 검색 -> 그 태그 내부의 문자열 반환
print(text)

