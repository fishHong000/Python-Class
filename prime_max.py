# 108213024
# 侯傑森

def isPrime(n):
    # 定義: 除了1和n，都不能整除n，則n為prime
    div = 2
    while div*div <= n :
        if n % div == 0: #可以整除，那就不是prime
            return False    
        div = div + 1 # 試下一個數字
    return n

def findMax(i,j):
    current = i # 正在處理的數字
    maxNum = 0 # 已知的最大值，先設最小
    while current <= j:
        if maxNum < isPrime(current) :
            maxNum = isPrime(current)
        current = current + 1
    return maxNum





def main():
    i = int(input())
    j = int(input())
    if i > j:
        i, j = j, i
    print(i,j,findMax(i,j))
if __name__ == '__main__':
    main()