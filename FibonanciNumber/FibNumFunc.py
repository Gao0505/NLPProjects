#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 13:10
# @Author  : GaoPeipei
# @File    : FibNumFunc.py
# @Software: PyCharm

import time     #计算程序消耗时间
import numpy as np

'''
    @FunctionName: fib_1
    @Purpose     : the Recursive method to calculate fibonacci number
    @Parameter   : num[int]: the index number
    @Return      : the n-th fibonacci number
    @Remark      : 时间复杂度为2^n（用画树的方法分析计算递归问题）
                   空间复杂度为n（每个斐波那契数只会占用一个空间）
'''
def fib_1(num):
    if num<3:
        return 1
    return fib_1(num-1)+fib_1(num-2)

'''
    @FunctionName: fib_2_1
    @Purpose     : the Dynamic Programming method to calculate fibonacci number
    @Parameter   : num[int]: the index number
    @Return      : the n-th fibonacci number
    @Remark      : 维护一个大小为num的数组，减少了重新计算前面的数的时间消耗，动态规划思想
                   时间复杂度为n
                   空间复杂度为n
'''
def fib_2_1(num):
    temp = np.zeros(num)
    temp[0] = 1
    temp[1] = 1
    for i in range(2, num):
        temp[i] = temp[i-1]+temp[i-2]
    return temp[num-1]

'''
    @FunctionName: fib_2_2
    @Purpose     : calculate fibonacci number with the help of two numbers
    @Parameter   : num[int]: the index number
    @Return      : the n-th fibonacci number
    @Remark      : 维护最后一个数之前的两个数，减少了程序的空间消耗
'''
def fib_2_2(num):
    num1, num2 = 1, 1
    tempNum = 0
    for i in range(2, num):
        tempNum = num1+num2
        num1 = num2
        num2 = tempNum
    return tempNum

'''
    @FunctionName: fib_3
    @Purpose     : calculate fibonacci number by formula
    @Parameter   : num[int]: the index number
    @Return      : the n-th fibonacci number
    @Remark      : 转换成矩阵连乘形式简化计算（Matrix Decomposition矩阵分解）推理部分见笔记
'''
def fib_3(num):
    matrix = np.array([[1,1],[1,0]])
    resMatrix = matricsMultiple(matrix, num)    #调用matricsMultiple计算矩阵的n-2次方
    # print(resMatrix)
    res = resMatrix[0][0]+resMatrix[1][0]
    return res

def matricsMultiple(Mtx, pow):
    resMtx = np.identity(2)     #一个二阶单位矩阵
    while pow-2:
        resMtx = np.dot(resMtx, Mtx)
        pow = pow-1
    return resMtx

def main():
    print("Different ways to calculate the 30th fibonacci number :")

    print("----------------------Method 1------------------------")
    start = time.time()
    print("the 30th fibonacci number is: "+str(fib_1(30)))
    end = time.time()
    print("time consumption: %.6f second" % (end-start))
    print("----------------------Method 1 END------------------------")

    print("----------------------Method 2_1------------------------")
    start = time.time()
    print("the 30th fibonacci number is: " + str(fib_2_1(30)))
    end = time.time()
    print("time consumption: %.6f second" % (end - start))
    print("----------------------Method 2_1 END------------------------")

    print("----------------------Method 2_2------------------------")
    start = time.time()
    print("the 30th fibonacci number is: " + str(fib_2_2(30)))
    end = time.time()
    print("time consumption: %.6f second" % (end - start))
    print("----------------------Method 2_2 END------------------------")

    print("----------------------Method 3------------------------")
    start = time.time()
    print("the 30th fibonacci number is: " + str(fib_3(30)))
    end = time.time()
    print("time consumption: %.6f second" % (end - start))
    print("----------------------Method 3 END------------------------")


if __name__ == '__main__':
    main()
