import csv 

"""
kakaotalk_user_wordcount.py

개인 대화내용인 <username>.csv 파일에서 특정 단어가 몇개나 들어있는지 세어 주는 모듈

input: 사람이름, 세고 싶은 단어 
output: 대화속의 단어 수 

"""

def word_count(username, target):
    f = open(username+'.csv', 'r')
    rdr = csv.reader(f) 

    count = 0

    for line in rdr: 
        count += line[1].count(target)
    
    f.close()

    return count

if __name__ == "__main__":
    print(word_count('박유찬', '수고'))