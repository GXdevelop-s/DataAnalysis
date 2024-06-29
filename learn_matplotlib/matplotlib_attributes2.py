import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 1.图例
    plt.figure(figsize=(6, 4))
    x = np.linspace(0, 2 * np.pi, 100)
    plt.plot(x, np.sin(x), label='sin')
    plt.plot(x, np.cos(x), label='cos')  # 此时两个label都是不会显示的
    plt.legend(
        fontsize=12,
        loc='center',
        # loc图例位置 还有 'best''upper right/left''lower right/left''right''center left/right''lower center''upper center'
        ncol=2,  # 图例显示成几列
        # 图例的具体位置（x,y,width,height）,4个参数的单位就是坐标的单位
        bbox_to_anchor=(0, 0, 1, 1)
    )  # 此时才会显示sin和cos这两个图例，或者plot的时候不写，在legend的参数中传个列表['sin','cos']也可以，还有fontsize、
    plt.show()  # 图例会默认自己寻找合适的位置

    # 2.线条属性
    '''
    color:颜色
    linestyle：样式
    linewidth：宽度
    alpha：透明度 在0~1之间
    marker：标记
    mfc：marker face color 标记的背景颜色，比如圆点的内部的那个颜色，感觉有点鸡肋
    '''
    plt.figure(figsize=(6, 4))
    x = np.linspace(0, 2 * np.pi, 20)  # tip:当给的点不够多的时候，会有折痕
    y1 = np.sin(x)
    y2 = np.cos(x)
    plt.plot(x, y1, color=['b'], linestyle=':', marker='o', mfc='y', markersize=10)
    plt.plot(
        x, y1 + y2, color=['o'], linestyle='-', marker='>', label='sin+cos',
        mfc='b',
        markersize=10,  # 标记大小
        markeredgecolor='green',  # 标记（点）的边缘颜色
        markeredgewidth=2,  # 标记（点）边缘的宽度
        alpha=0.5,
    )
    plt.show()

    # 3.坐标轴
    # 坐标轴刻度 xticks yticks
    plt.figure(figsize=(6, 4))
    x = np.linspace(0, 10)
    y = np.sin(x)
    plt.plot(x, y)  # 此时的x轴和y轴的刻度是默认的
    plt.xticks(np.arange(0, 10, 1), fontsize=20)  # x轴最小是0，最大是10，步长为1
    plt.yticks(
        [-1, 0, 1],  # 刻度值，刻度大小，画图是根据这个画的
        labels=['min', 0, 'max'],  # 显示刻度标签，也就是说根据ticks画图，但是显示出来是labels的内容
        ha='right'  # 刻度和轴的水平对齐方式
    )
    # 坐标轴范围
    plt.figure(figsize=(6, 4))
    x = np.linspace(0, 2 * np.pi)
    y = np.sin(x)
    plt.plot(x, y, c='r')  # 当前情况下坐标轴的范围是（0，2pi），但是可以控制
    plt.xlim(-2, 8)  # 设置x坐标轴的范围为-2到8
    plt.ylim(-2, 2)  # 设置y坐标轴的范围为-2到2
    # 设置坐标轴开关和范围
    plt.axis([1, -3, 4, 2])  # 设置坐标轴范围[xmin,xmax,ymin,ymax]
    plt.axis('on')  # 'off':不显示坐标轴 'equal':让x轴和y轴刻度距离相同  'scaled':自动缩放坐标轴和图片匹配 'tight':紧凑自动适配图片 'square':画布成正方形
    # 标题
    plt.figure(figsize=(6, 4))
    x = np.linspace(0, 10)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('sin曲线', fontsize=20, loc='center')  # 图的标题的属性 比如标题内容，标题字号，标题位置等等
    plt.suptitle('这是sin曲线的父标题', y=1.1, fonsize=22)  # 图的标题的父标题,y=1的时候父标题差不多就在标题上面一点点
    # 网格线
    plt.grid(ls='--', lw=0.5, c='r', axis='x')  # ls网格线条的样式 lw网格线条的宽度,axis只显示哪个轴对应的网格线条
    # 坐标轴的标签
    plt.xlabel('x', fontsize=10, rotation=0,
               horizontalalignment='right')  # rotation是旋转的角度，0度是水平,horizontalalignment是对齐方式，right是靠右对齐
    plt.ylabel('y')
