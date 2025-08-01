# 學號:108213010 姓名:洪瑄妤
def run(data,n,k):
    # 終止條件
    if n <= 0 :
        if n == 0 :
            print(*k)
        return # 終止函數
    # 在data數列中
    for i in range(len(data)):
        # data第二個位置開始跑, n減已跑的距離, k加入已跑的距離
        run(data[i+1:], n-data[i], k+[data[i]])

def main():
    # 要跑n距離
    n = int(input())
    # 每個同學能跑的距離
    data = list(map(int,input().split()))
    # 執行run
    run(data,n,[])

if __name__ == '__main__' :
    main()