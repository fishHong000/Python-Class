# 費氏數列
# 定義:
# F(0) = 0, F(1) = 1
# F(n) = F(n-1)+F(n-2)
# 0,1,1,2,3,5,8,13,21,34,55
# 寫一函數來計算費氏數
# 使用recursion的寫法
def F(n):
    if n <= 1:
        return n
    return F(n-1)+F(n-2) # 這不是呼叫自己! 是呼叫同學啦

if __name__ == '__main__':
    print(F(int(input())))