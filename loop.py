# 學號：108213010 姓名：洪瑄妤
def isPrime(n):
    # 定義:除了1和n, 都不能整除n, 則n為prime
    div = 2
    while div < n:
        if n % div == 0: # 可以整除1, 那就不是prime
            return False
        div = div + 1 # 測試下一個數字
    return True # 2~n-1都不能整除, 所以是prime

def genPrime(begin, end):
    if begin>end:
        begin,end = end,begin
    n = begin
    while n <= end:
        yield n
        n = n + 1

def main():
    begin = int(input())
    end = int(input())
    for v in genPrime(begin,end): # for v in range(1,11,2)->跳一個數字輸出
        if isPrime(v):
            print(v)

if __name__ == '__main__':
    main()