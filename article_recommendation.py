# -*- coding: utf-8 -*-
import requests
import json
import random
import pickle 
import os

"""
메인함수 
input: 혐오표현 단어 
output: 혐오표현 단어 관련 기사 링크 1개
"""
def get_article(target_word) : 

    link = ''

    if os.path.isfile('./articles/'+str(target_word)+'.pickle') : # 저장된 파일이 있을 때
        link = get_from_saved_file(target_word)
        # print("recommended news: ", link, '\n')
    else:  # 저장된 파일 없을 때 
        link = crawling_and_save(target_word)
        # print("recommended news: ", link, '\n')
    
    return link 

"""
저장된 [target_word].pickle 파일 을 열어서 기사를 하나 랜덤으로 선택하고, 리스트에서 지운다. 
input: 혐오표현 단어
output: 혐오표현 단어 관련 기사 링크 1개
"""
def get_from_saved_file (target_word):

    filename = './articles/' + str(target_word) + '.pickle'

    with open(filename, 'rb') as f: 
        saved_articles = pickle.load(f)
    
    count = saved_articles['count']
    news_list = saved_articles['articles']

    final_news = random.choice(news_list)
    news_list.remove(final_news)
    count -= 1

    # print("count: ", count, "\n")

    if count >= 1 : 
        saved_articles['count'] = count
        saved_articles['news_list'] = news_list
        with open(filename, 'wb') as f: 
            pickle.dump(saved_articles, f)
        
    else : # 남은 링크가 없을 때, .pickle 파일 삭제
        if os.path.isfile(filename): 
            os.remove(filename)
            # print("removed!\n")
        else :
            print("error: file not found, cant remove file \n")

    return final_news


"""
target_word 를 제목에 포함하고 있는 기사들 10개를 찾아내고, 결과를 저장해 놓는다. 
그리고 랜덤으로 하나를 골라서 리턴한다. 
input: 혐오표현 단어
output: 혐오표현 단어 관련 기사 링크 1개
"""
def crawling_and_save (target_word): 

    url="https://openapi.naver.com/v1/search/news?"
    clientId="k9JTMlEhxRLW7qKOPL66"
    clientSecret="8XeyVssQLq"

    header = {
        "X-Naver-Client-Id" :clientId,
        "X-Naver-Client-secret":clientSecret
    }

    saved_articles = {}                                                    
    news_list= [] 
    number_of_articles = 10 
    queryString="query=" + str(target_word)                                   
    displayString = "display=" + str(int(number_of_articles))

    r=requests.get(url+queryString, headers=header)
    final = (json.loads(r.text))

    for item in final[u'items']:
        # news_list.append([item[u'link'],item[u'pubDate']])           
        news_list.append(item[u'link'])

    final_news=random.choice(news_list)
    news_list.remove(final_news)

    saved_articles['count'] = len(news_list)
    saved_articles['articles'] = news_list

    with open('./articles/' + str(target_word) + ".pickle", 'wb') as f:
        pickle.dump(saved_articles, f)

    # print("initial count: ", len(news_list), "\n" )

    return final_news



