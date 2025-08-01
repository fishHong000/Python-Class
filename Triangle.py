# 學號：108213010 姓名：洪瑄妤
def triangle(a,b,c):
    # 判斷哪種類型的三角形
    if a+b > c :
        if (a**2) + (b**2) == (c**2) :
            print('Right')
        if (a**2) + (b**2) < (c**2) :
            print('Obtuse')
        if (a**2) + (b**2) > (c**2) :
            print('Acute')
    else : # 如果a+b<=c，非三角形
        print('No')

def main():
    # 輸入三邊長a,b,c
    a = int(input())
    b = int(input())
    c = int(input())
    # 邊長由小到大排列
    if a>b and b<c and c>a:
        a,b,c = b,a,c
    if a>b and a>c :
        a,b,c = c,b,a
    if b>a and b>c :
        a,b,c = a,c,b
    # 先印出邊長
    print(a,b,c)
    triangle(a,b,c)
    
if __name__ == '__main__':
    main()