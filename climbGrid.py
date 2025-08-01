def findSol(n,countLine,end):
    return myFindSol(n,countLine,end,[i for i in range(n)])
# v:直線數
# h:橫線數
# end:最後的結果
# current:目前的排法
def myFindSol(v,h,end,current):
    if h == 0: # 沒得換了
        if end == current: # 找到一組解
            return 1
        return 0
    sol = 0 # 找到幾解
    for pos in range(v-1): # 任選兩組相鄰直線加上橫線
        current[pos],current[pos+1] = current[pos+1],current[pos]
        sol += myFindSol(v,h-1,end,current)
        current[pos],current[pos+1] = current[pos+1],current[pos]
    return sol
# n:直線數
# countLine:橫線數
# end:最後的結果
# current:目前的排法
def main():
    n, countLine = map(int,input().split())
    end = list(map(int,input().split()))
    print(findSol(n,countLine,end))

if __name__ == '__main__':
    main()