def findSol(n,data):
    # 創一個board->每個位置都是True的棋盤
    board = [[True for i in range(n)] for j in range(n)]
    # 設起點位置x=0,y=0, pos用來計算幾塊區域, num用來計算走幾步
    return mySol(n,data,board,0,0,0,[[0,-1],[-1,0],[0,1],[1,0]]) # 左上右下與目前位置的座標差

def mySol(n,data,board,num,x,y,direction):
    # 終止條件->走完全部->結束, 印出有幾個區塊
    if num == n*n:
        return
    numSol = 0
    for c in range(4):
        if y+direction[c][0]>=0 and y+direction[c][0]<=n-1 and x+direction[c][1]>=0 and x+direction[c][1]<=n-1:
            # 判斷要走的位置是否可以走
            if board[y+direction[c][0]][x+direction[c][1]] and int(data[(y+direction[c][0])%5 + (x+direction[c][1])*5]) == int(data[y%5 + x*5]):
                # 走過的位置標記走過(False)
                board[y+direction[c][0]][x+direction[c][1]] = False
                # 加上找出的走法
                numSol = numSol + mySol(n,data,board,num+1,x+direction[c][1],y+direction[c][0],direction)
    return numSol

def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int,input().split())))
    print(findSol(n,data))

if __name__ == '__main__':
    main()