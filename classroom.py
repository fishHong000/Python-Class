# 學號:108213010 姓名:洪瑄妤
def count(n,grade,number,got): # 計算教室內被點到低於3次(不包含3)的學生
    # 開始來計算
    for i in range(len(grade)):
        # 未滿3分的話
        if grade[i] < 3:
            # 人數+1
            number = number + 1
            # 把那個座位號碼加進got
            got.append(i+1)
    # 如果未滿5人(達到目標)
    if number < 5:
        print(*got)
    # 沒有的話就繼續輸入座位號碼
    else:
        cross(n,int(input()),grade)

def cross(n,call,grade): # 玩大十字(算大家被點名的次數)
    # 大十字加分
    # 橫的
    for i in range(0,(n*n)):
        # 把i跟(輸入的座號-1)都去除n
        # 商數一樣的話, 代表同橫行
        if i//n == (call-1)//n:
            # 那個座位就+1
            grade[i] = grade[i]+1
    # 直的
    for j in range(0,n*n):
        # 把i跟(輸入的座號-1)都去除
        # 餘數一樣的話, 代表同直行
        if j%n == (call-1)%n:
            # 那個座位就+1
            grade[j] = grade[j]+1
    # 因為本身會重複算一次, 所以扣掉
    grade[call-1] = grade[call-1] - 1
    # 每次加分完就檢查不到3分的人有多少
    count(n,grade,0,[])

def main():
    # n表示教室大小 n*n
    n = int(input())
    # 計算每個座位加了幾分
    grade = [0 for i in range(n*n)]
    # 輸入被點到的座號
    cross(n,int(input()),grade)

if __name__ == '__main__':
    main()