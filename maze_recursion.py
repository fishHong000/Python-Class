def mymaze(n, data, r, c, end, count, ans):
    if r == end[0] and c == end[1]:
        ans.append(count)
        return ans
    for dictr, dictc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nextr, nextc = r+dictr, c+dictc
        if 0 <= nextr < n and 0 <= nextc < n and data[nextr][nextc] == 0:
            data[nextr][nextc] = 1
            mymaze(n, data, nextr, nextc, end, count+1, ans)
            data[nextr][nextc] = 0

def main():
    #整數n 表示地圖的大小為 n*n
    n = int(input())
    data = []
    #依序輸入迷宮
    for i in range(n):
        data.append(list(map(int, input().split())))
    #起始座標
    start = list(map(int, input().split()))
    #終點座標
    ans = []
    end = list(map(int, input().split()))
    mymaze(n, data, start[0], start[1], end, 1, ans)
    print(min(ans))
if __name__ == "__main__":
    main()