import requests
res = requests.get("https://www.google.com")
# res = requests.get("https://www.google.com", verify=False) # 안되면 이렇게하기도함
res.raise_for_status() # 올바르게 값을 가져오면 ok 아니면 에러를 강제로 내버림

print("응답코드 :", res.status_code) # 200 이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [응답코드 ",res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)