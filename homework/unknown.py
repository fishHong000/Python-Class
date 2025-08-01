# 學號:108213010 姓名:洪瑄妤
#  1?3?
#* ?4?5
#--------
# 7?8?9
# data由三個字串合成, first代表第一個字串的長度, second代表第二個字串的長度
# pos是我該負責的位置
def mySol(data,first,second,pos):
    if pos == len(data): # 都填完了
        # check and return
        firstnum = data[0:first] # 第一個數字->data的第0到第first-1的位置
        secondnum = data[first:first+second] # 第二個數字
        answer = data[first+second:] # 答案
        if (int(firstnum)*int(secondnum)==int(answer)): # 如果塞入的數字符合輸入的算式
            # print(int(firstnum),'*',int(secondnum),'=',int(answer)) # 印出
            print('{} * {} = {}'.format(firstnum, int(secondnum), answer))
        return
    if data[pos] != '?': # 如果不是'?'
        mySol(data,first,second,pos+1) # 就直接換下一個位置
        return # 要記得打->不然非問號的位置也會被換掉
    for i in range(10): # 數字0~9要跑
        mySol(data[:pos] + str(i) + data[pos+1:],first,second,pos+1) # 把要換成數字的位置拿掉填入str(i)

def findSol(data,first,second):
    mySol(data,first,second,0) # 再弄一個函數比較好看, 因為不是在main產生的東西

def main():
    x,y,z = input().split() # .split()->這樣才能用空白間隔, 打成一行
    findSol(x+y+z,len(x),len(y))

if __name__ == '__main__':
    main()