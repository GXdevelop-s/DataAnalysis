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
    plt.plot(x, y, color='pink')  # 它返回一个Line2D 对象，如果多次plt.plot最后再show，会显示多个图形在一张表
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
    plt.plot(x, y * 2, 'b-')
    plt.show()  # 每次调plt.show,都会将本行代码前还未显示的所有plot都展示且在同一张图标,即到上一个show()为止的所有plot

    # 画布配置
    plt.figure(figsize=(5, 3), dpi=200, facecolor='r')
    '''
    figsize:画布大小，宽高
    dpi:分辨率，像素密度
    facecolor:背景颜色
    
    '''
    # 画正弦曲线
    x1 = np.linspace(0, 2 * np.pi)
    y1 = np.sin(x1)
    plt.plot(x1, y1)
    # 设置网格
    plt.grid()
    plt.show()

    # 2.多图布局
    # 2.1 subplot函数 子图
    fig = plt.figure(figsize=(6, 4))  # 画布对象
    x2 = np.linspace(-np.pi, np.pi, 30)
    y2 = np.sin(x2)
    # 子图1
    ax1 = plt.subplot(221)  # 2行2列中的第一个图    返回一个 Axes 对象，表示这个子图。Axes 对象提供了对子图的全面控制，可以用来绘制数据、设置标签、标题等。
    ax1.plot(x2, y2)
    ax1.set_title('子图1')
    # 子图2
    ax2 = plt.subplot(222)  # 2行2列中的第二个图
    ax2.plot(x2, y2)
    ax2.set_title('子图2')
    # 子图3
    ax3 = plt.subplot(2, 2, 3)  # 2行2列中的第三个图
    ax3.plot(x2, y2)
    ax3.set_title('子图3')
    # 子图4
    ax4 = plt.subplot(2, 2, 4)  # 2行2列中的第四个图
    ax4.plot(x2, y2)
    ax4.set_title('子图4')
    # 使用画布对象自动调整布局
    fig.tight_layout()  # 紧凑布局
    plt.show()
    # 不相同大小子图
    fig = plt.figure(figsize=(8, 5))  # 画布对象
    x3 = np.linspace(-np.pi, np.pi, 30)
    y3 = np.sin(x2)
    # 子图1
    sax1 = plt.subplot(2, 2, 1)
    sax1.plot(x2, y2)
    # 子图2
    sax2 = plt.subplot(2, 2, 2)
    sax2.plot(x2, y2)
    # 子图3
    sax3 = plt.subplot(2, 1, 2)  # 这写的是2行1列中的第二个，也就是说将前两个子图整体视为2行1列中的第一个
    sax3.plot(x2, np.sin(x2 ** 2))
    plt.show()
    # 2.2 使用subplots函数
    fig2, ax_array = plt.subplots(3, 3)  # 返回一个画布对象和含有9个子图对象的2维数组对象（每3个子图一维）
    ax1_array, ax2_array, ax3_array = ax_array  # 接收行
    ax11, ax12, ax13 = ax1_array  # 接受行内子图对象
    ax21, ax22, ax23 = ax2_array
    ax31, ax32, ax33 = ax3_array
    # 使用fig对象设置画布大小
    fig2.set_figheight(8)
    fig2.set_figwidth(8)
    # 此时的画布和画框都有了，只是没有曲线和数据，但也是可以show()的其实
    ax11.plot(x3, np.sin(x3))
    ax12.plot(x3, np.sin(x3))
    ax13.plot(x3, np.sin(x3))
    ax21.plot(x3, np.cos(x3))
    ax22.plot(x3, np.sin(x3))
    ax23.plot(x3, np.sin(x3))
    ax31.plot(x3, np.tan(x3))
    ax32.plot(x3, np.sin(x3))
    ax33.plot(x3, np.sinh(x3))
    plt.tight_layout()  # 紧凑布局

    # 3.图形嵌套 add_subplot函数
    fig3 = plt.figure(figsize=(8, 5))
    # 子图1
    axes1 = fig3.add_subplot(1, 1, 1)
    axes1.plot([0, 1], [1, 3])  # （0，1）点和（1，3）点
    # 子图2：嵌套图
    axes2 = fig3.add_subplot(2, 2, 1, facecolor='pink')  # 会将现在的画布（既是fig3也是axes1的大小）划分成4份，然后放在第一个位置,加背景颜色
    axes2.plot([1, 3])  # 可以直接写1，3

    # 使用axes()函数和add_axes()进行图形嵌套
    fig3 = plt.figure(figsize=(8, 5))
    # 图1
    x4 = np.linspace(0, 2 * np.pi, 30)
    y4 = np.sin(x4)
    plt.plot(x4, y4)
    # 图2：嵌套图 axes()
    axess1 = plt.axes((0.5, 0.35, 0.3, 0.1))  # (left,bottom,width,height)
    axess1.plot(x4, y4, color='g')
    # 图2：嵌套图 add_axes()
    axess2 = fig3.add_axes((0.1, 0.5, 0.3, 0.7))
    axess2.plot(x4, y4, color='r')

    # 双轴显示/组合图
    fig4 = plt.figure(figsize=(8, 5))
    x5 = np.linspace(0, 2 * np.pi, 100)
    # 图1
    current_axis = plt.gca()  # 得到当前轴对象
    current_axis.plot(x5, np.exp(x), c='r')
    current_axis.set_xlabel('time')  # 子图要用set_xlabel,如果不是子图就直接是xlabel
    current_axis.set_ylabel('exp', c='r')
    current_axis.tick_params(axis='y', labelcolor='r')   # 改刻度,改y轴刻度的颜色
    # 图2
    another_axis = current_axis.twinx()  # 创建一个新的 y 轴，与 axes1 共享 x 轴。
    another_axis.plot(x5, np.sin(x5), color='b')
    another_axis.set_ylabel('sin',c='b')
    another_axis.tick_params(axis='y', labelcolor='blue')
    plt.tight_layout()