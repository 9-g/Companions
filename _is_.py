#!/usr/bin/env python
#-*- encoding: gbk -*-
def _is_(key):
    feedback=None
    _is_file=open("cache/_is_.txt","r")
    while 1:
        _is_info=_is_file.readline().strip('\n')
        if not _is_info:
            break
        _is=_is_info[:_is_info.index('��')]
        is_=_is_info[_is_info.index('��')+2:]
        if key == _is :
            for i in range(0,len(_is_info)/2,2):
                if _is_info[i:i+2]=='��':
                    _is_info=_is_info[0:i]+'��'+_is_info[i+2:]
                elif _is_info[i:i+2]=='��':
                    _is_info=_is_info[0:i]+'��'+_is_info[i+2:]
            feedback = _is_info
            break
        elif key == is_:
            for i in range(0,len(_is)/2,2):
                if _is[i:i+2]=='��':
                    _is=_is[0:i]+'��'+_is[i+2:]
                elif _is[i:i+2]=='��':
                    _is=_is[0:i]+'��'+_is[i+2:]
            feedback = _is
            break
    _is_file.close
    return feedback
if __name__=='__main__':
    info=raw_input('����Ϊ����Щʲô��')
    if info[:4]=='ɶ��' or info[:6]=='ʲô��' or info[:4]=='˭��':
        info=info[info.index('��')+1:]
        _is_(info)
    elif info[-4:]=='��ɶ' or info[-6:]=='��ʲô' or info[-4:]=='��˭':
        info=info[:info.index('��')]
        _is_(info)
