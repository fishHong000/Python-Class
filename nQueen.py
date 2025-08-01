# n皇后問題
# 把座標(0,0)放在左上角, 向右column+1, 向下row+1
# row是第一個索引, column是第二個索引
# 有n幾個直線, n橫線, 2n-1右上斜線, 2n-1右下斜線
# 給一個位置(x,y), 請問這個位置是在哪一條直橫右上斜右下斜的線上?
# 哪條直線? c
# 哪條橫線? r
# 哪條右上斜? r+c
# 哪條右下斜? r-c+(n-1)

# 找出n皇后問題有幾解
def findSol(n):
    return mySol(n,0,[True for i in range(n)],[True for i in range(2*n-1)],[True for i in range(2*n-1)],[[' 0' for c in range(n)] for d in range(n)])
# n: 幾皇后問題
# r: 你要負責的r編號
# Vok: list,某直線是否可以放
# Uok: list,某右上斜線是否可以放
# Dok: list,某右下斜線是否可以放
def mySol(n,r,Vok,Uok,Dok,board):
    if n == r: # 好棒棒, 已經擺上n皇后
        for d in board :
            print(*d)
        print('---------------')
        return # 這是一組解
    if n == 2 or n == 3 or n < 1 :
        print('找不到解')
        return
    for c in range(n): # r這個row上面的每個column c都試試看
        if Vok[c] and Uok[r+c] and Dok[r-c+n-1]: # 直,上斜,右下斜都可以放
            Vok[c],Uok[r+c],Dok[r-c+n-1] = False,False,False # 標示三條線都不能放
            board[r][c] = ' 1'
            mySol(n,r+1,Vok,Uok,Dok,board)
            Vok[c],Uok[r+c],Dok[r-c+n-1] = True,True,True # 回復原資料
            board[r][c] = ' 0'

def main():
    findSol(int(input()))

main()