'''
    2024/02/12
    저장된 csv파일을 읽어서 사용자가 입력한 지역에 있는 매장 정보 출력
    파일명 : hollys_branches.csv
'''
import pandas as pd

# 저장된 csv 파일 읽어오기
filename = 'hollys_branches.csv'
hollysDF = pd.read_csv(filename, encoding='utf-8')

while True:
    region_input = input('검색할 매장의 도시를 입력하세요: ')
    if region_input == 'quit':
        print('종료합니다.')
        break
    print('-'*30)

    region_mask = hollysDF['지역'].str.startswith(region_input)
    resultDF = hollysDF[region_mask]
    print(f'검색된 매장 수: {len(resultDF)}')
    print('-'*30)
    for i in range(len(resultDF)):
        temp = [resultDF.iloc[i, 2], resultDF.iloc[i, 3]]
        print(f'[{i+1:3d}] {temp}')
    print('-'*30)
