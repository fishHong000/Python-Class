# 學號：108213010 姓名：洪瑄妤
def reverse(k):
    k = k + int(str(k)[::-1]) # 加上和自己相反的數字
    num = 1 # 用來數數字相反了幾次
    while k != int(str(k)[::-1]): # 當k不等於和自己數字相反的數字
        k = k + int(str(k)[::-1]) # 就加上和自己相反的數字
        num += 1 # 相反的總次數加一
    print(num, k) # 印出總共相反幾次跟數字k

def main():
    n = int(input()) # 要測n個數字
    for i in range(n): # 輸入n個數字
        k = int(input())
        reverse(k) # 包一個函數

if __name__ == '__main__' :
    main()