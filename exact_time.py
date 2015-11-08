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
def exact_time(when):
    if ':' in when:
        _when=digits_only(when[:when.index(':')])
        when_=digits_only(when[when.index(':')+1:])
        if int(when_)>=60:
            _when=int(_when)+int(when_)/60
            when_=int(when_)%60
        if int(_when)>=24:
            exact_when='00:00'
        else:
            exact_when=str(_when)+':'+str(when_)
    elif '��' in when:
        _when=digits_only(when[:when.index('��')])
        when_=digits_only(when[when.index('��')+1:])
        exact_when=_when+':'+when_
    elif '���' in when:
        if not digits_only(when[:when.index('���')]):
            _when=str(shu2num(when[:when.index('���')]))
        else:
            _when=digits_only(when[:when.index('���')])
        exact_when=_when+':30'
    elif '��һ��' in when:
        if not digits_only(when[:when.index('��һ��')]):
            _when=str(shu2num(when[:when.index('��һ��')]))
        else:
            _when=digits_only(when[:when.index('��һ��')])
        exact_when=_when+':15'
    elif '������' in when:
        if not digits_only(when[:when.index('������')]):
            _when=str(shu2num(when[:when.index('������')]))
        else:
            _when=digits_only(when[:when.index('������')])
        exact_when=_when+':45'
    elif '��' in when:
        if not digits_only(when[:when.index('��')]):
            _when=str(shu2num(when[:when.index('��')]))
        else:
            _when=digits_only(when[:when.index('��')])
        if not when[when.index('��')+2:]:
            when_='00'
        else:
            if not digits_only(when[when.index('��')+2:]):
                when_=str(shu2num(when[when.index('��')+2:]))
            else:
                when_=digits_only(when[when.index('��')+2:])
        if int(when_)>=60:
            _when=int(_when)+int(when_)/60
            when_=int(when_)%60
        if int(_when)>=24:
            exact_when='00:00'
        else:
            exact_when=str(_when)+':'+str(when_)
    else:
        exact_when='00:00'
    return exact_when
