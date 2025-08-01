def findSol(n,things,price,m): # 由data任取n個的排列
    return myfindSol(n,things,price,m,[0 for i in range(n)],[0,0],'  ')

# times : 每個裝飾品的使用次數
# balance : balance[0]代表奇數層,[1]偶數層

def checkTimes(times):
    for v in times:
        if v == 0:
            return False
    return True

def checkBalance(n,balance):
    if max(balance) - min(balance) > n*100 :
        return False
    return True 

def myfindSol(n,things,price,m,times,balance,choose):
    if m == 0: # 如果都選完了
        if checkTimes(times) and checkBalance(n,balance):
            return 1
        return 0 
    ans = 0
    for i in range(n):
        # 不能和上一層拿的東西顏色或種類重複
        if choose[0] != things[i][0] and choose[1] != things[i][1]:
            times[i] = times[i] + 1
            balance[m%2] = balance[m%2] + price[i]
            ans = ans + myfindSol(n,things,price,m-1,times,balance,things[i])
            times[i] = times[i] - 1
            balance[m%2] = balance[m%2] - price[i]
    return ans

def main():
    # 第一行輸入整數n，代表有n種裝飾品
    n = int(input())
    # 第二行輸入n個裝飾品，每個裝飾品由兩個字元組成，裝飾品與裝飾品之間用空格區分
    things = input().split()
    # 第三行輸入n個裝飾品的價格
    price = list(map(int,input().split()))
    # 第四行輸入整數m，代表聖誕樹有m層要裝飾
    m = int(input())
    print(findSol(n,things,price,m))

main()