import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다." # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = EMAIL_ADDRESS # 받는 사람

# # 여러 명에게 메일을 보낼 때
# msg["To"] = "~~~@naver.com, ~~~@gamil.com"
# to_list = ["~~~@naver.com", "~~~@gamil.com"]
# msg["To"] = ",".join(to_list) # 앞에 , 로 합치겠다는 의미

# # 참조
# msg["Cc"] = "EMAIL_ADDRESS"

# # 비밀참조
# msg["Bcc"] = "EMAIL_ADDRESS"

msg.set_content("테스트 본문입니다.") # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결이 잘 수립되는지 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인
    smtp.send_message(msg)