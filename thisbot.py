#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import tweepy
import logging
from config import create_api
import random
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def writeTweetsfromTxt(api):
    logger.info("bot started")

    f = open("C:\\Users\\00_ma\\AppData\\Local\\Programs\\Python\\Python38-32\\tweepy-bots\\bots\\data.txt", 'r', encoding='UTF-8') #파일 열기
    datas = f.readlines()
    num = len(datas)+1

    ran =  random.randint(0, num-1)
    
    #print(datas[ran])
    
    api.update_status(datas[ran])
    
    f.close() #파일 닫기
    #os.system("pause")

def main():
    api = create_api()
    writeTweetsfromTxt(api)


if __name__ == "__main__":
    main()
