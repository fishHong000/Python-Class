# 印出大小為n的正方形
# n = 4
#    *     1
#   ***    3
#  *****   5
# *******  7
#  *****   5
#   ***    3
#    *     1
# 第line行怎印? line 1~n
def main():
    n = int(input())
    # 一共有1~n行
    line = 1
    while line <= n:
        # 第line行有n-line個' '+line個'*'
        print(' '*(n-line)+'*'*(2*line-1))
        line = line + 1
    line = n - 1
    while line >= 1:
        print(' '*(n-line)+'*'*(2*line-1))
        line = line - 1

if __name__ == '__main__':
    main()