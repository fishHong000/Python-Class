# 學號：108213010
# 姓名：洪瑄妤
def main():
    # 輸入
    a = float(input())
    b = float(input())
    c = float(input())
    # 印出一元二次方程式
    print((((-b)+(b**2-(4*a*c))**0.5)/(2*a)), (((-b)-(b**2-(4*a*c))**0.5)/(2*a)))
if __name__ == "__main__" :
    main()