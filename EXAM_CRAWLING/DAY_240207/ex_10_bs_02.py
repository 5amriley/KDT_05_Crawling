from bs4 import BeautifulSoup

html_example =	'''
<!DOCTYPE	html>
<html	lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1	id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library	Examples!</span>
    <div id="link">
        <a	class="external_link"	href="www.google.com">google</a>
        <div id="class1">
                <p	id="first">class1's	first	paragraph</p>
                <a	class="external_link"	href="www.naver.com">naver</a>
                <p	id="second">class1's	second	paragraph</p>
                <a	class="internal_link"	href="/pages/page1.html">Page1</a>
                <p	id="third">class1's	third	paragraph</p>
        </div>
    </div>
    <div	id="text_id2">
                        Example	page
                        <p>g</p>
    </div>
    <h1	id="footer">Footer</h1>
</body>
</html>
'''

soup = BeautifulSoup(html_example, 'html.parser')

#print(soup.title)               # <title> 태그 전체 추출, 타입: <class 'bs4.element.Tag'>
#print(soup.title.string)        # <title> 태그의 텍스트만 리턴
#print(soup.title.get_text())    # <title> 태그의 텍스트만 리턴 (위와 동일)

#print(soup.title.parent)        # <title> 태그를 포함하고 있는 부모 태그 <head> 출력

# print(soup.body)                # <body> 태그 전체
#
# print(soup.h1)                  # 전체 중 첫 번째 <h1> 태그 추출
# print(soup.h1.string)

# print(soup.a)                   # 전체 중 첫 번째 <a> 태그 전체 추출
# print(soup.a.string)            # <a> 태그 내부의 텍스트 추출
# print(soup.a['href'])           # <a> 태그의 href 속성의 url을 추출
# print(soup.a.get('href'))       # <a> 태그의 href 속성의 url을 추출 (위와 동일)

#print(soup.find('div'))         # 전체 중 첫 번째 <div> 태그 전체 추출

#print(soup.find('div', {'id':'text_id2'}))     # 여러 <div> 태그 중, id 속성의 값이 'text_id2'인 항목 추출

# div_text = soup.find('div', {'id':'text_id2'})
# print(div_text.text)            # <div> 태그의 텍스트만 리턴
# print(div_text.string)          # <div> 태그 내부에 한 개 이상의 child 태그를 가지면 None 리턴

href_link = soup.find('a', {'class': 'internal_link'})  # 딕셔너리 형태
href_link = soup.find('a', class_ = 'internal_link')         # class_ 사용 => class는 파이썬의 예약어

# print(href_link)
# print(href_link['href'])
# print(href_link.get('href'))
# print(href_link.text)

# print('href_link.attrs: ', href_link.attrs)  # <a> 태그 내부의 모든 속성 출력
# print('class 속성값: ', href_link['class'])   # class 속성의 value 출력
#
# values = list(href_link.attrs.values())   # dictionary 값들을 리스트로 변경
# print('values[0]: {0}, values[1]: {1}'.format(values[0], values[1]))

# find() 메서드 활용
href_value = soup.find(attrs={'href':'www.google.com'})
href_value = soup.find('a', attrs={'href':'www.google.com'})

# print('href_values: ', href_value)
# print(href_value['href'])
# print(href_value.string)


# span_tag = soup.find('span')                # 첫 <span> 태그 전체 추출
#
# print('span tag:', span_tag)
# print('attrs:', span_tag.attrs)             # 딕셔너리 형태로 리턴
# print('value:', span_tag.attrs['class'])
# print('text:', span_tag.string)


div_tags = soup.find_all('div')
print('div_tags length:', len(div_tags))

for div in div_tags:
    print('----------------------------')
    print(div)


links = soup.find_all('a')

for alink in links:
    print(alink)
    print(f'url:{alink["href"]}, text: {alink.string}')
    print()


# 여러 <a> 태그에서 2개의 class 속성값 검색 ('external_link', 'internal_link' 만)
link_tags = soup.find_all('a', {'class':['external_link', 'internal_link']})
print(link_tags)

p_tags = soup.find_all('p', {'id':['first', 'third']})
for p in p_tags:
    print(p)
