def count(P,M,N):
    
    firstsum = 0
    i = 3
    while i <= P:
        firstsum = firstsum + i
        i = i + 2
    
    secondsum = 0
    j = 0
    while j <= (M-1):
        secondsum = secondsum + (j*2)
        j = j + 1

    thirdsum = 0
    k = 1
    while k <= 45:
        thirdsum = thirdsum + (k*3)
        k = k +1

    total = 0
    total = firstsum+secondsum+thirdsum
    print(total)

def main():
    P = 50
    M = 50
    N = 45
    count(P,M,N)

if __name__ == "__main__":
    main()