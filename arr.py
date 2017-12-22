# import jieba.analyse
# txt="女人还是不要对什么事情都太认真了，太认真了会受伤、会难过，还是没心没肺点好啦！"
# tagsanother = jieba.analyse.textrank(txt, topK=4, withWeight=True)
# print(tagsanother)
from numpy import *
vocabList=["hi","you","like","me","hihi"]
inputSet=["you","hi","like","him","hi"]
returnVec = [0]*len(vocabList)        # 创建一个其中所含元素都为0的向量
for word in inputSet:
    if word in vocabList:
        # returnVec[vocabList.index(word)] = 1     # index函数在字符串里找到字符第一次出现的位置  词集模型
        returnVec[vocabList.index(word)] += 1      # 文档的词袋模型    每个单词可以出现多次
    else: print ("the word: %s is not in my Vocabulary!" % word)
# print(returnVec)

p0Num = ones(6);
print(p0Num)