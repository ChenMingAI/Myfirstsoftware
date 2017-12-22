import pymysql
import jieba.analyse
import csv
csv_reader=csv.reader(open('workhome_moments.csv',encoding='utf-8'))
user = "root"
passwd = "NUDTpdl@"

conn = pymysql.connect(host="127.0.0.1",user=user,passwd=passwd,db="contentsplitword",charset='utf8mb4' )
conn.set_charset('utf8')
conn.autocommit(1)
cur=conn.cursor()
insert_sql="insert into WordVector (id,wordvector,date) values(%d,\'%s\',\'%s\')"
f = open('log.txt','w')
i=1
for row in csv_reader:
    txt=row[1]
    arrastr=[]
    #print(txt)
    if txt!='':
        date = row[2]

        tagsanother = jieba.analyse.textrank(txt, topK=3, withWeight=True)
        if len(tagsanother) == 3:
            for tag in tagsanother:
                arrastr.append(round(tag[1], 3))
            cur.execute(insert_sql%(i,str(arrastr),date))
            # print("vector extracted")

        else:
            print(date, file=f)
        i = i + 1

        if ((i%100)==0):
            conn.commit()
            print(("%d has been worked")%(i))




# tags = jieba.analyse.extract_tags(content, topK=5,withWeight=True)


