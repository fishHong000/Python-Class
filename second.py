def F(n):
    if n <= 1:
        return n
    return F(n-1)+F(n-2)

if __name__ == '__main__':
    print(F(int(input())))