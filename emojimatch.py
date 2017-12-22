
# str="%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/ 懒惰:a%%%%%%%%/ 傻:a%%%/ 不糙:a"
# str="*******[愤怒]*******[难受]****[开心]*****[色]"
# str1 = ''.join(re.findall(u'\\[''[\u4e00-\u9fff]{1,5}?''\\]', str))
import re
import pymysql


user = "root"
passwd = "NUDTpdl@"

conn = pymysql.connect(host="127.0.0.1",user=user,passwd=passwd,db="contentsplitword",charset='utf8mb4' )
conn.set_charset('utf8')
conn.autocommit(1)
cur=conn.cursor()
update_sql="update emojiextract set flag=\'%s\' where id=%d"
select_sql="select * from emojiextract where emoji!='';"
cur.execute(select_sql)
select_data=cur.fetchall()
# print(select_data)
for s_data in select_data:
    str=s_data[1]
    print(str)
    array = ' '.join(re.findall(u'[\u4e00-\u9fff]+', str)).split(' ')
    for ai in array:
        if  ai=="红包" or ai=="悠闲" or ai=="拳头" or ai=="爱你" or ai=="太阳" or ai=="奸笑" or ai=="大笑" or ai=="坏笑" or ai=="转圈" or ai=="害羞" or ai=="拥抱" or ai=="调皮" or ai=="嘿哈" or ai=="捂脸" or ai=="鼓掌" or ai=="耶" or ai=="亲亲" or ai=="鼓掌" or ai=="奋斗" or ai=="爱心" or ai=="呲牙" or ai=="得意" or ai == "微笑" or ai == "色" or ai == "憨笑" or ai == "机智" or ai == "愉快" or ai == "胜利" or ai == "偷笑" or ai=="强":

            cur.execute(update_sql%("good",s_data[0]))
            print("mark good")
            break
        elif ai=="吐" or ai=="流汗" or ai=="心碎" or ai=="发怒" or ai=="吓" or ai=="冷汗" or ai=="困" or ai=="惊恐" or ai=="撇嘴" or ai=="委屈" or ai=="流泪" or ai=="大哭" or ai == "衰" or ai == "晕" or ai == "快哭了" or ai == "皱眉" or ai=="可怜" or ai=="傲慢" or ai=="抓狂" or ai=="难过":
            cur.execute(update_sql % ("bad", s_data[0]))
            print("mark bad")
            break
        elif ai=="勾引" or ai=="抱拳" or ai=="玫瑰" or ai=="咖啡" or ai=="发呆" or ai=="疑问":
            cur.execute(update_sql % ("normal", s_data[0]))
            print("mark normal")
            break
conn.commit()
