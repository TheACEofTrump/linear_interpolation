def interpolation(x1,x2,y1,y2,x):
    return (x-x1)*(y2-y1)/(x2-x1)+y1

print('智能线性插值')
px1 = eval(input('点1第一坐标：'))
px2 = eval(input('点2第一坐标：'))
py1 = eval(input('点1第二坐标：'))
py2 = eval(input('点2第二坐标：'))
x = eval(input('待插值坐标：'))

inx = px1<=x<=px2 or px1>=x>=px2
iny = py1<=x<=py2 or py2>=x>=py2

if not inx and not iny:
    print('错误：给定的待插值不在任何坐标范围内。')
else:
    if inx:
        print('第一坐标插值结果：', interpolation(px1,px2,py1,py2,x))
    if iny:
        print('第二坐标插值结果：', interpolation(py1,py2,px1,px2,x))
