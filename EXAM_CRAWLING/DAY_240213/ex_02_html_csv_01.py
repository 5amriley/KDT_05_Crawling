'''
    테이블 데이터를 CSV로 저장 #1
    colspan="2" 인 열 처리 X
    rowspan="2" 인 행 처리 X
'''

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')

# 두 개의 테이블 중에 첫 번쩨 테이블 사용
table = bs.find_all('table', {'class': 'wikitable'})[0]
rows = table.find_all('tr')

csvFile = open('editors.csv', 'wt', encoding='utf-8')   # t: text mode
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.find_all(['th', 'td']):
            print(cell.text.strip())
            csvRow.append(cell.text.strip())
        writer.writerow(csvRow)
finally:
    csvFile.close()
