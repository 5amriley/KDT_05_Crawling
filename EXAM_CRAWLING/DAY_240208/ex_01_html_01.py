from bs4 import BeautifulSoup

html_text = '<span class="red">Heavens! what a virtulent attack!</span>'
soup = BeautifulSoup(html_text, 'html.parser')

object_tag = soup.find('span')
print('object_tag:', object_tag)
print('attrs:', object_tag.attrs)
print('values:', object_tag.attrs['class'])
print('text:', object_tag.text)
print('values 이것도 가능:', object_tag['class'])
