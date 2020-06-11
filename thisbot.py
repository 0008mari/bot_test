
import tweepy
import logging
from config import create_api
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def writeTweetsfromTxt(api):
    logger.info("bot started")

    f = open("C:\\Users\\00_ma\\AppData\\Local\\Programs\\Python\\Python38-32\\tweepy-bots\\bots\\tweet_file.txt", 'r', encoding='UTF-8') #파일 열기
    datas = f.readlines()
    num = len(datas)+1 #각 줄을 리스트로 저장, num은 리스트 크기
    # range 함수는 stop 숫자 미포함

    ran =  random.randint(0, num-1) #난수 뽑기

    result = datas[ran].replace("\\n", "\n")
    
    print(result)
    # 그 난수로 나온 애만 출력할때 바꿔준다.. 왜 다 복사하고 앉았너 
    
    api.update_status(result)
    
    f.close() #파일 닫기
    #os.system("pause")

def main():
    api = create_api()
    writeTweetsfromTxt(api)


if __name__ == "__main__":
    main()
