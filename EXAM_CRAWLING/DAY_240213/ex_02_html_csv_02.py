'''
    테이블 데이터를 CSV로 저장 #2
    colspan="2" 인 열 처리 (html_table_parser 라이브러리의 make2d() 함수)
'''

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parse
import pandas as pd
# html_table_parser 설치 시, 파이썬 3.10 이상일 때 오류 발생
# 그 오류를 해결하는 코드가 아래 2줄
# import collections
# collections.Callable = collections.abc.Callable
'''
pip uninstall beautifulsoup4

# anaconda 업데이트
conda update conda
conda update anaconda
conda update -all

conda install -c anaconda beautifulsoup4
'''
# beautifulsoup4 새로 설치하고 아나콘다 업데이트하니 위의 코드 없이도 잘 작동한다.

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')

# 두 개의 테이블 중에 첫 번쩨 테이블 사용 : find_all() 사용
# table = bs.find_all('table', {'class':'wikitable'})[0]
table = bs.find('table', {'class':'wikitable'})
table_data = parse.make2d(table)    # 2차원 리스트 형태로 변환

# 테이블의 2행을 출력
print('[0]:', table_data[0])
print('[1]:', table_data[1])

# Pandas DataFrame으로 저장 (2행부터 데이터 저장, 1행은 column 이름으로 사용)
df = pd.DataFrame(table_data[2:], columns=table_data[1])
print(df.head())

# csv 파일로 저장
csvFile = open('editors1.csv', 'w', encoding='utf-8')
writer = csv.writer(csvFile)

for row in table_data:
    writer.writerow(row)

csvFile.close()
