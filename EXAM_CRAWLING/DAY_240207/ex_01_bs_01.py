from urllib.request import urlopen

html = urlopen('http://www.daangn.com/hot_articles')
print(type(html))
print(html.read())
