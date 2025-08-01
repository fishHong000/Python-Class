def printTornado(n,board,d):
    # r,c代表目前所在位置, 一開始在正中央
    # allow代表方陣的某位置是否可以走過去, 一開始都可以走, 所以填True
    r,c,allow = n//2,n//2,[[True for j in range(n)] for i in range(n)]
    rDif,cDif = [0,-1,0,1],[-1,0,1,0] # 左上右下與目前位置的座標差
    # 印出第1個數字, 並標示不可以走了
    print(board[r][c],end = ' ')
    allow[r][c] = False
    # 再印出剩下的2~n*n個數字
    for num in range(2,n*n+1):
        if allow[r+rDif[d]][c+cDif[d]] : # 如果可以走過去
            r,c,d = r+rDif[d],c+cDif[(d-1)%4],d+1
        # 印出並標示不能走了
        print(board[r][c],end = ' ')
        allow[r][c] = False

def main():
    # 讀入奇數n
    n = int(input())
    # 讀入方向dir
    d = int(input())
    # 產生大小為n的奇數魔方陣
    # 由方向
    printTornado(n,board,d)

if __name__ == '__main__':
    main()