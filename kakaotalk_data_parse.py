"""
kakaotalk_data_parse.py 

n명으로 구성된 특정 카카오톡 채팅방 A 의 대화내용(.csv) 을 가져와서, 다시 각 멤버의 대화내용을 담고 있는 n개의 .csv 파일로 저장한다. 

Data Format: 
raw data: 
date - user - message 

output data: <username>.csv 
date - message

"""
import csv

def data_parse(file_name):
    f = open(file_name, 'r')
    rdr = csv.reader(f) 

    # 1. 딕셔너리에 각자의 대화내용 저장

    chat_dic = {}
    
    for line in rdr:
        """
        line 형식 예: ['2020-09-03 13:17:04', '박유찬', '저는 수목금 저녁 시간괜찮습니다']
        """
        if line[1] == 'User':
            continue
        if line[1] not in chat_dic:
            # print(line[1])
            chat_dic[line[1]] = [[line[0], line[2]]]
        else:
            chat_dic[line[1]].append([line[0], line[2]])
    f.close()

    # 2. 딕셔너리 내용을 csv 파일로 바꿔서 저장 
    for username in chat_dic.keys():
        f = open(username+".csv", 'w', encoding='utf-8-sig', newline='')
        wr = csv.writer(f) 
        for chat in chat_dic[username]:
            wr.writerow(chat)
        f.close()

        
if __name__ == "__main__":
    data_parse("KakaoTalk_Chat_컴윤사 8조_2020-10-28-15-17-03.csv")

