# PKNU notice parser

Python, BeautifulSoup, Slack Webhook API 를 활용한 부경대학교 공지사항 알림이

## Getting Started

설치에 앞서 다음과 같은 과정으로 환경을 설정해야 합니다

### Prerequisites

다음과 같은 파이썬 버전과 패키지 그리고 Slack 컴포넌트를 준비해야 합니다. 각 패키지는 pip로 설치 가능합니다.

- Python >= 3.6
- beautifulsoup4 >= 4.7.1
- requests >= 2.22.0
- Slack Workspace
- Slack App

Slack 워크스페이스는 이미 생성되었다고 가정하고, Slack App을 생성합니다.

### Create Slack App

Slack App을 만들기 위해 [Slack API](https://api.slack.com/) 홈페이지에 접속하고, 맨 오른쪽 위 Your Apps버튼을 클릭하면 다음과 같은 화면이 나옵니다.
여기에선 이미 기존에 만들어진 App이 존재하지만, 새로운 App을 만들어 줍니다. 오른족 위의 Create New App 버튼을 클릭합니다.\
\
<img width="1678" alt="Screen Shot 2019-09-11 at 4 54 11 AM" src="https://user-images.githubusercontent.com/31213226/64646140-63019b80-d451-11e9-8a3b-248f8b9b2c5c.png">

App의 이름과 연동할 워크스페이스를 선택합니다. 새롭게 만든 워크스페이스를 선택해 줍니다.\
\
<img width="460" alt="Screen Shot 2019-09-11 at 4 54 40 AM" src="https://user-images.githubusercontent.com/31213226/64646214-92b0a380-d451-11e9-9c4e-8dbf799a572f.png">

그런 다음 Create App 버튼을 누르면 다음과 같은 화면으로 넘어갑니다.\
\
<img width="460" alt="Screen Shot 2019-09-11 at 4 55 06 AM" src="https://user-images.githubusercontent.com/31213226/64646269-b2e06280-d451-11e9-990c-bc07ebe08d00.png">

그림에서 Incoming Webhooks라는 버튼을 클릭합니다.\
\
<img width="1677" alt="Screen Shot 2019-09-11 at 4 55 45 AM" src="https://user-images.githubusercontent.com/31213226/64646331-d5727b80-d451-11e9-96f7-9901851fa369.png">

오른쪽 버튼을 ON시켜서 Incoming Webhooks기능을 활성화 시킵니다.\
\
<img width="600" alt="Screen Shot 2019-09-11 at 4 56 20 AM" src="https://user-images.githubusercontent.com/31213226/64646371-f2a74a00-d451-11e9-8845-f5db659ae0e8.png">

그런 다음엔 Webhooks URL을 생성할 수 있는 인터페이스가 나타나는데, 아래의 Add new Webhookds to Workspace 버튼을 눌러서 URL을 생성합니다.\
\
<img width="600" alt="Screen Shot 2019-09-11 at 4 56 49 AM" src="https://user-images.githubusercontent.com/31213226/64646424-0baffb00-d452-11e9-87cc-b3be19125487.png">

알림을 전송 할 채널을 선택해 줍니다.\
\
<img width="416" alt="Screen Shot 2019-09-11 at 4 57 27 AM" src="https://user-images.githubusercontent.com/31213226/64646514-38641280-d452-11e9-8ec6-de749192f3a2.png">

잠시 뒤 만들어진 URL을 PKNUNotifierAtSlack.py 의 webhook_url 변수에 문자열로 저장해주면 됩니다.\
\
<img width="676" alt="Screen Shot 2019-09-11 at 4 57 59 AM" src="https://user-images.githubusercontent.com/31213226/64646666-7cefae00-d452-11e9-9ebe-38a594880535.png">

```
webhook_url = "여기에 발급받은 Webhooks URL을 입력하세요"
```

## DEMO

pknu-notifier.slack.com\
\
<img width="1680" alt="Screen Shot 2019-09-11 at 5 24 22 AM" src="https://user-images.githubusercontent.com/31213226/64647808-a90c2e80-d454-11e9-8d61-72a233ea01ca.png">

## LICENSE

MIT
