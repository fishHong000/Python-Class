def square(n):
    data = [[0 for c in range(n)] for r in range(n)] # data → [[.....],[.....],[.....],.....]
    r, c = 0, n//2 # 最上方正中央
    data[r][c] = 1
    for num in range(2,n*n+1):
        nextR,nextC = r-1,c+1 # 原位置右上
        if nextR < 0: # 如果超過最上面
            nextR = n-1 # 移到最下面
            
        if nextC >= n: # 如果超過最右邊
            nextC = 0 # 移到最左邊
            
        if data[nextR][nextC] != 0: # 如果那個位置有數字了
            nextR,nextC = r+1,c # 原位置下面
        data[nextR][nextC] = num # 填入目前數字
        r,c = nextR,nextC # 移動位置
    return data

def printTornado(n,board,d):
    #r,c代表目前所在的位置，一開始在正中央
    #allow代表方陣的某位置是否可以走過去，一開始都可以走，所以填True
    r,c,allow = n//2,n//2,[[True for j in range(n)] for i in range(n)]
    # 印出第一個數字，並標示可以走了
    print(board[r][c],end=' ')
    allow[r][c] = False
    
    rDif,cDif=[0,-1,0,1],[-1,0,1,0] # 左上右下與目前位置的座標差
    
    # 再印出剩下的2~n*n個數字
    for num in range(2,n*n+1):
        if allow[r+rDif[d]][c+cDif[d]] : # 如果可以走過去,走過去並轉彎看能不能走
            r,c,d=r+rDif[d],c+cDif[d],(d+1)%4
        else : # 否則改走原來的方向
            r,c=r+rDif[(d-1)%4],c+cDif[(d-1)%4]
        # 印出並標示不能走了
        print(board[r][c],end=' ')
        allow[r][c] = False

def main():
    n = int(input())
    d = int(input())
    square(n)
    printTornado(n,square(n),d)

main()