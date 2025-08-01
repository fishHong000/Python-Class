def printTornado(n,dir,board):
    r,c = n//2,n//2
    rDif,cDif = [0,-1,0,1],[0,-1,0,1]
    # 印出第1個數字, 並標示不能走了
    board[r][c] = 1
    # 再印出剩下的2~n*n個數字
    # l=0, u=1, r=2, d=3
    if dir[1] == 'l':
        dir[1] = 0 # 字串可直接轉數字
    if dir[1] == 'u':
        dir[1] = 1
    if dir[1] == 'r':
        dir[1] = 2
    if dir[1] == 'd':
        dir[1] = 3
    for num in range(2,n*n+1):
        if dir[0] == 'c':
        # 先跳到下一個位置(因為最一開始站在正中間，因此沒辦法判斷轉向)
        # 再該位置填入數字
        # 檢查 當前位置的 下一個"方向"，是否可以走過去(填數字)
            # 如果可以，就把當前前進的方向，改成下一個方向

def main():
    n = int(input())
    dir = input().split() # 不用轉型, 所以不需要map
    board = [[0 for i in range(n)] for j in range(n)]
    printTornado(n,dir,board)

if __name__ == '__main__':
    main()