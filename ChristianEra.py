def main():
    return year%400==0 or (year%100!=0 and year%4==0)

def sort3(a,b,c):
    if a > b:
        a,b = b,a
    if a > c:
        a,c = c,a
    if b > c:
        b,c = c,b
    return a,b,c

def main():
    a,b,c = sort3(int(input()), int(input()), int(input()))
    print(a,b,c)

if __name__ == "__main__" :
    main()