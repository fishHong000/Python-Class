def isPrime(n):
    # 定義:除了1和n, 都不能整除n, 則n為prime
    div = 2
    while div < n:
        if n % div == 0: # 可以整除2, 那就不是prime
            return False
        div = div + 1 # 測試下一個數字
    return True # 2~n-1都不能整除, 所以是prime

def countPrime(n):
    # 你問我<=n有幾個prime
    # 那就2~n一個一個試阿
    found = 0 # 找到幾個了
    testNum = 2 # 要測試的數字
    while testNum <= n:
        if isPrime(testNum): # 找到一個質數
            found = found + 1
        testNum = testNum + 1
    return found

def main():
    n = int(input()) # 讀入>=2的整數
    # 請問n是否為質數(prime number)
    print(isPrime(n))

if __name__ == "__main__" :
    main()