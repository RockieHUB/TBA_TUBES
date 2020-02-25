# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:48:25 2019

@author: MRI, Hasbi, Bayu
"""

List_Token = []
str = input("Masukkan Test Case : ")
print() 
x = str.replace(" ", "").lower()

token = 0
state = 0
i = 0

#START OF LOOP
while i < len(x):
    
    if state == 99:
        state = 0
        
#START STATE 0
    if state == 0:
        
#OPERAND p,q,r, dan s
        if(x[i] == "p" or x[i] == "q" or x[i] == "r" or x[i] == "s"):
            token = 1
            List_Token.append(token)
            state = 99

#OPERATOR if dan iff
        elif(x[i] == "i"):
            state = 11

#OPERATOR then
        elif(x[i] == "t"):
            state = 8
                                   
#GROUPING ) & (
        elif(x[i] == "("):
            token = 9
            List_Token.append(token)
            state = 99
        elif(x[i] == ")"):
            token = 10
            List_Token.append(token)
            state = 99

#OTHER OPERATORS FROM STATE 0
        elif(x[i] == "a"):
            state = 1
        elif(x[i] == "n"):
            state = 3
        elif(x[i] == "o"):
            state = 5
        elif(x[i] == "x"):
            state = 6
        else:
            state = 99
            token = "error"
            List_Token.append(token)

#START STATE 1
    elif state == 1:

#OPERATOR AND
        if(x[i] == "n"):
            state = 2
        else:
            state = 99
            token = "error"
            List_Token.append(token)

#START STATE 2
    elif state == 2:
        
#OPERATOR AND
        if(x[i] == "d"):
            state = 99
            token = 3
        else:
            state = 99
            token = "error"
        List_Token.append(token)
        
#START STATE 3
    elif state == 3:
        
#OPERATOR NOT
        if(x[i] == "o"):
            state = 4
        else:
            state = 99
            token = "error"
            List_Token.append(token)
            
#START STATE 4
    elif state == 4:
        
#OPERATOR NOT
        if(x[i] == "t"):
            state = 99
            token = 2
        else:
            state = 99
            token = "error"
        List_Token.append(token)
        
#START STATE 5

    elif state == 5:

#OPERATOR OR        
        if(x[i] == "r"):
            state = 99
            token = 4
        else:
            state = 99
            token = "error"
        List_Token.append(token)
            
#START STATE 6
    elif state == 6:

#OPERATOR XOR        
        if(x[i] == "o"):
            state = 7
        else:
            state = 99
            token = "error"
            List_Token.append(token)

#START STATE 7
    elif state == 7:
        
#OPERATOR XOR
        if(x[i] == "r"):
            state = 99
            token = 5
        else:
            state = 99
            token = "error"
        List_Token.append(token)
        
#START STATE 8
            
    elif state == 8:

#OPERATOR THEN
        if(x[i] == "h"):
            state = 9
        else:
            state = 99
            token = "error"
            List_Token.append(token)            
        
#START STATE 9

    elif state == 9:
        
#OPERATOR THEN
        if(x[i] == "e"):
            state = 10
        else:
            state = 99
            token = "error"
            List_Token.append(token)
        
#START STATE 10
            
    elif state == 10:
        
#OPERATOR THEN
        if(x[i] == "n"):
            state = 99
            token = 7
        else:
            state = 99
            token = "error"
        List_Token.append(token)
        
#START STATE 11

    elif state == 11:

#OPERATOR IF & IFF
        if(x[i] == "f") and not((i+1) > (len(x) - 1)):
            state = 12
        elif(x[i] == "f") and ((i+1) > (len(x) - 1)):
            state = 12
            token = 6
            List_Token.append(token)
        else:
            state = 99
            token = "error"
            List_Token.append(token)
        
#START STATE 12
        
    elif state == 12:
        
        if (x[i] == "f") and not((i+1) > (len(x) - 1)):
            if(x[i+1] == "p" or x[i+1] == "q" or x[i+1] == "r" or x[i+1] == "s" or \
               x[i+1] == "(" or x[i+1] == ")" or x[i+1] == "i" or x[i+1] == "t" or \
               x[i+1] == "a" or x[i+1] == "n" or x[i+1] == "o" or x[i+1] == "x"):
                token = 8
                state = 99
            else:
                token = "error"
                state = 99
        elif (x[i] == "f") and ((i+1) > (len(x) - 1)):
            token = 8
            state = 99
        elif (x[i] == "p" or x[i] == "q" or x[i] == "r" or x[i] == "s" or \
              x[i] == "(" or x[i] == ")" or x[i] == "i" or x[i] == "t" or \
              x[i] == "a" or x[i] == "n" or x[i] == "o" or x[i] == "x"):
            i -= 1
            token = 6
            state = 99
        else:
            state = 99
            token = "error"
        List_Token.append(token)
              
#END OF ALL STATE
    if(token == "error"):
        break
    i += 1
#END OF LOOP

print(List_Token)