# 排列問題
# 給一個list, 請列出其中n個元素的所有排列
# 想像一下, 你手中有2個容器, 一個是可選的容器, 一個是別人幫你事先選好的元素
# 如何由A取出n個元素的所有排列?
# 方法如下
# 由A任選一個元素, 並把A-1,B+1,n-1丟給另外m位同學請他列出所有的排列

# eg ABCDE
# A開頭BCDE的排列, or
# B開頭ACDE的排列, or
# C開頭ABDE的排列, or
# D開頭ABCD的排列, or
# E開頭ABCD的排列

# 有一個神奇的運算式
#  ? ?
#  * ?
#-------
#  ? ?
#+ ? ?
#-------
#  ? ?
def magicExp(data):
    return(data[0]*10+data[1])*data[2] == (data[3]*10+data[4]) and \
           ((data[3]*10+data[4])+(data[5]*10+data[6]))==(data[7]*10+data[8])
def findSol():
    myPerm([i for i in range(1,10)],[],9,magicExp)

def comb(data,n): # 由data任取n個組合
    myComb(data,[],n)

def myComb(data,got,n):
    if n == 0: # 如果都選完了
        print(*got) # 印出來
        return
    for pos in range(len(data)): # 選data中位置在pos的元素
        # 再請同學選剩下的n-1個元素
        myComb(data[pos+1:],got+[data[pos]],n-1)

def perm(data,n): # 由data任取n個的排列
    myPerm(data,[],n)
# data是可選的元素
# got是別人幫忙選好的元素
# n是我負責要選的個數
def myPerm(data,got,n):
    if n == 0: # 如果都選完了
        print(*got) # 印出來
        return
    for i in range(len(data)): # 任選data中的一個元素
        # 再請同學選剩下的n-1個元素
        myPerm(data[0:i]+data[i+1:],got+[data[i]],n-1)

def main():
    perm('ABCDE',3)

if __name__ == '__main__':
    main()