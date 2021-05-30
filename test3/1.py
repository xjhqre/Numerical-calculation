# -*- coding: utf-8 -*-

def Jacobi(mat_a, mat_b, c=0.0001):
    x = []  # 迭代初值 初始化为单行全0矩阵
    for i in range(len(mat_b)):
        x.append(0)
    count = 0  # 迭代次数计数
    print('{:<2d}'.format(count), ['{:.8f}'.format(i) for i in x])
    lc = 1000000  # 存储两次迭代结果之间的误差的集合
    while lc > c:
        x2 = []  # 保存单次迭代后的值的集合
        for i in range(len(x)):
            xi = mat_b[i][0]
            for j in range(len(mat_a[i])):
                if j != i:
                    xi = xi + (-mat_a[i][j]) * x[j]
            xi = xi / mat_a[i][i]
            x2.append(xi)  # 迭代计算得到的下一个xi值
        lc_list = []  # 存储误差值
        for i in range(len(x)):
            lc_list.append(abs(x[i] - x2[i]))
        lc = max(lc_list)  # 取最大误差为误差值
        x = x2
        count = count + 1
        print('{:<2d}'.format(count), ['{:.8f}'.format(i) for i in x2])


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
    Jacobi(mat_a, mat_b, 0.0001)
