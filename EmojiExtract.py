import pymysql
import jieba
import re
import csv
csv_reader=csv.reader(open('workhome_moments.csv',encoding='utf-8'))
user = "root"
passwd = "NUDTpdl@"

conn = pymysql.connect(host="127.0.0.1",user=user,passwd=passwd,db="contentsplitword",charset='utf8mb4' )
conn.set_charset('utf8')
conn.autocommit(1)
cur=conn.cursor()
insert_sql="insert into emojiextract (id,emoji,date) values(%d,\'%s\',\'%s\')"
i=1
for row in csv_reader:
    txt=row[1]
    #print(txt)
    if txt!='':
        data = row[2]

        str = ''.join(re.findall(u'\\[''[\u4e00-\u9fff]{1,5}?''\\]', txt))

        cur.execute(insert_sql % (i, str,data))
        i = i + 1
        if ((i%100)==0):
            conn.commit()
            print(("%d has been worked")%(i))




