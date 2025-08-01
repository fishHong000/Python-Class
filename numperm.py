#  ?????
# - ????
#--------
#  ?????

def magicExp(data,target):
    return (data[0]*10000+data[1]*1000+data[2]*100+data[3]*10+data[4]) - \
           (data[5]*1000+data[6]*100+data[7]*10+data[8]) == target

def findSol(target):
    myPerm([i for i in range(1,10)], [], 9, magicExp, target)

def myPerm(data,got,n,valid,target):
    if n == 0: # 如果都選完了
        if valid(got,target):
            print(*got) # 印出來
        return
    for pos in range(len(data)): # 任選data中的一個元素
        # 再請同學選剩下的n-1個元素
        myPerm(data[0:pos]+data[pos+1:],got+[data[pos]],n-1,valid,target)

def main():
    findSol(int(input()))

if __name__ == '__main__':
    main()