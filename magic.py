# r,c 代表row和column
# 在list of list裡面, 習慣上第一個index當row, 第二個index當column
# data[r][c]
# 我們習慣把(0,0)當左上角, 向下r+1, 向右c+1
# 1放在中間正上方
# 2~n*n放在跟前一個數字"相關"的位置
# 先找前一個(currentR,currentC)的右上方(r,c)
# r = currentR-1,c = currentC+1
# 如果r<0, 則let r = n-1, 也就是找最下面
# 如果c>=n, 則let c = 0, 也就是到最左邊
# 如果data[r][c]沒有填過, 就填到data[r][c]
# 否則填到data[currentR+1][currentC]

# generate Odd Magic Matrix
# return list of list
def genOddMagic(n):
    data = [[0 for c in range(n)] for r in range(n)] # 先用0填滿
    r,c = 0,n//2 # 最上方正中央, 前一個填的位置
    data[r][c] = 1 # 先填入1
    for num in range(2,n*n+1): # 依序填入數字2~n*n
        nextR,nextC = r-1,c+1 # 原位置右上
        if nextR < 0: # 超過上邊界
            nextR = n-1 # 移到最下面
        if nextC >= n: # 超過右邊界
            nextC = 0 # 移到最左邊
        if data[nextR][nextC] != 0: # 已經填過了
            nextR,next = r+1,c # 原位置下面
        data[nextR][nextC] = num # 把數字填進去
        r,c = nextR,nextC # 移動位置
    return data

def printByRow(data):
    for r in data:
        for v in r:
            print(str(v).rjust(2,' '),end=' ')
        print()

def main():
    board = genOddMagic(int(input()))
    printByRow(board)

if __name__ == '__main__':
    main()