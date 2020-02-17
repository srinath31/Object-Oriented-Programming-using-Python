# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:56:36 2019

@author: srinath
"""

def rotate_matrix(list1):
    n=len(list1)
    for i in range(0,int(n/2)):
        for j in range(0,n):
            temp=list1[i][j]
            list1[i][j]=list1[n-1-i][j]
            list1[n-1-i][j]=temp
    
    for i in range(0,n):  
       for j in range(0,n):  
           list1[i][j] = list1[j][i]
    
    return list1
if __name__=="__main__":
    l=[[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16]]
    
    result=rotate_matrix(l)
    print(result)