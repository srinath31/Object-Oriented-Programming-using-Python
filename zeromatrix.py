# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:28:16 2019

@author: srinath
"""

def zero_matrix(list1):
    n=len(list1)
    rows=[]#Stores row number
    cols=[]#Stores column number
    for i in range(0,n):  
       for j in range(0,n):
           if list1[i][j]==0:
               rows.append(i)
               cols.append(j)
    print(rows,cols)
    l=len(rows)
    
    for i in range(0,n):
        for j in range(0,n):
            if i in rows:
                list1[i][j]=0
            if j in cols:
                list1[i][j]=0
    print(list1)
    
    #return list1
if __name__=="__main__":
    l=[[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,0,0,16]]
    
    zero_matrix(l)
    #print(result)