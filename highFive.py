# 印出來
def show(n,board):
    sol = 0
    for r in range(n):
        for c in range(n):
            if board[r][c] == '@':
                sol += 1
        print(sol)
        for data in board:
            print(*data)
# 判斷質數
# 判斷周圍
def findSol(n,m,data):
    # 上'下'左'右'左上'右上'左下
    dire = [[-1,0],[1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]
    for pos in data:
        # 周圍有多少個位置
        num = 0
        # 周圍位置的座標
        put = []
        # 加上中心位置
        put.append(pos)
        # 判斷8個方位
        for dic in dire:
            # 穿牆
            newr, newc = (pos[0]+dir[0]) % n, (pos[1]+dir[1]) % n
            # 因為如果前面判斷的時候
            if board[newr][newc] == '@' or board[newr][newc] == '#':
                num += 1
                put.append([newr,newc])
        if num in [2,3,5,7]:
            for i in put:
                board[i[0]][i[1]] = '#'

def prepare(n,m,data):
    board = [['X' for i in range(n)] for j in range(n)]
    for pos in data:
        board[pos[0]][pos[1]] = '@'

def main():
    n = int(input())
    m = int(input())
    data = []
    for i in range(m):
        data.append(list(map(int,input().split())))

if __name__ == '__main__':
    main()