#!/usr/bin/env python
#-*- encoding: gbk -*-
import time
def time_now(time_id):
    feedback = None    
    T=int(time.time())
    if time_id==2 or time_id==3:
        T+=86400
    elif time_id==4 or time_id==5:
        T+=172800
    elif time_id==6 or time_id==7:
        T+=259200
    elif time_id==8 or time_id==9:
        T-=86400
    elif time_id==10 or time_id==11:
        T-=172800
    elif time_id==12 or time_id==13:
        T-=259200
    Time=time.strftime("%H:%M", time.localtime())
    Year=int(time.strftime("%Y", time.localtime(T)))
    Month=int(time.strftime("%m", time.localtime(T)))
    Day=int(time.strftime("%d", time.localtime(T)))
    Week=int(time.strftime("%w", time.localtime(T)))
    Date="%d��%d��%d�� "%(Year,Month,Day)
    if Week==0:
        Week='������ '
    elif Week==1:
        Week='����һ '
    elif Week==2:
        Week='���ڶ� '
    elif Week==3:
        Week='������ '
    elif Week==4:
        Week='������ '
    elif Week==5:
        Week='������ '
    elif Week==6:
        Week='������ '
    if time_id==0:
        feedback = '������'+Date
    elif time_id==1:
        feedback = '������'+Week
    elif time_id==2:
        feedback = '������'+Date
    elif time_id==3:
        feedback = '������'+Week
    elif time_id==4:
        feedback = '������'+Date
    elif time_id==5:
        feedback = '������'+Week
    elif time_id==6:
        feedback = '�������'+Date
    elif time_id==7:
        feedback = '�������'+Week
    elif time_id==8:
        feedback = '������'+Date
    elif time_id==9:
        feedback = '������'+Week
    elif time_id==10:
        feedback = 'ǰ����'+Date
    elif time_id==11:
        feedback = 'ǰ����'+Week
    elif time_id==12:
        feedback = '��ǰ����'+Date
    elif time_id==13:
        feedback = '��ǰ����'+Week
    if time_id==14:
        feedback = '����ʱ����'+Time    
    elif time_id==15:
        feedback = '������'+Date+Week
    elif time_id==16:
        feedback = Date+Week+Time
    return feedback
if __name__=='__main__':
    info=raw_input('����Ϊ����Щʲô��')
    if '����' in info:
        if '����' in info:
            time_now(0)
        elif '����' in info:
            time_now(2)
        elif '�����' in info:
            time_now(6)
        elif '����' in info:
            time_now(4)
        elif '����' in info:
            time_now(8)
        elif '��ǰ��' in info:
            time_now(12)
        elif 'ǰ��' in info:
            time_now(10)
    elif '���ڼ�' in info:
        if '����' in info:
            time_now(1)
        elif '����' in info:
            time_now(3)
        elif '�����' in info:
            time_now(7)
        elif '����' in info:
            time_now(5)
        elif '����' in info:
            time_now(9)
        elif '��ǰ��' in info:
            time_now(13)
        elif 'ǰ��' in info:
            time_now(11)
    elif info == 'ʱ��'or info == '����ʱ��':
        time_now(14)
    elif info == '����':
        time_now(15)
    elif 'ʱ��' in info and '����' in info:
        time_now(16)
