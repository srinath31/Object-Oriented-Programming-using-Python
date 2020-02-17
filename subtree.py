# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:46:23 2019

@author: srinath
"""

class Solution:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.val=value
   
    #O(m*n) where m and n are the number of nodes of respective trees
    def isSubtree(self,s,t):
        if (s == None):
            return False
        if (self.isSame(s, t)): 
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSame(self,s,t):
        if (s == None and t == None):
            return True
        if (s == None or t == None):
            return False
        
        if (s.val != t.val): 
            return False
        
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
 
    
    
if __name__=="__main__":
    
    obj=Solution(None)
    
    s=Solution(3)
    s.left=Solution(4)
    s.right=Solution(5)
    s.left.left=Solution(1)
    s.left.right=Solution(2)
    #s.left.right.left=Solution(0)
    
    t=Solution(4)
    t.left=Solution(1)
    t.right=Solution(2)
    
    result=obj.isSubtree(s,t)
    
    if result==True:
        print("same")
    else:
        print("Not same")
    
    #O(n) where n is the number of nodes
    def inorder(root,string):
        if(root):
            string=string+str(root.val)
            inorder(root.left,string)
            inorder(root.right,string)
        return string
    
    def preorder(root,string):
        if(root):
            preorder(root.left,string)
            string=string+ str(root.val)
            preorder(root.right,string)
        return string
    
    str1=str2=str3=str4=""
    tree1inorder=inorder(s,str1)
    tree1preorder=preorder(s,str2)
    tree2inorder=inorder(t,str3)
    tree2preorder=preorder(t,str4)
    
    print(tree1inorder)
    
    