# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:18:39 2019

@author: srinath
"""

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

if __name__=="__main__":
    root=Node(8)
    root.left=Node(2)
    root.right=Node(10)
    root.right.left=Node(9)
    root.right.right=Node(12)
    root.left.left=Node(4)
    root.left.right=Node(6)
    #root.right.right=Node(4)

    
    def printinorder(root):
        
        if(root):
            printinorder(root.left)
            
            print(root.val)
            
            printinorder(root.right)
    
    def printpostorder(root):
        
        if(root):
            printpostorder(root.left)
            
            printpostorder(root.right)
            
            print(root.val)
    
    printpostorder(root)
    printinorder(root)