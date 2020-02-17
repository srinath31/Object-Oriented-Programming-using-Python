# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:07:35 2019

@author: srinath
"""
import math
class TreeNode:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def create_tree(array):
    if (array==[]):
        return None
    mid = math.floor((len(array))/2)
    node = TreeNode(array[mid])
    node.left = create_tree(array[0:mid])
    node.right = create_tree(array[mid+1:])
    return node


if __name__=="__main__":      
    
    a=[1,2,3,4]
    b=create_tree(a)
    print(b.right.val)