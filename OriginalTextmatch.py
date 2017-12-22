import pymysql
user = "root"
passwd = "NUDTpdl@"

conn = pymysql.connect(host="127.0.0.1",user=user,passwd=passwd,db="contentsplitword",charset='utf8mb4' )
conn.set_charset('utf8')
conn.autocommit(1)
cur=conn.cursor()
select_sql="select date from emojiextract where flag!=''"
select_sqlfromoriginal="select content from totaldata where date=\'%s\'"
update_sql="update emojiextract set content=\'%s\' where date=\'%s\'"

cur.execute(select_sql)
select_data=cur.fetchall()
i=1
for single_data in select_data:
    cur.execute(select_sqlfromoriginal % (single_data))
    content=cur.fetchall()
    # print(type(content[0][0]))
    # break
    # print(update_sql%(content[0][0],single_data[0]))
    # break
    try:
        cur.execute(update_sql % (content[0][0], single_data[0]))
    except Exception as ee:
        print(ee)
        pass

    i=i+1
    if i%100==0:
        conn.commit()
        print(("%d has been worked") % (i))


#
# print(cur.fetchone())

