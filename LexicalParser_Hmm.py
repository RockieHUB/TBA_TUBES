# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:08:49 2019

@author: MRI, Hasbi, Bayu
"""

from Tahap1 import List_Token
from queue import LifoQueue

stackIfThen = LifoQueue()
stackGrouping = LifoQueue()
i = 0
status = "VALID"

while status == "VALID" and i < len(List_Token):
    
    #Belum Mentok
    if not((i+1) > (len(List_Token) - 1)):
    
        if (List_Token[0] == 3 or List_Token[0] == 4 or \
           List_Token[0] == 5 or List_Token[0] == 7 or \
           List_Token[0] == 8 or List_Token[0] == 10):
            status = "INVALID"
        
        else:
            #PQRS
            if (List_Token[i] == 1) and (List_Token[i+1] == 1):
                status = "INVALID"
        
            #NOT
            elif (List_Token[i] == 2 ):
                if List_Token[i+1] == 2 or List_Token[i+1] == 3 or \
                   List_Token[i+1] == 4 or List_Token[i+1] == 5 or \
                   List_Token[i+1] == 6 or List_Token[i+1] == 7 or \
                   List_Token[i+1] == 8 or List_Token[i+1] == 10:
                    status = "INVALID"
            
            #AND,OR,XOR,IFF
            elif List_Token[i] == 3 or List_Token[i] == 4 or \
                 List_Token[i] == 5 or List_Token[i] == 8:
                if List_Token[i+1] == 3 or List_Token[i+1] == 4 or \
                   List_Token[i+1] == 5 or List_Token[i+1] == 6 or \
                   List_Token[i+1] == 7 or List_Token[i+1] == 8 or \
                   List_Token[i+1] == 10:
                    status = "INVALID"
            
            #IF
            elif List_Token[i] == 6:
                if List_Token[i+1] == 3 or List_Token[i+1] == 4 or \
                   List_Token[i+1] == 5 or List_Token[i+1] == 6 or \
                   List_Token[i+1] == 7 or List_Token[i+1] == 8 or \
                   List_Token[i+1] == 10:
                       stackIfThen.put(7)
            
            #THEN
            elif List_Token[i] == 7:
                if List_Token[i+1] == 3 or List_Token[i+1] == 4 or \
                   List_Token[i+1] == 5 or List_Token[i+1] == 6 or \
                   List_Token[i+1] == 7 or List_Token[i+1] == 8 or \
                   List_Token[i+1] == 10:
                       stackIfThen.get()
            
            #GROUPING "(" & ")"
            elif List_Token[i] == 9:
                stackGrouping.put(10)
            elif List_Token[i] == 10:
                stackGrouping.get()

    #Elemen Terakhir     
    else:
    
        #AND,OR,XOR,IFF
        if List_Token[i] == 2 or List_Token[i] == 3 or \
           List_Token[i] == 4 or List_Token[i] == 5 or \
           List_Token[i] == 6 or List_Token[i] == 7:
                status = "INVALID"
        #GROUPING "(" & ")"
        elif List_Token[i] == 9:
            stackGrouping.put(10)
        elif List_Token[i] == 10:
            stackGrouping.get()
    
    if(List_Token[i] == "error"):
        status = "INVALID"

    i += 1
#END OF LOOP

if not(stackGrouping.empty()):
    status = "INVALID"
if not(stackIfThen.empty()):
    status = "INVALID"
    
#HASIL
print(status)
