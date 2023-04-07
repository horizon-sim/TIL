from imap_tools import MailBox, mailbox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# mailbox.logout()
# 위 내용보다 밑에가 좀더 코드적으로 깔끔


with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    
    # # 전체 메일 다 가져오기
    # for msg in mailbox.fetch(limit=2, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # # 읽지 않은 메일만 가져오기
    # for msg in mailbox.fetch('(UNSEEN)'):
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # # 특정인이 보낸 메일 가져오기
    # for msg in mailbox.fetch('(FROM EMAIL_ADDRESS)'):
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # # 작은 따옴표로 먼저 감싸고, 실제 TEXT 부분은 큰 따옴표로 감싸주세요
    # # 어떤 글자를 포함하는 메일 (제목, 본문) 작은 따옴표 큰따옴표 다 규칙이 있음
    # for msg in mailbox.fetch('(TEXT "test mail")'):
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # # 어떤 글자를 포함하는 메일 (제목만)
    # for msg in mailbox.fetch('(SUBJECT "test mail")'):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # # 어떤 글자(한글)을 포함하는 메일 필터링 (제목만)
    # for msg in mailbox.fetch(limit=2, reverse=True):
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))
    
    # # 특정 날짜 이후의 메일
    # for msg in mailbox.fetch('(SENTSINCE 07-nov-2020)'):
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # # 2 가지 이상의 조건을 모두 만족하는 메일 (AND)
    # for msg in mailbox.fetch('(ON 12-Jan-2022 SUBJECT "test mail")'):
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # 2 가지 이상의 조건 중 하나라도 만족하는 메일 (OR)
    for msg in mailbox.fetch('(OR ON 12-Jan-2022 SUBJECT "test mail")'):
        print("[{}] {}".format(msg.from_, msg.subject))
        