##################################
#                                #
#  Homework 3                    #
#  Released: September 26, 2017  #
#  Due: October 10, 2017         #
#                                #
##################################


# Matrix Transpose
# 
# Description:
#     Given an m x n target A, return A^T, that is, 
#     return the transpose of the target A.
# 
# Example(s):
# 
#     Example 1:
#         Input:
#             A = [[1]]
#         Output:
#             [[1]]
# 
#     Example 2:
#         Input:
#             A = [[1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9]]
#         Output:
#             [[1, 4, 7],
#              [2, 5, 8],
#              [3, 6, 9]]
#
def matrix_transpose(A): # 计算二维矩阵的转置矩阵, 即对二维矩阵各元素作变换(各元素的行号变列号且列号变行号): a[j][i]=a[i][j]
        
    # 可以将hw3_test.py内"def test_matrix_transpose(self):"的前面2条语句注释掉, 然后单独执行"test_matrix_transpose(self)"方法确认矩阵的行数和列数
    
    # 计算入口参数所给矩阵的行数和列数, #61, https://stackoverflow.com/questions/10713004/find-length-of-2d-array-python
    row = len(A)
    col = len(A[0])
    
    # 显示入口参数矩阵给出的行树和列数, 示例: 对矩阵[[1, 2], [3, 4], [5, 6], [7, 8]]显示"row= 4 , col= 2". 
    #print('row=', row, ',', 'col=', col)
    
    # 不能写成matrix=[row][col]的形式初始化, 将产生"IndexError: list index out of range", Python的二维数组初始化非常变态
    target  = [[0 for j in range(row)] for i in range(col)]
    
    # 显示转置后矩阵的行数和列数, 示例: 对矩阵[[1, 2], [3, 4], [5, 6], [7, 8]]显示"row= 2 col= 4"
    #print('row=', len(target), 'col=', len(target[0]));
    
    for i in range(row):
        for j in range(col):
            target[j][i]= A[i][j]
            
            # 更改为下面的语句将导致"IndexError: list index out of range"
            #target[i][j]= A[j][i]

    return  target

# Max Element in 2-D Array
# 
# Description:
#     Given a 2-d array grid of integers, 
#     determine the maximum number in grid.
# 
# Example(s):
#     Example 1:
#         Input:
#             grid = [[4, 2],
#                     [3, -1]]
#         Output:
#             4
#     
#     Example 2:
#         Input:
#             grid = [[-300, -200],
#                     [-300, -100]]
#         Output:
#             -100
# 
def max_2d_array(grid):
    
    row = len(grid)
    col = len(grid[0])

    max = grid[0][0]    # 假设(只是假设, 可能碰巧它就是最大, 也无所谓)第1个元素数值最大
    
    for i in range(row):
        for j in range(col):
            if(grid[i][j]>max):
                max=grid[i][j]  # 如果某个元素比max大, 则把它作为max
    
    return  max

# Binary Search
# 
# Description:
#     Given a sorted (increasing) array with distinct integers and a
#     target integer, determine the index of target in the given array. 
#     If target is not in the array, return None. Try to use the fact
#     that the array is sorted to optimize your algorithm.
# 
# Example(s):
# 
#     Example 1:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#             target = 3
#         Output:
#             2
# 
#     Example 2:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#             target = 0
#         Output:
#             None
# 
def binary_search(arr, target):
    
    # 可以参考http://www.algolist.net/Algorithms/Binary_search实现机制("Algorithm"部分所述内容)及代码

    left  = 0
    right  = len(arr) -1    # 数组元素最大的索引号

    while (left < right):
    
        # Python计算结果为float, 没有自动转换为int而需要casting, 否则运行错误
        middle = (int)((left + right) / 2) # 中间值的索引号
        
        if(arr[middle] == target):  # 当前元素恰好为待搜索的数值
        
            return middle
        
        elif (target < arr[middle]):
            
            right = middle -1    # 将在middle的左半区间搜索 
            
        else:
            
            left = middle + 1   # 将在middle的右半区间搜索
    
    return  None

# Sorted Matrix Search
# 
# Description:
#     Given a square 2d array of integers and a target integer 
#     return the coordinates of the target integer as a tuple
#     in the form (row, col) if the element exists in the matrix, 
#     or None if the element does not exists. The 2d array 
#     is guaranteed to be sorted ascending row-wise, 
#     and the zeroth element of each row is strictly larger than 
#     the last element of the previous row.
# 
# Example(s):
#     Example 1:
#         Input:
#             arr = [[1 , 2 ,  3],
#                    [8 , 11, 16],
#                    [23, 24, 25]]
#             target = 8
#         Output:
#             (1, 0)
# 
#     Example 2:
#         Input:
#             arr = [[1 , 2 ,  3],
#                    [8 , 11, 16],
#                    [23, 24, 25]]
#             target = 20
#         Output:
#             None
# 
def search_2d_array(arr, target):   # 偷懒儿而没有使用上面二叉搜索方式, 而是穷举搜索, HAHA
    
    row = len(arr)
    col = len(arr[0])
    
    for i in range(row):
        for j in range(col):
            if(arr[i][j] == target):
                return [i, j]
    
    return  None

# Maximum Sum Subarray
# 
# Description:
#     Given an array of integers, determine the maximum sum of
#     a continuous subarray of the given array.
# 
# Examples(s):
#     Example 1:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#         Ouput:
#             15
# 
#     Example 2:
#         Input:
#             arr = [1, -3, 4, 1, -2, 3]
#         Output:
#             6
# 
def max_sum_subarray(arr):  # 不明白什么意思
    
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    
    for i in range(len(a)):
        b  = a[0:i]
        print(i,b)
    
    return  0



# Maximum Sum Sub-Rectangle
# 
# Description:
#     Given a 2-d array of integers, determine the
#     maximum sub-rectangle sum.
# 
# Example(s):
#     Example 1:
#         Input:
#             grid = [[1, 2],
#                     [3, 4]]
#         Output:
#             10
# 
#     Example 2:
#         Input:
#             grid = [[1,  2],
#                     [-3, 0]]
#         Ouput:
#             3
# 
#     Example 3:
#         Input:
#             grid = [[ 1, -2,  0],
#                     [-1,  3,  0],
#                     [ 3, -1, -9]]
#         Output:
#             4
# 
def max_sum_subrectangle(grid): # 不明白什么意思
    pass



# Maximum Number of Times an Array can be Flattened
# 
# Description:
#     Given an array of integers and arrays, 
#     return the maximum number of times arr can be flattened. 
#     For example, if arr = [1, 2, [3, 4], 5], 
#     then arr could be flattened once.
# 
# Example(s):
#     Example 1:
#         Input:
#             arr = [1, 2, [3, 4], 5]
#         Output:
#             1
# 
#     Example 2:
#         Input:
#             arr = [1, 2, 3, 4, 5]
#         Output:
#             0
# 
def max_array_flatten(arr): # 不明白什么意思
    pass

def main():

    print('enter')
    A=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    matrix_transpose(A)
    print('leave')

if __name__ == "__main__": main()
