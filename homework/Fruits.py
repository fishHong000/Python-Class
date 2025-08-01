    # money:身上有多少錢, n:要買的數量, species:水果種類
    # price:每一種水果的單價
    # got:每種水果已經買好的數量
    # pos:我要負責買的種類

def findSol(money,n,species,price):
    mySol(money,n,species,price,[],0)

def mySol(money,n,species,price,got,pos):
    if pos == species:
        if n == 0:
            print(*got)
        return
    # 請問pos種水果可以買多少個?
    for i in range(min(n, money//price[pos]),-1,-1) :
        mySol(money-(price[pos]*i), n-i, species, price, got+[i], pos+1)

def main():
    money, n, species = map(int,input().split())
    price = list(map(int,input().split()))
    if min(price)*n > money:
        print('無法買滿')
    else:
        findSol(money,n,species,price)

if __name__ == '__main__':
    main()