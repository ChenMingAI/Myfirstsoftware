# This Python file uses the following encoding: utf-8
# text=u'''职位描述 乐视招聘android自动化测试工程师 岗位职责:1、负责android超级电视TV设备的自动化方案设计、自动化测试与工具开发； 2、根据项目特点研究稳定性测试技术,完成相关工具的开发以及测试； 技能要求:1、有移动终端自动化工具架构设计与开发者优先,熟悉Android自动化工具Uiautomator、Monkey、MonkeyRunner 2、有实际用过JAVA/Python语言写过自动化测试脚本来测试项目的经验； 3、有Android自动化测试/稳定性测试经验,熟练掌握白盒测试工具JUnit、Instrumentation等； 4、熟悉linux命令,我们的工作环境是ubuntu操作系统 5、熟练使用git/svn等版本控制工具； 6、本科及以上学历（在职或者自考的本科可能暂时不考虑,ＨＲ要求的,特别优秀的除外）； PS:java/python编程开发基础扎实优先,有uiautomator实际项目经验者优先 个性能力要求:1. 主动思考、积极向上,有较强的逻辑分析能力和学习能力。 2. 工作细心、耐心、有责任心。 3. 具有良好的沟通能力和团队合作精神。 福利:转正后全员持股、年底奖金、带薪年假、餐补、交通补、通讯补等。'''
# import re
# str=''.join(re.findall(u'[\u4e00-\u9fff]+', text))
#
# print(len())
#Mark the word
# import jieba.posseg as pseg
# words = pseg.cut("我爱北京天安门!!!")
# print(type(words))
# for word,flag in words:
#     print(word,flag)
import jieba.posseg as pseg
import pymysql
import re
import csv
csv_reader=csv.reader(open('workhome_moments.csv',encoding='utf-8'))
user = "root"
passwd = "NUDTpdl@"

conn = pymysql.connect(host="127.0.0.1",user=user,passwd=passwd,db="contentsplitword",charset='utf8mb4' )
conn.set_charset('utf8')
conn.autocommit(1)
cur=conn.cursor()
insert_sql="insert into Splitword (id,splitword,date) values(%d,\'%s\',\'%s\')"
i=1
for row in csv_reader:
    txt=row[1]
    #print(txt)
    if txt!='':
        data = row[2]
        splitword = ''
        str = ''.join(re.findall(u'[\u4e00-\u9fff]+', txt))
        # seg_list = jieba.cut(str, cut_all=False)
        # splitwordall="/ ".join(seg_list)
        words = pseg.cut(str)

        for singleword, flag in words:
            if (flag=='a' or flag=='ad' or flag=='an' or flag=='ag' or flag=='al'):
                splitwordtmp = "/ " + singleword + ":" + flag
                splitword = splitword + splitwordtmp
            else:
                splitword=splitword+"%"

        splitword=''.join(re.findall(u'[\u4e00-\u9fff]{1,5}?''\\:', splitword))
        cur.execute(insert_sql % (i, splitword,data))
        i = i + 1
        if ((i%100)==0):
            conn.commit()
            print(("%d has been worked")%(i))


    #print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
    #print(data)
    # print(splitword)
    # print(str)
    # seg_list = jieba.cut(str, cut_all=False)
    # splitword="/ ".join(seg_list)

