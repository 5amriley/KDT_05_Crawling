from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

princeList = bs.find_all(text='the prince')                     # DeprecationWarning 발생
print('the prince count: ', len(princeList))

prince_list = bs.find_all(text=re.compile('[T|t]{1}he prince')) # DeprecationWarning 발생
print('T|the prince count:', len(prince_list))
