from bs4 import BeautifulSoup

national_anthem ='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>애국가</title>
</head>
<body>
    <div>
        <p id="title">애국가</p>
        <p class="content">
            동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            남산 위에 저 소나무 철갑을 두른 듯 바람서리 불변함은 우리 기상일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>                
    </div>
</body>
</html>
'''

# 제목과 추출
soup = BeautifulSoup(national_anthem, 'html.parser')
print(soup.select_one('p#title').string)

# 가사 내용 추출
contents = soup.select('p.content')
for content in contents:
    print(content.text)

