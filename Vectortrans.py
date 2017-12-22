import pymysql
import jieba.analyse
user = "root"
passwd = "NUDTpdl@"

conn = pymysql.connect(host="127.0.0.1",user=user,passwd=passwd,db="contentsplitword",charset='utf8mb4' )
conn.set_charset('utf8')
conn.autocommit(1)
cur=conn.cursor()
select_sql="select date,content from emojiextract where content!=''"
select_ifex="select splitwordvector from emojiextract where date=\'%s\'"
update_sql="update emojiextract set splitwordvector=\'%s\' where date=\'%s\'"
cur.execute(select_sql)
select_data=cur.fetchall()
i=1
for single_data in select_data:

    cur.execute(select_ifex % (single_data[0]))
    spliwo_ifex=cur.fetchall()[0][0]
    # print(type(spliwo_ifex))
    # break
    arrastr=[]

    # if spliwo_ifex!='':
    #     print("exits")
    #     pass
    # else:
    #     tagsanother = jieba.analyse.textrank(single_data[1], topK=3, withWeight=True)
    #     if len(tagsanother) == 3:
    #         for tag in tagsanother:
    #             arrastr.append(round(tag[1], 3))
    #         cur.execute(update_sql % (str(arrastr), single_data[0]))
    #     i = i + 1

    if i%100==0:
        conn.commit()
        print(("%d has been worked") % (i))


#
# print(cur.fetchone())

