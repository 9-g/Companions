#!/usr/bin/env python
#-*- encoding: gbk -*-
import string
from shu2num import *
def translator(frm='',to='',delete='',keep=None):
    if len(to)==1:
        to=to*len(frm)
    trans=string.maketrans(frm,to)
    if keep is not None:
        allchars=string.maketrans('','')
        delete=allchars.translate(allchars,keep.translate(allchars,delete))
    def translate(s):
        return s.translate(trans,delete)
    return translate
digits_only=translator(keep=string.digits)
def count_down(time):
    hour=minute=second=0
    if 'Сʱ'in time:
        h=time[:time.index('Сʱ')]
        time=time[time.index('Сʱ')+4:]
        hour=digits_only(h)
        if hour == '':
            hour=shu2num(h)
            if hour==0.5:
                minute=30
        else:
            hour=int(hour)
    if '��'in time:
        m=time[:time.index('��')]
        time=time[time.index('��')+2:]
        minute=digits_only(m)
        if minute == '':
            minute=shu2num(m)
            if minute==0.5:
                second=30
        else:
            minute=int(minute)
    if '��'in time:
        s=time[:time.index('��')]
        second=digits_only(s)
        if second == '':
            second=shu2num(s)
            if second==0.5:
                second=1
        else:
            second=int(second)
    return (hour,minute,second)
