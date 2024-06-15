'''
Matplotlib 是py中最受欢迎的数据可视化库之一
支持跨平台运行，是2D绘图库，也支持3D绘图接口
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 1.基本绘图
    x = np.linspace(-5, 5, 50)
    y = x ** 2
    plt.plot(x, y, color='pink')  # 如果多次plt.plot最后再show，会显示多个图形在一张表
    plt.show()  # 在标准的Python脚本中，需要显式地调用 plt.show()
    '''
    颜色和样式
    样式：
    '.'：点       ','：像素点     'o'：圆圈      '^'：上三角     'v'：下三角     '<'：左三角     '>'：右三角
	's'：正方形    '+'：加号      'x'：叉号      'D'：菱形      'd'：瘦菱形     '1'：下花三角    '2'：上花三角
    '3'：左花三角    '4'：右花三角    'h'：六边形1    'H'：六边形2    'p'：五边形     '|'：垂直线     '_'：水平线
    '-'：实线      '--'：虚线     '-.'：点划线        ':'：点线
    颜色：
    b：蓝色（blue）      g：绿色（green）     r：红色（red）   c：青色（cyan）
	m：品红（magenta）   y：黄色（yellow）    k：黑色（black） w：白色（white）
    '''
    plt.plot(x, y, color='b', ls='--')  # ls line style线条样式
    plt.plot(x, y*2, 'b-')
    plt.show()  # 每次调plt.show,都会将本行代码前还未显示的所有plot都展示且在同一张图标,即到上一个show()为止的所有plot

    # 画布配置
    plt.figure(figsize=(5,3),dpi=200,facecolor='r')
    '''
    figsize:画布大小，宽高
    dpi:分辨率，像素密度
    facecolor:背景颜色
    
    '''
    # 画正弦曲线
    x1=np.linspace(0,2*np.pi)
    y1=np.sin(x1)
    plt.plot(x1,y1)
    #设置网格
    plt.grid()
    plt.show()


