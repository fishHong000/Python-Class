# 河內塔問題Tower of Hanoi problem
# 有3根柱子
# 有n個大小不同, 中間有洞的碟子
# 一開始所有碟子都在同一根柱子上, 且大的在下方
# 請問限制一次只能移動一個碟子, 且大的一定要在下面
# 要如何移動才能把所有碟子移動到目標位置
# 例如由A柱移到B柱
# 假設有個"神奇"的函數可以幫我把n個碟子, 由A柱移到B柱
def move(n,source,dest,third):
    # 請問甚麼條件下, 已經完成工作?
    if n == 0:
        return
    # 叫某同學幫忙把上面n-1個碟子由source搬到third
    move(n-1,source,third,dest)
    # 然後把最後一個留在source上的碟子搬到dest
    print(source,'-->',dest)
    # 最後叫某同學幫忙把上面n-1個碟子由third搬到dest
    move(n-1,third,dest,source)

if __name__ == '__main__':
    move(int(input()),'A','B','C')