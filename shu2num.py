#!/usr/bin/env python
#-*- encoding: gbk -*-
feedback = None
def shu2num(string):
    shu=['һ','��','��','��','��','��','��','��','��','ʮ','��','��']
    num=''
    for i in range (0,len(string),2):#�Ż�����ȥ��Ӣ��
        for j in range(0,12):
            if string[i:i+2] == shu[j]:
                num+=shu[j]                
    if len(num)==2:
        for i in range(0,10):
            if num==shu[i]:
                num=i+1
            elif num=='��':
                num=2
            elif num=='��':
                num=0.5
    elif len(num)==4:
        if num[:2]=='ʮ':
            num=str(num)
            for i in range(0,9):
                num=str(num)
                if num[2:]==shu[i]:
                    num=int('1'+str(i+1))
        elif num[2:]=='ʮ':
            for i in range(0,9):
                num=str(num)
                if num[:2]==shu[i]:
                    num=int(str(i+1)+'0')
        else:
            num=10
    elif len(num)==6:
        if num[2:4]=='ʮ':
            for i in range(0,9):
                if num[:2]==shu[i]:
                    num1=str(i+1)
            for i in range(0,9):
                if num[4:]==shu[i]:
                    num2=str(i+1)
            num=int(num1+num2)
        else:
            num=10
    else:
        num=10
    return num
