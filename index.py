from urllib.request import urlopen
from bs4 import BeautifulSoup

# with as 구문
# 아래는 동일한 뜻을 가진 코드 이다
# with as는 앞에있는 부분을 as 뒤에 있는 변수로 사용하겠다라는 뜻을 가진다 그 후 아래에서 변수를 사용한다
# with [expression] as [변수명]
""" response = urlopen("https://www.naver.com/")
with urlopen("https://www.naver.com/") as response:
    response """

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, "html.parser")
print(soup.prettify())

for link in soup.find_all("a"):
    print(link.get("href"))

print(soup.get_text())

""" with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

soup = BeautifulSoup("<html>a web page</html>", 'html.parser') """

with urlopen("https://en.wikipedia.org/wiki/Main_Page") as response:
    soup = BeautifulSoup(response, "html.parser")
    for anchor in soup.find_all("a"):
        print(anchor.get("href", "/"))
# writedata.py
""" f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close() """

with urlopen("https://en.wikipedia.org/wiki/Main_Page") as response:
    soup = BeautifulSoup(response, "html.parser")
    f = open("새파일.txt", "w")
    i = 1
    for anchor in soup.find_all("a"):
        # print(anchor.get("href", "/"))
        data = str(i) + " : " + anchor.get_text() + "\n"
        i += 1
        f.write(data)
    f.close()
