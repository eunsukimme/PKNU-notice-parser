# PKNU_notice_parser

### Parse PKNU notices and send message to slack chennel

1.  use slack api "slacker"

*   to alert some news
  * 함수로 표현해놓음
  <pre>
    <code>
      def send_slack_message(token):
        slack = Slacker(token)
        slack.chat.post_message('#your_channel_name_goes_here', my_titles[0].text)
        slack.chat.post_message('#your_channel_name_goes_here', link)
    </code>
  </pre>

2.  use library "BeautifulSoup"

*   to parse PKNU web
  *   BeautifulSoup으로 html소스를 python객체로 변환하기
  *   첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
  *   이 글에서는 Python 내장 html.parser 를 이용했다
    ```soup = BeautifulSoup(html, 'html.parser')```
