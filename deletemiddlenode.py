# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:49:56 2019

@author: srinath
"""

class Node:
    def __init__(self,data,nextNode=None):
        self.data=data
        self.nextNode=nextNode

def printList(l):
    value = []
    while(l):
        value.append(l.data)
        l = l.nextNode
    print(' -> '.join(map(str, value)))

def getsize(l1):
    s=1
    p1=l1
    while(p1.nextNode!=None):
        s=s+1
        p1=p1.nextNode
    return s

def deleteNode(l1,node,head):
    p1=l1
    p2=l1
   
    
    if p1.data==node:
        print("Cannot delete since it is the first node")
    else:
        while(p1.nextNode!=None):
            if(p1.data!=node):
                p2=p1
                p1=p1.nextNode
            else:
                p2.nextNode=p1.nextNode
                p1.nextNode=None
    
        if p1==None:
            print("Cannot delete since it is the last node")
                
    return l1   

if __name__=="__main__":
     
    l1 = Node(9, Node(8, Node(9)))
    
    size=getsize(l1)
    head=l1.data
    inputnode=l1.nextNode.nextNode.data
    print(inputnode)
    
    newlist=deleteNode(l1,inputnode,head)
    printList(newlist)
