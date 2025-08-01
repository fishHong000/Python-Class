# lines: list of [int,int], 所有線段清單
# return coverage of all lines
def findSol(lines):
    # 先將lines依照起點做排序
    lines.sort()
    # length: 覆蓋的總長度
    # begin: 目前線段的起點
    # end: 目前線段的終點
    length, begin, end = 0, 0, 0
    # 起點由小到大依序處理
    for line in lines: # 為什麼是line
        # 仔細想想, 只有兩種狀況, 重疊, 不重疊
        if line[0] <= end:
            # end向右延伸
            end = max(end,line[1])
        else: # 不重疊
        # 直接算線段長度
        # 再把begin, end設為正在檢查的線段兩端
            length,begin,end = length+end-begin,line[0],line[1]
    # 計算最後一個線段
    length = length + end - begin
    # 傳回length
    return length

def main():
    data = []
    # 使用[int,int]來表達一個線段
    for i in range(int(input())):
        data.append(list(map(int,input().split())))
    print(findSol(data))

if __name__ == '__main__':
    main()