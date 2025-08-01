
import matplotlib.pyplot as plt
# size要印出的地毯大小
def Fractal(size):
    plotx,ploty=[],[]
    myFractal(size,0,0,plotx,ploty)
    plt.plot(plotx,ploty,'o')
    plt.show()

# 需要..
# size: list of
# ploty: list of 要畫的點y
def myFractal(size,x,y,plotx,ploty):
    # 多大的地毯一個人就可以畫了?
    if size == 1:
        plotx.append(x)
        ploty.append(y)
        return
    # 如果一個人不能畫, 怎處理?
    # 找八個同學畫地毯啊
    # 123
    # 4 5
    # 678
    myFractal(size//3,x,y,plotx,ploty)
    myFractal(size//3,x+size//3,y,plotx,ploty)
    myFractal(size//3,x+2*size//3,y,plotx,ploty)
    myFractal(size//3,x+2*size//3,y+size//3,plotx,ploty)
    myFractal(size//3,x+2*size//3,y+2*size//3,plotx,ploty)
    myFractal(size//3,x+size//3,y+2*size//3,plotx,ploty)
    myFractal(size//3,x,y+2*size//3,plotx,ploty)
    myFractal(size//3,x,y+size//3,plotx,ploty)

def main():
    Fractal(3**4)

main()