# coding: utf8
import numpy as np


# 设置矩阵
def getInput():
 a = np.mat([[1.1348, 3.8326, 1.1651, 3.4017, 9.5342],
             [0.5301, 1.7875, 2.5330, 1.5435, 6.3941],
             [3.4129, 4.9317, 8.7643, 1.3142, 18.4231],
             [1.2371, 4.9998, 10.6721, 0.0147, 16.9237]],dtype = float)
 a = a.round(8)
 return a


# 计算三角矩阵
def triangularMatrix(mat_a):
 for i in range(0, (mat_a.shape[0])-1):
  if mat_a[i, i] == 0:
   print("终断运算：")
   print(mat_a)
   break
  else:
   for j in range(i+1, mat_a.shape[0]):
    mat_a[j, :] = mat_a[j,:] - (mat_a[j,i]/mat_a[i,i])*mat_a[i, :]
 return mat_a


# 计算方程解
def revert(new_mat):
 #创建矩阵存放答案 初始化为0
 x = np.mat(np.zeros(new_mat.shape[0], dtype=float))
 number = x.shape[1]-1
 # print(number)
 x[0,number] = new_mat[number,number+1]/new_mat[number, number]
 for i in range(number-1,-1,-1):
  try:
   x[0,i] = (new_mat[i,number+1]-np.sum(np.multiply(new_mat[i,i+1:number+1],x[0,i+1:number+1])))/(new_mat[i,i])
  except:print("错误")
 print(x)
if __name__ == "__main__":
 mat_a = getInput()
 print("原矩阵")
 print(mat_a)
 new_mat = triangularMatrix(mat_a).round(8)
 print("三角矩阵")
 print(new_mat)
 print("方程的解")
 revert(new_mat)