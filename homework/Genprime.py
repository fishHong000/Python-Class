# 學號：108213010 姓名：洪瑄妤
def isPrime(n):
    for i in range(2, n):
        if n % i == 0: # 如果可以整除, i是n的因數, 所以n不是質數
            return False
    return True # 都沒有數字能整除, 所以n是質數

def main():
    n = int(input()) # 輸入整數n。
    num = 2 # 設第一個質數num=2
    while n >= num : # 當n>=num, 還能整除的情況下
        if isPrime(num) and n % num == 0: # 如果num是質數, 而且n能被num整除
            n = n//num # 把n除掉
            print(num) # 印出質數num
        else: # 不符合if的條件
            num = num + 1 # num加一, 找下一個數字試試看

if __name__=='__main__':
    main()