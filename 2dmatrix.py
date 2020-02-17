# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 06:22:30 2019

@author: srinath
"""

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    
    ###O(m+n)
    def searchMatrix(self, matrix, target):
        if matrix:
            row,col,width=len(matrix)-1,0,len(matrix[0])
            while row>=0 and col<width:
                if matrix[row][col]==target:
                    print(row,col)
                    return True
                elif matrix[row][col]>target:
                    row=row-1
                else:
                    col=col+1
            return False
    
    ###O(m*n)    
    def searchMatrixbrute(self,matrix,target):
        height=len(matrix)
        width=len(matrix[0])
        flag=0
        for i in range(0,height):
            for j in range(0,width):
                if matrix[i][j]==target:
                    flag=1
                    return True
                    break
        if flag==0:
            return False

if __name__=='__main__':
    s=Solution()
    
    matrix=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

    target=5
    
    if (s.searchMatrixbrute(matrix,target)):
        print('Found')
    else:
        print('Not Found')