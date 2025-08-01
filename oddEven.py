# 學號：108213010 姓名：洪瑄妤
def findSol(n):
    k = str(n) # 將N變成字串
    oddnum = k[0::2] # 從中取出奇數位置
    evennum = k[1::2] # 從中取出偶數位置
    odd = 0 # 因為都還沒加起來，所以設為0
    even = 0
    for i in range (len(oddnum)): # 把所有奇數位置的數字加起來
        odd = odd + int(oddnum[i])
        
    for j in range(len(evennum)): # 把所有偶數位置的數字加起來
        even = even + int(evennum[j])
        
    print("odd :",odd) # 印出相加結果
    print("even :",even)
    
def main():
    n = int(input()) # 輸入整數n
    findSol(n)

if __name__ == '__main__':
    main()