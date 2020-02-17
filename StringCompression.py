# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:13:34 2019

@author: srinath
"""

def stringcompress(s:str,length:int):
    count=0
    str1=""
    for i in range(0,length):
        count=count+1
        if(i+1>=length or s[i]!=s[i+1]):
            str1=str1+s[i]+str(count)
            count=0
        
    
        
    return str1
        

if __name__=="__main__":
    s="abb"
    l=len(s)
    newstr=stringcompress(s,l)
    print(newstr)
            