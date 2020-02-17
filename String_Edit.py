# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 11:13:36 2019

@author: srinath
"""
def insert(s1:str,s2:str,length:int):
    edits=0

    for i in range(0,length):
        if (s2[i] in s1):
            continue
        else:
            edits=edits+1
    
        
    return edits

def replace(s1:str,s2:str,length:int):
    edits=0
    for i in range(0,length):
        if(s1[i]==s2[i]):
            continue
        else:
            edits=edits+1
    return edits

if __name__=="__main__":
    s1="pales"
    s2="pale"
    
    
    l1=len(s1)
    l2=len(s2)
    
    if s1==s2:
        e=0
    elif(l1==l2+1):
        e=insert(s2,s1,l1)
    elif l2==l1+1:
        e=insert(s1,s2,l2)
    elif l1==l2:
        e=replace(s1,s2,l1)
    else:
        e=2
    
    if(e==0):
        print("0 edits required")
    elif(e==1):
        print("1 edit required")
    else:
        print("String cannot be edited")