# python.py
import requests
from bs4 import BeautifulSoup
import json

# your 'something' goes here 로 작성된 부분에 정보를 입력하면 된다.

# slack app의 webhook url을 정의한다
webhook_url = 'https://hooks.slack.com/services/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'

def send_slack_message():
    headers = {
        'Content-type': 'application/json'
    }
    
    # 알림 전송할 공지사항 페이지를 요청한다
    notice_body_res = requests.get(link)
    # HTML 소스를 가져온다
    html = notice_body_res.text
    # BeautifulSoup로 html 소스를 python 객체로 변환한다
    soup = BeautifulSoup(html, 'html.parser')
    # CSS selector로 html 요소에 접근한다
    # 공지사항 본문은 .contents-inner -> .bbs-view -> .bbs-body 이다
    notice_body = soup.select (
        '.contents-inner .bbs-view .bbs-body'
    )
    print(notice_body[0].text)
    # POST 의 body에 제목, 링크, 내용을 모두 포함한다
    data = {
        'text': '제목: ' + my_titles[0].text + '\n' + '내용: ' + notice_body[0].text + '\n' + '링크: ' + link
    }

    res = requests.post(webhook_url, headers=headers, data=json.dumps(data))
    print('slack webhook 응답: ' + str(res.status_code))


# HTTP GET Request
req = requests.get('http://www.pknu.ac.kr/usrBoardActn.do?p_bm_idx=5&p_boardcode=PK10000005')

# HTML 소스 가져오기
html = req.text

# BeautifulSoup으로 html소스를 python객체로 변환하기
# 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
# 이 글에서는 Python 내장 html.parser 를 이용했다
soup = BeautifulSoup(html, 'html.parser')

# CSS Selector를 통해 html요소들을 찾아낸다.
# contents > div.contents-inner > form:nth-child(3) > table > tbody > tr:nth-child(5) > td.title > a
# 공지사항 리스트
my_titles = soup.select(
    '.title > a'
)
# contents > div.contents-inner > form:nth-child(3) > table > tbody > tr:nth-child(19) > td.no
# 공지사항 넘버
my_num = soup.select(
    '.no'
)
# my_titles는 list 객체

print("====================================학교 공지사항===========================================")
for title in my_titles:
    # Tag안의 텍스트
    print(title.text)
    # Tag의 속성을 가져오기(ex: href속성)
    print(title.get('href'))

print("===========================================================================================")

# 콘솔 화면에 보여줌
print("=============현재 최신 공지사항================")
print(my_titles[0].text)
link = 'http://www.pknu.ac.kr'+my_titles[0].get('href')
print(link)

# 메모장에 저장된 최신 공지사항 url 읽어옴
try:
    f = open("new_notice.txt", 'r')
    notice_url = f.read()
# 파일을 찾을 수 없다면 제일 처음 씌여지는 경우 이므로 바로 알림 보낸다
except FileNotFoundError :
    f = open("new_notice.txt", 'w')
    f.write(my_titles[0].get('href'))
    send_slack_message()
    exit()

f.close()

# 메모장에 저장되있던 url과 새로 읽어들인 url이 다를 경우 메시지보내고 해당 url저장
if notice_url != my_titles[0].get('href'):
    print("새로운 url 이므로 slack으로 해당 공지를 전송")
    f = open("new_notice.txt", 'w')
    f.write(my_titles[0].get('href'))
    f.close()
    # Slack으로 보내기
    # 테스트채널
    send_slack_message()
else:
    print("기존 공지사항과 url같음. slack으로 공지 전송 X")
