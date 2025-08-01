def findSol(n):
    k = str(n) # 變成字串
    # len_n = len(k) # 有幾個數字
    odd = 0 # 設奇數0, 因為還未加任何數
    even = 0 # 設偶數0
    # oddnumber = n[0:len_n:2]
    # evennumber = n[1:len_n:2]
    for i in range(0,len(k)):
        if i % 2 == 0: # 基數個
            odd = odd + (n//(len(k)*10))
        else:
            even = even + (n//((len(k)-1)*10)
        n = n//10
    print("odd : ",odd)
    print("even : ", even)

def main():
    n = int(input()) # 輸入整數n
    findSol(n)

if __name__ == '__main__':
    main()