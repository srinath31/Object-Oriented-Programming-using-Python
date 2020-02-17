# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:10:46 2019

@author: srinath
"""

class Node:
    def __init__(self,data,nextNode):
        self.data=data
        self.nextNode=None

def printList(l):
    value = []
    while(l):
        value.append(l.data)
        l = l.nextNode
    print(' -> '.join(map(str, value)))


def duplicate(l1):
    p1=l1
    p2=l1
    duplist=[]
    
    while(p1.nextNode!=None):
        if(p1.data not in duplist):
            duplist.append(p1.data)
            p2=p1
            p1=p1.nextNode
        else:
            p2.nextNode=p1.nextNode
            p1=p1.nextNode
    if(p1.nextNode==None):
        if(p1.data not in duplist):
            duplist.append(p1.data)
        else:
            p2.nextNode=None
    return l1
    
    

if __name__=="__main__":
     
    #l1 = Node(1, Node(4, Node(3)))
    l1 = Node(9,None)
    l2= Node(9,None)
    l1.nextNode=l2
    l3= Node(3,None)
    l2.nextNode=l3
    l4= Node(9,None)
    l3.nextNode=l4
    l5= Node(9,None)
    l4.nextNode=l5
    

    
    #print(node1.data,"->",node2.data,"->",node3.data)
    
    
    newlinkedlist=duplicate(l1)
    
    printList(newlinkedlist)

    
    