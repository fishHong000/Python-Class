def mymaze(n,data,beginX,beginY,finalPos):
    #建立每一個點與原點之間的距離
    #因此合法的距離最小為1
    distance = [[0 for j in range(n)]for i in range(n)]
    #checklist存放要處理的點，一開始只有起點
    checklist,distance[beginX][beginY] = [[beginX,beginY]],1
    #還有點要處理
    while len(checklist) != 0:
        [r,c] = checklist.pop(0) #拿出最前面還沒處理的點
        if finalPos[0] == r and finalPos[1] == c: #抵達終點了
            return distance[r][c]
        for [rdif,cdif] in [[1,0],[-1,0],[0,1],[0,-1]]:
            nextr,nextc = r+rdif,c+cdif
            if nextr<0 or nextr >= n or nextc<0 or nextc >= n: #超過邊界
                continue #跳過此點
            if data[nextr][nextc] == 0 and distance[nextr][nextc] == 0:
                distance[nextr][nextc] = distance[r][c]+1
                checklist.append([nextr,nextc])
    return n*n

def main():
    #整數n 表示地圖的大小為 n*n
    n = int(input())
    data = []
    #依序輸入迷宮
    for i in range(n):
        data.append(list(map(int,input().split())))
    #起始座標
    beginX,beginY = map(int,input().split())
    #終點座標
    finalPos = list(map(int,input().split()))
    # direc = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    print(mymaze(n,data,beginX,beginY,finalPos))

if __name__ == "__main__":
    main()