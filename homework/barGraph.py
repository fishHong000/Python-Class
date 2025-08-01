# 學號：108213010 姓名：洪瑄妤
def bar(n,values):
    # 縱
    # max(values)是輸入數值中最大的數
    # 上至下, 由大到小, 長度是最大數+2
    for r in range(max(values)+2, 0, -1):
        # z.fill(2)->如果數字不滿2位數, 用0補足至2位數
        print(str(r).zfill(2),end = ' ')
        # 橫
        for c in range(n):
            if values[c] >= r : # 如果輸入的值>=r, 就印出##, 意思是畫出直條的長度
                print('##',end = ' ')
            else : # 不是的話, 印出.., 表示空的
                print('..',end = ' ')
        print()
    # 印出最下面那排數字, 由1~n, 不足2位數補0, 後面空一格
    print(*[str(c).zfill(2) for c in range(n+1)],end = ' \n') # end = ' '

def main():
    n = int(input()) # 表示有幾個數字要印在長條圖
    values = list(map(int,input().split())) # 在長條圖上顯示的數值
    bar(n,values)

if __name__ == '__main__' :
    main()