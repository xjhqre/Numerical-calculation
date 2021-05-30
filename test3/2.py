# -*- coding: utf-8 -*-

def Gauss(mat_a, mat_b, c=0.0001):
    x = []  # 迭代初值 初始化为单行全0矩阵
    for i in range(len(mat_b)):
        x.append(0)
    count = 0  # 迭代次数计数
    print('{:<2d}'.format(count), ['{:.8f}'.format(i) for i in x])
    lc = 1000000  # 初始化误差为1000000
    while lc > c:
        x2 = list(x)  # 保存上一次x的值
        for i in range(len(x)):
            xi = mat_b[i][0]
            for j in range(len(mat_a[i])):
                if j != i:
                    xi = xi + (-mat_a[i][j]) * x[j]
            xi = xi / mat_a[i][i]
            x[i] = xi;  #高斯-赛德尔迭代法
        lc_list = []  # 存储误差值
        for i in range(len(x)):
            lc_list.append(abs(x[i] - x2[i]))
        lc = max(lc_list)  # 取最大误差为误差值
        count = count + 1
        print('{:<2d}'.format(count), ['{:.8f}'.format(i) for i in x])


if __name__ == "__main__":
    mat_a = [[4, -1, 0, -1, 0, 0],
             [-1, 4, -1, 0, -1, 0],
             [0, -1, 4, -1, 0, -1],
             [-1, 0, -1, 4, -1, 0],
             [0, -1, 0, -1, 4, -1],
             [0, 0, -1, 0, -1, 4]]
    mat_b = [[0], [5], [-2], [5], [-2], [6]]
    xx = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    print('k   ', '{: <13s}'.format('x1'), '{: <13s}'.format('x2'), '{: <13s}'.format('x3'),
          '{: <13s}'.format('x4'), '{: <13s}'.format('x5'), '{: <13s}'.format('x6'))
    Gauss(mat_a, mat_b, 0.0001)
