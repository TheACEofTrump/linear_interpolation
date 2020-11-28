def doubleInterpolation(x1,x2,x,y1,y2,y,z11,z21,z12,z22):
    def interpolation(x1,x2,y1,y2,x):
        return (x-x1)*(y2-y1)/(x2-x1)+y1
    return interpolation(y1,y2,interpolation(x1,x2,z11,z21,x),interpolation(x1,x2,z12,z22,x),y)

print('双线性插值')
x1 = eval(input('x1值：'))
x2 = eval(input('x2值：'))
x = eval(input('x坐标待插值：'))
if not (x1<=x<=x2 or x1>=x>=x2):
    print('警告：给定的x轴待插值不在坐标范围内。')
y1 = eval(input('y1值：'))
y2 = eval(input('y2值：'))
y = eval(input('y轴待插值：'))
if not (y1<=y<=y2 or y1>=y>=y2):
    print('警告：给定的y轴待插值不在坐标范围内。')
z11 = eval(input('(x1,y1)函数值：'))
z21 = eval(input('(x2,y1)函数值：'))
z12 = eval(input('(x1,y2)函数值：'))
z22 = eval(input('(x2,y2)函数值：'))
print('插值结果：',doubleInterpolation(x1,x2,x,y1,y2,y,z11,z21,z12,z22))
