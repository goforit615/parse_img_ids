from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")  # "html.parser"를 명시적으로 지정해 주세요.

# 이미지 태그를 찾습니다. 여기에서 "img" 태그를 사용합니다.
images = bsObj.findAll("img", {"src": re.compile("\.\./img/gifts/img\d+\.jpg")})

for image in images:
    print(image["src"])
