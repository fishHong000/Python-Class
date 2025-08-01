# 108213010 洪瑄妤
def isPrime(n):
    for i in range(2, n):
        if n % i == 0: # 整除, i是n的因數, 所以n不是質數
            return False
    return True # 都沒有數字能整除, 所以n是質數

n = int(input()) # 得到輸入值n

def main():
    for i in range(2, n + 1): # 產生2到n的數字
        i_isPrime = isPrime(i) # 判斷i是否為質數
        if i_isPrime: # 如果是, 印出來
            print(i)

if __name__=='__main__':
    main()