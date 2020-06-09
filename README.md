# bot_test

일정 주기로 텍스트 파일에서 한 줄을 읽어 트윗을 올리는 프로그램을 만들어보기로 했다.
python 모듈 tweepy를 이용하였다.

참고 문서:

* https://realpython.com/twitter-bot-python-tweepy/ tweepy 사용
* http://hleecaster.com/task-scheduling-in-windows-using-cron/ cron으로 일정 주기마다 프로그램 실행

## tweepy 설치

```
pip install tweepy
```

가상환경을 설정했는지 안 했는지 모르겠다.

아마 귀찮아서 안 한 거 같은데...

얼마전에 컴퓨터 밀어서 아무것도 안 깔려있으니 걱정 노노 (아마도)

## api 얻기

https://developer.twitter.com/en

이 부분이 귀찮았는데 영어를 열심히 읽으면서 따라가면 되는 듯하다

해당 계정은 전화번호와 이메일이 등록된 상태여야 하고,

이 앱을 어디에 쓸지 영어로 100자 정도 작문해야 한다. 몇번 해야하니까 똑같은 말을 복붙할 수 있도록 준비하면 편할듯 

## 코드 작성

tweepy와 관련된 기능은 거의 쓰지 않았다.

```python
api = tweepy.API() #api 받아오기
api.update_status("문자열") #해당 문자열을 트윗 작성
```

오랜만에 파일입출력을 복습했다... 해당 파일은 커밋하겠음

그래서... 이제 다 했다.

thisbot.py를 실행하면 랜덤하게 한 줄을 작성해준다.

## cron으로 작업 예약하기

일정한 시간마다 thisbot.py를 실행시키기 위해 작업 스케줄러를 알아보았다.

윈도우 기본 작업 스케줄러보다 cron을 써서 한다고 해서 깔았음.

상기 링크 참고.

cron은 유닉스 계열에서 쓰는 건데 이걸 윈도우에서 돌아가게 한 프로그램이 nncron

라이트 버전을 깔아준다. 라이트 버전은 프리웨어.

워드패드를 관리자 권한으로 실행해 cron.tab을 수정해준다.

```
* * * * * C:\Users\00_ma\AppData\Local\Programs\Python\Python38-32\python.exe C:\Users\00_ma\AppData\Local\Programs\Python\Python38-32\tweepy-bots\bots\thisbot.py
```

테스트를 위해 매 분 마다 실행시켜줌.

컴퓨터에서 파이썬 프로그램 창이 잠깐 켜졌다가 꺼지는 것을 확인함.

**근데 안 되네?**

왜 안되는지 모르겠다.



