#!/usr/bin/env python
#-*- encoding: gbk -*-
import string,random

def blur(key,question):
    feedback = None
    re_good=['лл�佱��','�ţ���ʵ��Ҳû��ô������������','������ˣ��˼Ҷ�������˼��*^_^*']
    re_bad=['������˵�һ�����','���������������ˣ�','(�i�n�i)�ء���']
    ni_keyi=['�����ԣ����Բ��У�','�Ҳ�ͬ�⣡']
    ni_neng=['��ô���ܣ���','�ң����ڿ���Ц�ɣ�','�Ҳ���ô���á���']
    ni_hui=['^_^|||���ᡭ��','�ҵ����밡����','��̽����£�']
    ni_xihuan=['һ�㶼��ϲ������','�����һ��Ǻ�ϲ���ģ�','����ô���ܲ�ϲ����']
    ni_ai=['�۾���������','�ܰ����ܰ���','��������']
    ni_hen=['һ��Ҳ����']
    ni_shi=['��Ȼ���ǣ�','����ô�����ǡ���','�����������']
    ni_you=['�Բ��𡭡�û�С���','��Ҳ�������㣡','������һ������������']
    ni_xiang=['��Ȼ���ˣ�','���ζ������أ�','']
    ni_unknown=['��°���','���Ǹ����ܣ�','����ôʲô���ʰ���','����治֪��','��֪����̫���ˣ�','�⻹������','�㲻�����˽��˼������ڣ���ô�᲻֪����']
    if key[:2]=='��':
        good_time=bad_time=0
        good_file=open("data/db/good.txt","r")
        over=False
        while not over:
            good_info=good_file.readline().strip('\n')
            if good_info=='':
                over=True
            elif good_info in key:
                good_time_file=open("data/db/good_time.txt","r")
                good_time=int(good_time_file.readline().strip('\n'))
                feedback=re_good[good_time%len(re_good)]
                good_time+=1
                good_time_file.close
                good_time_file=open("data/db/good_time.txt","w")
                good_time_file.write('%d'%good_time)
                good_time_file.close
                over=True
        good_file.close
        if not feedback:
            bad_file=open("data/db/bad.txt","r")
            over=False
            while not over:
                bad_info=bad_file.readline().strip('\n')
                if bad_info=='':
                    over=True
                elif bad_info in key:
                    bad_time_file=open("data/db/bad_time.txt","r")
                    bad_time=int(bad_time_file.readline().strip('\n'))
                    feedback=re_bad[bad_time%len(re_bad)]
                    bad_time+=1
                    bad_time_file.close
                    bad_time_file=open("data/db/bad_time.txt","w")
                    bad_time_file.write('%d'%bad_time)
                    bad_time_file.close
                    over=True
            bad_file.close
        if not feedback:
            if key[-2:]=='��' or key[-2:]=='ô' or question==True:
                if key[-4:]=='����' or key[-4:]=='��ô' :
                    if key[-6:]=='������' or key[-6:]=='����ô' :
                        feedback ='�����ǣ���Ȼ��'
                    else:
                        feedback ='�ǿ�δ�أ�'
                else:
                    if '����' in key:
                        feedback = random.choice(ni_keyi)
                    elif '��' in key:
                        feedback = random.choice(ni_neng)
                    elif '��' in key:
                        feedback = random.choice(ni_hui)
                    elif 'ϲ��' in key:
                        feedback = random.choice(ni_xihuan)
                    elif '��' in key:
                        feedback = random.choice(ni_ai)
                    elif '��' in key:
                        feedback = random.choice(ni_hen)
                    elif '��' in key:
                        feedback = random.choice(ni_shi)
                    elif '��' in key:
                        feedback = random.choice(ni_you)
                    elif '��' in key:
                        feedback = random.choice(ni_xiang)
                    else:
                        feedback = random.choice(ni_unknown)
    elif key[:2]=='��':
        wo_keyi=['û�ţ�','���ΰ��㣡','�붼���룡']
        wo_neng=['������ر�����ô���Ļ�����','','']
        wo_shi=['ŷ�ͱ���ô˵�Լ���','��ֻ��˵�����������Ĳ�һ������']
        wo_you=['����û������ô֪������','','']
        wo_unknown=['']
        if key[-2:]=='��' or key[-2:]=='ô' or question==True:
            if key[-4:]=='����' or key[-4:]=='��ô' :
                if key[-6:]=='������' or key[-6:]=='����ô' :
                    feedback ='�����ǣ���Ȼ��'
                else:
                    feedback ='�ǿ�δ�أ�'
            else:
                if '����' in key:
                    feedback = random.choice(wo_keyi)
                elif '��' in key:
                    feedback = random.choice(wo_neng)
                elif '��' in key:
                    feedback = random.choice(wo_shi)
                elif '��' in key:
                    feedback = random.choice(wo_you)
                else:
                    feedback = random.choice(wo_unknown)
        if '���Բ�����' in key:
            feedback = random.choice(wo_keyi)
        elif '�ܲ���' in key:
            feedback = random.choice(wo_neng)
        elif '�ǲ���' in key:
            feedback = random.choice(wo_shi)
        elif '��û��' in key:
            feedback = random.choice(wo_you)
    if '���Բ�����' in key:
        feedback = random.choice(ni_keyi)
    elif '�ܲ���' in key:
        feedback = random.choice(ni_neng)
    elif '�᲻��' in key:
        feedback = random.choice(ni_hui)
    elif 'ϲ����ϲ��' in key:
        feedback = random.choice(ni_xihuan)
    elif '������' in key:
        feedback = random.choice(ni_ai)
    elif '�޲���' in key:
        feedback = random.choice(ni_hen)
    elif '�ǲ���' in key:
        feedback = random.choice(ni_shi)
    elif '��û��' in key:
        feedback = random.choice(ni_you)
    elif '�벻��' in key:
        feedback = random.choice(ni_xiang)
    return feedback
if __name__=='__main__':
    info=raw_input('����Ϊ����Щʲô��')
    print blur(info)
