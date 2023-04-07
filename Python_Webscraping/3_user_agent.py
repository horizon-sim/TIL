import requests

url = "https://nadocoding.tistory.com"
headers = {"User-Agent":"blind"}
res = requests.get(url, headers=headers) 
res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)

# 지금 tistory는 User-Agent를 건드리지않아도 잘 가져온다.
# User-Agent를 넣어줌으로써 정보를 다 받을수있는 경우도 있다.