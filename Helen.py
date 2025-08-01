def main():# 輸入三角形的三個邊長a,b,c
    a = float(input())
    b = float(input())
    c = float(input())
    # 使用海龍公式求解
    s = (a+b+c)/2
    print((s*(s-a)*(s-b)*(s-c)) ** 0.5)
if __name__ == "__main__":
    main()