# 學號:108213010 姓名:洪瑄妤
def perm(cats, result, DoNotTogether, n):
    # 終止條件
    if n == 0:
        print(*result)
        return
    for i in range(len(cats)):
        # len(result)==0 用來判斷是不是第一次進遞迴
        # result[-1]代表倒數第一個位置
        if len(result) == 0 or (result[-1] not in DoNotTogether \
        or cats[i] not in DoNotTogether):
            perm(cats[0:i]+cats[i+1:], result+[cats[i]], DoNotTogether, n-1)
            # result+[]<--記得加[]

def main():
    # n->想排的貓咪數量, m->有幾隻貓不能排在一起
    n, m = map(int, input().split())
    # m隻貓咪的名字
    DoNotTogether = list(input().split())
    # 所有貓的list
    cats = ['鯊魚','hero','mia','黑貓','miu','mogan','mori','melo','小貓']
    # 排隊拍照去
    perm(cats, [], DoNotTogether, n)

if __name__ == '__main__':
    main()