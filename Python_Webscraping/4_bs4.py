import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title) # 이건 태그까지 포함
# print(soup.title.get_text()) # 이건 html 글자만
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element 의 속성 정보 값
# print(soup.a["href"]) # a element 의 href 속성 '값' 정보를 출력

# # class="Nbtn_upload" 인 a element 를 찾아줘
# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# print(soup.find(attrs={"class":"Nbtn_upload"})) # 이것도 된다

# print(soup.find("li", attrs={"class":"rank01"}))

# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())

# 다음으로 바로 넘어가는 방법
# print(rank1.next_sibling) # 줄바꿈이 있어서 그럴가능성이있음
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling # 이전 이전
# print(rank2.a.get_text())
# print(rank1.parent) # 부모 태그로 가기

# 랭크1기준으로 다음 li를 찾기
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank3.a.get_text())

# 한번에 모든정보 받아서 처리
# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="여신강림-159화")
print(webtoon)