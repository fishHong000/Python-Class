def findSol(n,m,x,y):
    # 2->r:用來數是否填完了(因為第一步就是最初的位置, 所以從第二步開始走)/[]->direction
    # 創一個board->每個位置都是True的棋盤
    board = [[True for i in range(m)] for j in range(n)]
    # 起始點標註成已經走過(False)
    board[y][x] = False
    return mySol(n,m,x,y,2,board,[[-1,-2],[-1,2],[1,-2],[1,2],[-2,-1],[-2,1],[2,-1],[2,1]])

def mySol(n,m,x,y,r,board,direction):
    # 終止條件
    if r == (n*m)+1:
        return 1 # 找到一組解
    numSol = 0
    for c in range(8):
        # 判斷要走的位置是否在範圍內
        if y+direction[c][0]>=0 and y+direction[c][0]<=n-1 and x+direction[c][1]>=0 and x+direction[c][1]<=m-1:
            # 判斷要走的位置是否可以走
            if board[y+direction[c][0]][x+direction[c][1]]:
                # 走過的位置標記走過(False)
                board[y+direction[c][0]][x+direction[c][1]] = False
                # 加上找出的走法
                numSol = numSol + mySol(n,m,x+direction[c][1],y+direction[c][0],r+1,board,direction)
                # 回復原資料
                board[y+direction[c][0]][x+direction[c][1]] = True
    return numSol

def main():
    n,m,x,y = map(int,input().split())
    print(findSol(n,m,x,y),'種走法')

if __name__ == '__main__':
    main()