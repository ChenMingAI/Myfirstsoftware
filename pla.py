from numpy import *
from numpy.linalg import *
import string
import random
import time
import matplotlib.pyplot as plt
import operator
def Is_Same_Sign(W,vector,y):
    if(dot(W,vector) >0 and y>0) or (dot(W,vector)<=0 and y<0):
        return True
    else:
        return False


def getErrorNum(X,Y,W):
    (dataNum,dataDim)=X.shape
    Sum=0
    for i in range(0,dataNum):
        if not Is_Same_Sign(W,X[i],Y[i]):
            Sum+=1
    return Sum


def Pocket_Algo(X,Y,iterateTimes):
    (m,n)=shape(X)
    W_p=ones(n)
    W=[ 2,-2.086837,-3.61571101,-1.940475,2.1869404 ]
    ErrNum_p=m

    iterate=0

    while iterate<iterateTimes:
        iterate += 1
        wrongdata=0
        # print("dataIdx"+str(dataIdx))
        for dataIdx in range(m):
            if not Is_Same_Sign(W, X[dataIdx], Y[dataIdx]):
                wrongdata+=1
                W = W + Y[dataIdx] * X[dataIdx]
                ErrNum = getErrorNum(X, Y, W)
                if ErrNum < ErrNum_p:
                    W_p = W
                    ErrNum_p = ErrNum
        if not wrongdata:
            print("success")
            break
        print("iter:" + str(iterate))



    return W_p

def Data_Prepro(path):
    rawData=open(path).readlines()
    dataNum=len(rawData)
    dataDim=len(rawData[0].strip().split(' '))+1
    dataIdx = 0
    X = zeros([dataNum, dataDim])
    X[:,0]=1
    Y=zeros(dataNum)

    print(type(Y))
    for line in rawData:
        temp = line.strip().split('\t')
        temp[0] = temp[0].split(' ')

        Y[dataIdx] = int(temp[1])
        # print(Y)

        X[dataIdx, 1:] = double(temp[0])
        # print(X)
        dataIdx += 1
    return (X,Y)
# def createTrainDataSet():#训练样本,第一个1为阈值对应的w，下同
#     trainData=[   [1, 1, 4],
#                     [1, 2, 3],
#                     [1, -2, 3],
#                     [1, -2, 2],
#                     [1, 0, 1],
#                     [1, 1, 2]]
#     label=[1, 1, 1, -1, -1,  -1]
#     return trainData, label
# def createTestDataSet():#数据样本
#     testData = [   [1, 1, 1],
#                    [1, 2, 0],
#                    [1, 2, 4],
#                    [1, 1, 3]]
#     return testData
# def sigmoid(X):
#     X=float(X)
#     if X>0:
#         return 1
#     elif X<0:
#         return -1
#     else:
#         return 0
# def pla(traindataIn,trainlabelIn):
#     traindata=mat(traindataIn)
#     trainlabel=mat(trainlabelIn).transpose()
#     m,n=shape(traindata)
#     w=ones((n,1))
#     while True:
#         iscompleted=True
#         for i in range(m):
#             if (sigmoid(dot(traindata[i],w))==trainlabel[i]):
#                 continue
#             else:
#                 iscompleted=False
#                 w+=(trainlabel[i]*traindata[i]).transpose()
#         if iscompleted:
#             break
#     return w
# def classify(inX,w):
#     result=sigmoid(sum(w*inX))
#     if result>0:
#         return 1
#     else:
#         return -1
# def plotBestFit(w):
#     traindata,label=createTrainDataSet()
#     dataArr = array(traindata)
#     n = shape(dataArr)[0]
#     xcord1=[];ycord1=[]
#     xcord2=[];ycord2=[]
#     for i in range(n):
#         if int(label[i])==1:
#             xcord1.append(dataArr[i,1])
#             ycord1.append(dataArr[i,2])
#         else:
#             xcord2.append(dataArr[i, 1])
#             ycord2.append(dataArr[i, 2])
#     fig=plt.figure()
#     ax= fig.add_subplot(111)
#     ax.scatter(xcord1, ycord1,s=30,c='red',marker='s')
#     ax.scatter(xcord2, ycord2,s=30,c='green')
#     x = arange(-3.0, 3.0, 0.1)
#     y = (-w[0]-w[1] * x)/w[2]
#     ax.plot(x, y)
#     plt.xlabel('X1'); plt.ylabel('X2')
#     plt.show()
# def classifyall(datatest,w):
#     predict=[]
#     for data in datatest:
#         result=classify(data,w)
#         predict.append(result)
#     return predict
def main():


    (X,Y)=Data_Prepro('18_train.txt')
    W_pocket = Pocket_Algo(X, Y, 1000)

    # trainData,label=createTrainDataSet()
    # testdata=createTestDataSet()
    # w=pla(trainData,label)
    # result=classifyall(testdata,w)
    # plotBestFit(w)
    print(getErrorNum(X,Y,W_pocket))
    print (W_pocket)
if __name__=='__main__':
    start = time.clock()
    main()

    end = time.clock()
    print('finish all in %s' % str(end - start))


