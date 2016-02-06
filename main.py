#!/usr/bin/env python
#-*- encoding: gbk -*-
import os,random,webbrowser,string,time,re,sched,thread
from shell import shell
from shell import shellcon
from calc import *
from the_time import *
from weather import *
from movie import *
from zhidao import *
from wiki import *
from _is_ import _is_
from reminder import *
from count_down import *
from exact_time import *
from blur import *
from xiaohua import *
from neihan import *
from iciba import *

en_punctuation=['+','-','*','/','^','!','"','#','$','%','&','\'','(',')',',','.',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']
cn_punctuation=['��','��','��','��','&','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��']
operator=['+','-','*','/','^','!','��','��','��','��','�η�','ƽ��','����','����','�׳�','����','������','������','������','������','������','�����','sin','cos','tan','cot','sec','csc','ln']
number=['0','1','2','3','4','5','6','7','8','9']
Q=['��','��','ô','ɶ','��','˭','զ','���','����','զ��','Ϊ��','��û��','ϲ����ϲ��','�в���','�ǲ���','�ܲ���','�᲻��','�ò���','','','']
schedule = sched.scheduler(time.time, time.sleep)
windows_path = shell.SHGetPathFromIDList(shell.SHGetSpecialFolderLocation(0,shellcon.CSIDL_WINDOWS))
programfiles_path = shell.SHGetPathFromIDList(shell.SHGetSpecialFolderLocation(0,shellcon.CSIDL_PROGRAM_FILES))
def baidu(key):
    feedback=None
    url="http://www.baidu.com/baidu?word="+key
    webbrowser.open_new_tab(url)
    feedback='����Ϊ������"'+key+'"'
    return feedback
def main(info):  
    feedback = None
    special_format=False
###########################################################################################
#calc
###########################################################################################
    op=False
    nu=False
    current_theme_file=open("data/settings/current_theme.txt","r")
    current_theme=current_theme_file.readline()
    current_theme_file.close()
    for i in range(0,len(operator)):
        if operator[i] in info:
            op=True
    for i in range(0,len(number)):
        if number[i] in info:
            nu=True
    if op==True and nu==True:
        feedback = calc(info)
###########################################################################################
#ȥ����
###########################################################################################
    q=False
    if info[-2:]=='��'or info[-1:]=='?':
        q=True
    origin_info=info
    info=info.decode("gbk").encode("utf8") 
    for i in range(0,len(en_punctuation)):
        while en_punctuation[i].decode("gbk").encode("utf8") in info:
            info=info[:info.index(en_punctuation[i].decode("gbk").encode("utf8"))]+info[info.index(en_punctuation[i].decode("gbk").encode("utf8"))+1:]
    for i in range(0,len(cn_punctuation)):
        while cn_punctuation[i].decode("gbk").encode("utf8") in info:
            info=info[:info.index(cn_punctuation[i].decode("gbk").encode("utf8"))]+info[info.index(cn_punctuation[i].decode("gbk").encode("utf8"))+3:]
    info=info.decode("utf8").encode("gbk")

###########################################################################################
#cancel
###########################################################################################
    if 'ȡ��' in info:
        if '�ػ�' in info or '�رռ����'in info or '�رյ���'in info:        
            subprocess.Popen('shutdown -a', shell=True)
            feedback ='���Ĺػ��ƻ���ȡ��(���ùػ��ƻ�ʱ���Զ�ȡ��֮ǰ�Ĺػ��ƻ�)'
        elif '����' in info or '��������' in info:        
            subprocess.Popen('shutdown -a', shell=True)
            feedback ='���������ƻ���ȡ��(���������ƻ�ʱ���Զ�ȡ��֮ǰ�������ƻ�)'
        elif 'ע��' in info:        
            subprocess.Popen('shutdown -a', shell=True)
            feedback ='����ע���ƻ���ȡ��'
        elif '����' in info:
            cancel()
            feedback ='�ѽ�������������ȡ��'

###########################################################################################
#search
########################################################################################### 
    if '����' in info:
        info=info[info.index('����')+4:]
        feedback=baidu(info)
    elif '��һ��' in info:
        info=info[info.index('��һ��')+6:]
        feedback=baidu(info)
    elif '�ٶ�һ��' in info:
        info=info[info.index('�ٶ�һ��')+8:]
        feedback=baidu(info)
    elif 'baiduһ��' in info:
        info=info[info.index('baiduһ��')+9:]
        feedback=baidu(info)
###########################################################################################
#weather
###########################################################################################
    if '����'in info or '������'in info or '��������'in info or '������'in info or '�²�����'in info or 'ʲô��'in info or '������'in info or '��ѩ��'in info or '�²���ѩ'in info or '�¶�'in info or '���ٶ�'in info or '����'in info or '����'in info:
        city=False
        city_file=open("data/db/city1.txt","r")
        for i in range (0,2586):
            city_info=city_file.readline()
            city_name=city_info[10:].strip(" \n")
            if city_name in info:
                city=True
                break
        if city:
            feedback = city_weather(city_name)
        else:
            feedback = local_weather()
        if feedback:
            special_format = True
###########################################################################################
#xiaohua
###########################################################################################
    if "����Ц��" in info or "�ں�����" in info:
        feedback=xiaohua()
        style_path_file=open("data/settings/style_path.txt","r")
        style_path=style_path_file.read()
        style_path_file.close()
        href_file=open(style_path+"href.txt","r")
        href=href_file.read()
        href_file.close()
        feedback = '<p style="font-family:Microsoft Yahei;font:24px">'+feedback+'��do������ǿ����Ц��˵��<br><a style="text-decoration:none;color:#'+href+'" href="#">����һ��</a></p>'
        special_format=True
    if "�ں�ͼ" in info or "��Цͼ" in info:
        feedback=neihan()
        style_path_file=open("data/settings/style_path.txt","r")
        style_path=style_path_file.read()
        style_path_file.close()
        href_file=open(style_path+"href.txt","r")
        href=href_file.read()
        href_file.close()
        feedback = feedback+'<a style="font-family:Microsoft Yahei;font:24px;text-decoration:none;color:#'+href+'" href="#">����һ��</a>'
        special_format=True
    if "���ҿ���һ��" in info or "���Ҹ���һ��" in info:
        style_path_file=open("data/settings/style_path.txt","r")
        style_path=style_path_file.read()
        style_path_file.close()
        href_file=open(style_path+"href.txt","r")
        href=href_file.read()
        href_file.close()
        if random.randint(0,1)==0:
            feedback=xiaohua()
            feedback = '<p style="font-family:Microsoft Yahei;font:24px">'+feedback+'��do������ǿ����Ц��˵��<br><a style="text-decoration:none;color:#'+href+'" href="#">����һ��</a></p>'
        else:
            feedback=neihan()
            feedback = feedback+'<a style="font-family:Microsoft Yahei;font:24px;text-decoration:none;color:#'+href+'" href="#">����һ��</a>'
        special_format=True
###########################################################################################
#run
###########################################################################################
    exe=sys_app=sys_game=sys=web=None
    start=False
    if info[:4]=='��':
        b=info[4:]
        start=True
    else:
        b=info
    if b=='��ʾ����':
        os.startfile("bin\\Shows Desktop.lnk")
        feedback="����Ϊ����ʾ����"
    elif b=='�������':
        sys_app='control'
    elif b=='��ʾ':
        sys_app='DpiScaling'
    elif b=='������':
        sys_app='calc'
    elif b=='��ͼ':
        sys_app='mspaint'
    elif b=='���':
        sys_app='StikyNot'
    elif b=='��ͼ����':
        sys_app='SnippingTool'     
    elif b=='¼����':
        sys_app='SoundRecorder'
    elif b.lower()=='cmd' or b=='������' or b=='������ʾ��':
        sys_app='cmd'
    elif b=='�Ŵ�':
        sys_app='Magnify'
    elif b.lower()=='windows�ƶ�����' or b=='�ƶ�����':
        sys_app='mblctr'
    elif b=='ϵͳ����':
        sys_app='msconfig'
    elif b=='ϵͳ��Ϣ':
        sys_app='msinfo32'
    elif b=='�û��˻�':
        sys_app='Netplwiz'
    elif b=='��Ļ����':
        sys_app='osk'
    elif b=='ע���༭��' or b=='ע���':
        sys_app='regedt32'
    elif b=='�����ϳ���' or b=='�����ϳ�' or b=='����������' or b=='��������' or b=='����':
        sys_app='SndVol'
    elif b=='���������' or b.lower()=='windows���������':
        sys_app='taskmgr'
    elif b=='����' or b.lower()=='����windows' or b.lower()=='windows�汾' or b=='ϵͳ�汾':
        sys_app='winver'
    elif b=='��������':
        sys_app='cleanmgr'
    elif b=='������Ƭ����':
        sys_app='dfrgui'
    elif b=='����' or b=='���������':
        sys_app='CompMgmtLauncher'
    elif b=='��Դ������':
        sys_app='resmon'
    elif b.lower()=='windows����' or b.lower()=='�򿪻�ر�windows����':
        sys_app='OptionalFeatures'
    elif b=='���ݺͻ�ԭ' or b=='����' or b=='ϵͳ����':
        sys_app='sdclt'
    elif b=='ϵͳ��ԭ':
        sys_app='rstrui'
    elif b=='ϵͳ����' or b=='ϵͳ�߼�����' or b=='�߼�ϵͳ����' or b=='�߼�ϵͳ����':
        sys_app='SystemPropertiesAdvanced'
    elif b=='�û��˻�����' or b=='�˻�����':
        sys_app='UserAccountControlSettings'
    elif b=='���ɷ�������' or b=='���ɷ���':
        sys_app='Utilman'
    elif b=='����':
        sys_app='services.msc'
    elif b=='���̹���' or b=='���̹�����':
        sys_app='diskmgmt.msc'
    elif b=='�豸������' or b=='�豸����':
        sys_app='devmgmt.msc'
    elif b=='��ӡ����' or b=='��ӡ������' or b=='��ӡ��':
        sys_app='printmanagement.msc'    
    elif b=='ɨ��':
        sys_game='MineSweeper'
    elif b=='�յ�����':
        sys_game='FreeCell'
    elif b=='ֽ��':
        sys_game='Solitaire'
    elif b=='֩��ֽ��':
        sys_game='SpiderSolitaire'
    elif b=='�齫':
        sys_game='Mahjong'
    elif b=='���Ĵ�ս':
        sys_game='Hearts'
    elif b=='��������':
        sys_game='Chess'
    elif b=='˫½��':
        sys_game='InternetBackgammon'
    elif b=='��ά����':
        sys_game='3DPinlinkall'
    elif b=='����':
        sys_game='InternetCheckers'
    elif b=='������':
        sys_game='InternetSpades'
    elif b=='���±�':
        sys='notepad'
    elif b=='д�ְ�':
        sys='write'
    elif b=='����' or b=='Windows������֧��':
        sys='winhlp32'
    elif b=='��' or b=='�����' or b=='�ҵĵ���' or b.lower()=='windows��Դ������':
        sys='explorer'
    elif b=='����վ':
        os.popen('explorer.exe ::{645FF040-5081-101B-9F08-00AA002F954E}')
        feedback='����Ϊ����%s'%b
    elif b=='�����ھ�' or b=='����':
        os.popen('explorer.exe ::{208D2C60-3AEA-1069-A2D7-08002B30309D}')
        feedback='����Ϊ����%s'%b
    elif b=='�ҵ��ĵ�':
        os.popen('explorer.exe ::{450D8FBA-AD25-11D0-98A8-0800361B1103}')
        feedback='����Ϊ����%s'%b
    elif b.lower()=='c��'or b.lower()=='c':
        os.popen('%SystemRoot%\explorer.exe /n,/e,C:\\')
        feedback='����Ϊ����%s��'%b[:1]
    elif b.lower()=='d��'or b.lower()=='d':
        os.popen('%SystemRoot%\explorer.exe /n,/e,D:\\')
        feedback='����Ϊ����%s��'%b[:1]
    elif b.lower()=='e��'or b.lower()=='e':
        os.popen('%SystemRoot%\explorer.exe /n,/e,E:\\')
        feedback='����Ϊ����%s��'%b[:1]
    elif b.lower()=='f��'or b.lower()=='f':
        os.popen('%SystemRoot%\explorer.exe /n,/e,F:\\')
        feedback='����Ϊ����%s��'%b[:1]
    elif b.lower()=='g��'or b.lower()=='g':
        os.popen('%SystemRoot%\explorer.exe /n,/e,G:\\')
        feedback='����Ϊ����%s��'%b[:1]
    elif b.lower()=='h��'or b.lower()=='h':
        os.popen('%SystemRoot%\explorer.exe /n,/e,H:\\')
        feedback='����Ϊ����%s��'%b[:1]
    elif b.lower()=='i��'or b.lower()=='i':
        os.popen('%SystemRoot%\explorer.exe /n,/e,J:\\')
        feedback='����Ϊ����%s��'%b[:1]
    elif b.lower()=='j��'or b.lower()=='j':
        os.popen('%SystemRoot%\explorer.exe /n,/e,K:\\')
        feedback='����Ϊ����%s��'%b[:1]
    elif b=='�ٶ�'or b=='�����'or b.lower()=='baidu':
        web='http://www.baidu.com'
    elif b=='����'or b=='�ٶ�����'or b=='tieba':
        web='http://tieba.baidu.com'
    elif b=='�ٶ���':
        web='http://yun.baidu.com'
    elif b=='�ٶȵ�ͼ':
        web='http://map.baidu.com'
    elif b=='�ſ�'or b=='�ſ���'or b.lower()=='youku':
        web='http://www.youku.com' 
    elif b=='������':
        web='http://www.tudou.com' 
    elif b=='����'or b=='������'or b.lower()=='douban':
        web='http://www.douban.com'
    elif b=='�����Ӱ':
        web='http://movie.douban.com'
    elif b=='QQ�ռ�'or b.lower()=='qzone':
        web='http://qzone.qq.com'
    elif b=='����':
        web='http://www.163.com'
    elif b=='��������'or b=='163����':
        web='http://mail.163.com'
    elif b.lower()=='qq����':
        web='http://mail.qq.com'
    elif b=='����������'or b=='��������':
        web='http://music.163.com'
    elif b=='������'or b.lower()=='iqiyi':
        web='http://www.iqiyi.com'
    elif b.lower()=='����fm':
        web='http://fm.douban.com'
    elif b=='�Ѻ�'or b=='�Ѻ���':
        web='http://www.sohu.com'
    elif b=='�Ѻ���Ƶ':
        web='http://tv.sohu.com'
    elif b=='����'or b=='������'or b.lower()=='sina':
        web='http://www.sina.com'
    elif b=='΢��'or b=='����΢��'or b.lower()=='weibo':
        web='http://www.weibo.com'
    elif b=='��Ѷ��'or b.lower()=='tencent':
        web='http://www.qq.com'
    elif b=='������':
        web='http://www.renren.com'
    elif b=='�����':
        web='http://www.ifeng.com'
    elif b=='Я��'or b=='Я����':
        web='http://www.ctrip.com'
    elif b=='ȥ�Ķ�'or b=='ȥ�Ķ���'or b=='ȥ��'or b=='ȥ����':
        web='http://www.qunar.com'
    elif b=='�йش�'or b=='�йش�����':
        web='http://www.zol.com.cn'
    elif b=='����֮��'or b=='autohome':
        web='http://www.autohome.com'
    elif b=='�ϼ���':
        web='http://www.ganji.com'
    elif b=='������'or b.lower()=='cctv':
        web='http://www.ctrip.com'
    elif b=='������':
        web='http://www.people.com.cn'
    elif b=='�»���':
        web='http://www.xinhuanet.com' 
    elif b=='������':
        web='http://www.huanqiu.com'
    elif b=='�����籨'or b=='�����籨��':
        web='http://www.zaobao.com'
    elif b=='��������':
        web='http://news.163.com'
    elif b=='�Ա�'or b=='�Ա���'or b.lower()=='taobao':
        web='http://www.taobao.com'
    elif b=='��è'or b=='��è��':
        web='http://www.tmall.com'
    elif b=='����'or b=='������':
        web='http://www.jd.com'
    elif b=='����ѷ'or b.lower()=='amazon':
        web='http://www.amazon.cn'
    elif b=='�����׹�':
        web='http://www.suning.com'
    elif b=='����'or b=='������':
        web='http://www.dangdang.com'
    elif b=='����'or b=='������':
        web='http://www.meituan.com'
    elif b=='��������':
        web='http://waimai.meituan.com'
    elif b=='����ô':
        web='http://www.ele.me'
    elif b=='������':
        web='http://www.meilijie.com'
    elif b=='����˵':
        web='http://www.meilishuo.com'
    elif b=='ΨƷ��':
        web='http://www.vip.com'
    elif b=='1�ŵ�':
        web='http://www.yhd.com'
    elif b=='������Ʒ':
        web='http://www.jumei.com'
    elif b=='�ۻ���':
        web='http://ju.taobao.com'
    elif b=='Ŵ��'or b=='�ٶ�Ŵ��'or b=='Ŵ���Ź�':
        web='http://www.nuomi.com'
    elif b=='����'or b=='���ͳ�Ʒ':
        web='http://www.vancl.com'
    elif b=='����'or b=='������':
        web='http://www.lashou.com'
    elif b=='yitao':
        web='http://www.etao.com'
    elif b=='Ģ����':
        web='http://www.mogujie.com'
    elif b=='���Ա�':
        web='http://ai.taobao.com'
    elif b=='������'or b=='��������':
        web='http://www.tianya.com'
    elif b=='�ٺ���':
        web='http://www.baihe.com'
    elif b=='�䰮��':
        web='http://www.zhenai.com'
    elif b=='���ͼ�Ե':
        web='http://www.jiayuan.com'
    elif b=='������':
        web='http://www.weifeng.com'
    elif b=='è����'or b=='è�˴��ӻ�':
        web='http://www.mop.com'
    elif b=='���ڵ���':
        web='http://www.dianping.com'
    elif b=='58ͬ��':
        web='http://www.58.com'
    elif b=='12306'or b=='��Ʊ':
        web='http://www.12306.cn'
    elif b=='ά��'or b=='ά���ٿ�'or b=='wikipedia':
        web='http://zh.wikipedia.org'
    elif b=='�����ٿ�':
        web='http://www.baike.com'
    elif b.lower()=='lofter':
        web='http://www.lofter.com'
    elif b=='�࿴'or b=='�࿴�Ķ�':
        web='http://www.duokan.com'
    elif b=='��������':
        web='http://www.baozoumanhua.com'
    elif b=='������'or b=='����������':
        web='http://www.u17.com'
    elif b=='����'or b=='������':
        web='http://www.guokr.com'
    elif b=='36�'or b.lower()=='36kr':
        web='http://www.36kr.com'
    elif b=='������'or b.lower()=='ifanr':
        web='http://www.ifanr.com'
    elif b=='�嵰'or b=='�嵰��':
        web='http://www.jiandan.com'
    elif b=='��ѧ�����':
        web='http://www.songshuhui.com'
    elif b=='����լ����':
        web='http://www.gn00.com'
    elif b=='����լ�Ľ��'or b.lower()=='0xaa55':
        web='http://www.0xaa55.com'
    elif b.lower()=='jackeriss'or b.lower()=='jc'or b.lower()=='jack criss':
        web='http://www.jackeriss.com'
    elif b=='�߲����г�����'or b=='�߲����г�'or b=='�߲��������г�'or b=='�߲�'or b.lower()=='bamboo bike':
        web='http://www.gn00.com'
    elif b=='Ľ��'or b=='Ľ����':
        web='http://www.imooc.com'
    elif b=='������Ƹ':
        web='http://www.zhaopin.com'
    elif b=='ǰ������':
        web='http://www.51job.com'
    elif b=='֪��'or b=='֪����':
        web='http://www.zhihu.com'
    elif b=='����'or b=='������':
        web='http://www.huxiu.com'
    elif b=='����'or b=='������':
        web='http://www.duitang.com'
    elif b=='������':
        web='http://www.ikanchai.com'
    elif b=='��������'or b.lower()=='bվ'or b.lower()=='bilibili':
        web='http://www.bilibili.com'
    elif b.lower()=='acfun'or b.lower()=='aվ':
        web='http://www.acfun.tv'
    elif b=='����'or b=='����ֱ��'or b.lower()=='����tv':
        web='http://www.douyutv.com'
    elif b.lower()=='yy'or b.lower()=='yyֱ��':
        web='http://www.yy.com'
    elif b=='ս��'or b.lower()=='ս��tv':
        web='http://www.zhanqi.tv'
    elif b=='17173':
        web='http://www.17173.com'
    elif b=='�����ǿ�':
        web='http://www.gamesky.com'
    elif b=='ս��':
        web='http://www.battlenet.cn'
    elif b.lower()=='steam':
        web='http://store.steampowered.com'
    elif b.lower()=='twitch':
        web='http://www.twitch.com'
    elif b=='����'or b.lower()=='twitter':
        web='http://www.twitter.com'
    elif b=='����'or b.lower()=='facebook':
        web='http://www.facebook.com'
    elif b=='�ȸ�'or b.lower()=='google':
        web='http://www.google.com'
    elif b.lower()=='youtube':
        web='http://www.youtube.com'
    elif b.lower()=='ebay':
        web='http://www.ebay.com'
    elif b.lower()=='github':
        web='http://www.github.com'
    elif b=='�Ż�'or b.lower()=='yahoo':
        web='http://www.yahoo.com'
    if sys_app:
        thread.start_new_thread(subprocess.Popen,(sys_app,))
        feedback='����Ϊ����%s'%b           
    elif sys_game:
        thread.start_new_thread(os.startfile,(programfiles_path+'/Microsoft Games/'+sys_game+'/'+sys_game+'.exe',))
        feedback='����Ϊ����%s'%b 
    elif sys:
        thread.start_new_thread(subprocess.Popen,(sys,))
        feedback='����Ϊ����%s'%b
    elif web:
        webbrowser.open_new_tab(web)
        feedback='����Ϊ����%s'%b
    if not feedback:
        if info.isalpha():
            if info.count(' ')<2:
                feedback=iciba(info)
###########################################################################################
#the_time
###########################################################################################
    if '����' in info:
        if '����' in info:
            feedback=time_now(0)
        elif '����' in info:
            feedback=time_now(2)
        elif '�����' in info:
            feedback=time_now(6)
        elif '����' in info:
            feedback=time_now(4)
        elif '����' in info:
            feedback=time_now(8)
        elif '��ǰ��' in info:
            feedback=time_now(12)
        elif 'ǰ��' in info:
            feedback=time_now(10)
    elif '���ڼ�' in info or '�ܼ�' in info:
        if '����' in info:
            feedback=time_now(1)
        elif '����' in info:
            feedback=time_now(3)
        elif '�����' in info:
            feedback=time_now(7)
        elif '����' in info:
            feedback=time_now(5)
        elif '����' in info:
            feedback=time_now(9)
        elif '��ǰ��' in info:
            feedback=time_now(13)
        elif 'ǰ��' in info:
            feedback=time_now(11)
    elif info == 'ʱ��' or info == '����ʱ��' or '������' in info or '���ڼ���' in info:
        feedback=time_now(14)
    elif info == '����':
        feedback=time_now(15)
    elif 'ʱ��' in info and '����' in info:
        feedback=time_now(16)
###########################################################################################
#chat
###########################################################################################
    chat_file=open("data/db/chat.txt","r")
    over=False
    answer=False
    Type=0
    while not over:
        chat_info=chat_file.readline().strip('\n')
        if chat_info=='':
            over=True
            break
        questions=chat_info[:chat_info.index(':')].split(';')
        answers=chat_info[chat_info.index(':')+1:].split(';')
        for i in range(0,len(questions)):
            if info == questions[i]:                
                answer=random.choice(answers)
                over=True
    chat_file.close()
    if answer:
        feedback = answer
    else:
        re_dirty_words=['��Ҫ˵�໰�����Ե����low��','���Ѿ���������ˣ��벻Ҫ˵�໰��','��TM�ĸ�TM����TM��������TM�ı�TM�ĸ�����Ҫ����']
        dirty_words_time=0
        dirty_words_file=open("data/db/dirty_words.txt","r")
        over=False
        while not over:
            dirty_words=dirty_words_file.readline().strip('\n')
            if dirty_words=='':
                over=True
                break
            if dirty_words in info:
                dirty_words_time_file=open("data/db/dirty_words_time.txt","r")
                dirty_words_time=int(dirty_words_time_file.readline().strip('\n'))
                feedback=re_dirty_words[dirty_words_time%len(re_dirty_words)]
                dirty_words_time+=1
                dirty_words_time_file.close()
                dirty_words_time_file=open("data/db/dirty_words_time.txt","w")
                dirty_words_time_file.write('%d'%dirty_words_time)
                dirty_words_time_file.close()
                over=True
        dirty_words_file.close()
###########################################################################################
#reminder
###########################################################################################
    if not feedback:
        if '������' in info:
            event=info[info.index('������')+6:]
            if event:
                remind='���ˣ���'+event+'�ˣ�'
                remind_file=open("data/db/reminder.txt","w")
                remind_file.write(remind)
                remind_file.close()
                when=info[:info.index('������')]
                if when:
                    special_format=True
                    style_path_file=open("data/settings/style_path.txt","r")
                    style_path=style_path_file.read()
                    style_path_file.close()
                    href_file=open(style_path+"href.txt","r")
                    href=href_file.read()
                    href_file.close()
                    if '��'in when:
                        (h,m,s)=count_down(when)
                        h=int(h)
                        m=int(m)
                        s=int(s)
                        second=3600*h+60*m+s
                        thread.start_new_thread(reminder, (second,))
                        feedback ='<p style="font-family:Microsoft Yahei;font:24px">OK,��������������֮ǰ��ɲ�Ҫ�ص���Ŷ������˭ȥ�����㣿do���������ĵ�˵��<br><a style="text-decoration:none;color:#'+href+'" href="#">ȡ������</a></p>'
                    if not feedback:
                        exact_when=exact_time(when)
                        date=time.strftime("%Y%m%d", time.localtime())
                        whole_time=exact_when+date
                        second=time.mktime(time.strptime(whole_time,"%H:%M%Y%m%d"))-time.time()
                        thread.start_new_thread(reminder, (second,))
                        feedback ='<p style="font-family:Microsoft Yahei;font:24px">OK,��������������֮ǰ��ɲ�Ҫ�ص���Ŷ������˭ȥ�����㣿do���������ĵ�˵��<br><a style="text-decoration:none;color:#'+href+'" href="#">ȡ������</a></p>'
                else:
                    feedback="��û������������ʲôʱ�������㣬���ø������ı����˵һ�顣"
            else:
                feedback="��û��������������������ʲô�����ø������ı����˵һ�顣"
        else:
            shutdown=restart=False
            if '�ػ�' in info:
                if '�ػ�'==info:
                    subprocess.Popen('shutdown -s')
                    feedback='ûʱ�����ˣ��ټ�~'
                    shutdown=False
                else:
                    when=info[:info.index('�ػ�')]
                    shutdown=True
            elif '�ص���' in info:
                if '�ص���'==info:
                    subprocess.Popen('shutdown -s')
                    feedback='ûʱ�����ˣ��ټ�~'
                    shutdown=False
                else:
                    when=info[:info.index('�ص���')]
                    shutdown=True
            elif '�رռ����' in info:
                if '�رռ����'==info:
                    subprocess.Popen('shutdown -s')
                    feedback='ûʱ�����ˣ��ټ�~'
                    shutdown=False
                else:
                    when=info[:info.index('�رռ����')]
                    shutdown=True
            elif '�رյ���' in info:
                if '�رյ���'==info:
                    subprocess.Popen('shutdown -s')
                    feedback='ûʱ�����ˣ��ټ�~'
                    shutdown=False
                else:
                    when=info[:info.index('�رյ���')]
                    shutdown=True
            if shutdown:
                special_format=True
                style_path_file=open("data/settings/style_path.txt","r")
                style_path=style_path_file.read()
                style_path_file.close()
                href_file=open(style_path+"href.txt","r")
                href=href_file.read()
                href_file.close()
                if '��'in when:
                    (h,m,s)=count_down(when)
                    h=int(h)
                    m=int(m)
                    s=int(s)
                    second=3600*h+60*m+s
                    subprocess.Popen('shutdown -a', shell=True)
                    subprocess.Popen('shutdown -s -t %d'%second, shell=True)
                    feedback ='<p style="font-family:Microsoft Yahei;font:24px">���ļ��������'
                    if h!=0:
                        feedback +='%dСʱ'%h
                    if m!=0:
                        feedback +='%d����'%m
                    if s!=0:
                        feedback +='%d��'%s            
                    feedback = feedback+'��رա�do�����಻���˵��<br><a style="text-decoration:none;color:#'+href+'" href="#">ȡ���ػ�</a></p>'
                if not feedback:
                    exact_when=exact_time(when)
                    date=time.strftime("%Y%m%d", time.localtime())
                    whole_time=exact_when+date
                    second=time.mktime(time.strptime(whole_time,"%H:%M%Y%m%d"))-time.time()
                    if second<0:
                        second+=86400
                    subprocess.Popen('shutdown -a', shell=True)        
                    subprocess.Popen('shutdown -s -t %d'%second, shell=True)
                    feedback ='<p style="font-family:Microsoft Yahei;font:24px">���ļ��������'+exact_when+'�رա�do�����಻���˵��<br><a style="text-decoration:none;color:#'+href+'" href="#">ȡ���ػ�</a></p>'
            else:
                if '��������' in info:
                    if '��������'==info:
                        subprocess.Popen('shutdown -r', shell=True)
                        feedback='���İɣ��������Ͼͻ��ټ���ģ�'
                        restart=False
                    else:
                        when=info[:info.index('��������')]
                        restart=True
                elif '����' in info:
                    if '����'==info:
                        subprocess.Popen('shutdown -r', shell=True)
                        feedback='���İɣ��������Ͼͻ��ټ���ģ�'
                        restart=False
                    else:
                        when=info[:info.index('����')]
                        restart=True
                if restart:
                    special_format=True
                    style_path_file=open("data/settings/style_path.txt","r")
                    style_path=style_path_file.read()
                    style_path_file.close()
                    href_file=open(style_path+"href.txt","r")
                    href=href_file.read()
                    href_file.close()
                    if '��'in when:
                        (h,m,s)=count_down(when)
                        h=int(h)
                        m=int(m)
                        s=int(s)
                        second=3600*h+60*m+s
                        subprocess.Popen('shutdown -a', shell=True)
                        subprocess.Popen('shutdown -r -t %d'%second, shell=True)
                        feedback ='<p style="font-family:Microsoft Yahei;font:24px">���ļ��������'
                        if h!=0:
                            feedback +='%dСʱ'%h
                        if m!=0:
                            feedback +='%d����'%m
                        if s!=0:
                            feedback +='%d��'%s
                        feedback +='��������do�����಻���˵��<br><a style="text-decoration:none;color:#'+href+'" href="#">ȡ���ػ�</a></p>'                                    
                    if not feedback:
                        exact_when=exact_time(when)
                        date=time.strftime("%Y%m%d", time.localtime())
                        whole_time=exact_when+date
                        second=time.mktime(time.strptime(whole_time,"%H:%M%Y%m%d"))-time.time()
                        if second<0:
                            second+=86400
                        subprocess.Popen('shutdown -a', shell=True)        
                        subprocess.Popen('shutdown -r -t %d'%second, shell=True)
                        feedback ='<p style="font-family:Microsoft Yahei;font:24px">���ļ��������%s������do�����಻���˵��<br><a style="text-decoration:none;color:#'+href+'" href="#">ȡ���ػ�</a></p>'%exact_when
                elif 'ע��'==info:
                    subprocess.Popen('shutdown -r', shell=True)
                    feedback='�㻹������Ķ԰ɣ����뿪̫�ã��һ������ģ�'
                    logout=False
                elif '����'==info:
                    subprocess.Popen('powercfg -h on', shell=True)
                    subprocess.Popen('shutdown -h', shell=True)
                    feedback='����������������ˣ���Ҫ�����ˡ���zzZ'
                    hibernation=False
                elif '˯��'==info:
                    subprocess.Popen('powercfg -h off', shell=True)
                    subprocess.Popen('rundll32.exe powrprof.dll,SetSuspendState', shell=True)
                    subprocess.Popen('powercfg -h on', shell=True)
                    feedback ='����zzZ ������������ң��˼�˯�������أ�'
                elif '����'==info or '����'==info or'���������'==info:
                    subprocess.Popen('rundll32 user32.dll,LockWorkStation', shell=True)
                    feedback ='Կ�����������ҿ����˰���'

###########################################################################################
#wiki
###########################################################################################
    if info=="���" or info=="��" or info=="���" or info=="��ð�" or info=="����":
        if "(" in current_theme and ")" in current_theme:
            feedback="��ã��ҽд�ף������˽�˽�������"
    if "����˭" in info or "���ɶ" in info or "���ʲô" in info or "��ʲô����" in info or "���������ʲô" in info or "���ɶ��" in info:
        if "(" in current_theme and ")" in current_theme:
            feedback="��ã��ҽд�ף������˽�˽�������"
        elif current_theme=="����10032��":
            feedback="�ҵ����������࣬�ǽ����˵Ŀ�¡�塣"
        elif current_theme=="Stuart":
            feedback="�ң�Stuart��"
        elif current_theme=="����A��":
            feedback="�ҽж���A�Σ���һֻ����22���͵�è�ͻ����ˣ�"
    if "������" in info or "���������" in info or "�㼸����" in info or "����꼸��" in info or "�������" in info:
        if "(" in current_theme and ")" in current_theme:
            feedback="������"+str(int(time.strftime("%Y", time.localtime()))-2014)+"��ɣ�"
        elif current_theme=="����10032��":
            feedback="�������14�ꡣ"
        elif current_theme=="Stuart":
            feedback="��ÿ�����Ӱ��С���ˡ��������������֮ǰ���������ˣ�"
        elif current_theme=="����A��":
            feedback="��2112����������Խ���Ӧ����"+str(int(time.strftime("%Y", time.localtime()))-2112)+"�꣡"
    if "�������" in info or "��ʲôʱ�������" in info or "��ɶʱ������" in info or "��ĳ�������" in info or "��ʲôʱ�������" in info:
        if "(" in current_theme and ")" in current_theme:
            feedback="2014��11��07�� ��������~"
        elif current_theme=="����10032��":
            feedback="�����ǿ�¡�ˣ����Ѿ����ǵ��Լ�ʲôʱ����������ˡ���ֻ֪�������˵�������5��2�ա�"
        elif current_theme=="Stuart":
            feedback="��...�ǺǺ�..."
        elif current_theme=="����A��":
            feedback="����2112��9��3�ճ����ģ�"
    if "�����еĻ���Ů��" in info or "����Ա�" in info or "����GG����MM" in info or "����������" in info or "���Ǻ��ӻ�������" in info:
        if "(" in current_theme and ")" in current_theme:
            feedback="�ҵĳ����ҵ������趨Ϊ���ԡ�"
        elif current_theme=="����10032��":
            feedback="���������á�"
        elif current_theme=="Stuart":
            feedback="�ۣ�����ò��û���Ա𡣰�����������"
        elif current_theme=="����A��":
            feedback="���ǹ��ģ�"
    if info=="ɨ����" or info.lower()=="scan me":
        if "(" in current_theme and ")" in current_theme:
            feedback="ɨ����ɣ���û���ܵ����ˣ����ǣ���ĺɶ���ˮƽ���񾭵��ʶ���ʾ�����쳣������������������������Ⱥ��֢״�������ഺ���궯��ֱ����˵���Һ���������չˡ����ҲŻ����������"
        elif current_theme=="����10032��":
            feedback="���ҵ�������"
        elif current_theme=="Stuart":
            feedback="�ҳ���ô����۾��ɲ�������������ģ�"
        else:
            feedback="ι��������ˣ����ֲ��Ǵ�ף�"
    if info=="�Һ���������չ�" or info=="�Ҷ�����չ˺�����":
        if "(" in current_theme and ")" in current_theme:
            quit()
        elif current_theme=="����A��":
            feedback="��Ȼ��Ҳ�Ǹ������ˣ����ҵ�ʹ���������Ҹ����ڴ�֮ǰ���ǲ������뿪��ģ�"
        elif current_theme=="Stuart":
            feedback="лл���ˣ������ģ��������Ҳ̫�������ˣ���Gru��Զ�ˣ���"
        elif current_theme=="����10032��":
            feedback="...�����������Ĳ�����"
    if "���׸�" in info or "������" in info or "����" in info:
        if current_theme=="Stuart":
            feedback="@sing"
            special_format=True
        elif current_theme=="����10032��":
            feedback="С���˳����ر�������Ҳ�ƭ�㣬��ģ�"
        elif current_theme=="����A��":
            feedback="�����о�С���˳���ר�������ȥ�������㳪һ�װɣ�"
        else:
            feedback="�ܱ�Ǹ�Ҳ��ᳪ�裬��������˵С���˸������������ĸ��֣�"
    if info=="������" or info=="������":
        if current_theme=="����A��":
            fb=["","ǰ"]
            zeros=["0","00","000"]
            feedback="��ӭ������Ԫ"+random.choice(fb)+str(random.randint(1,99))+random.choice(zeros)+"��"
        elif current_theme=="Stuart":
            feedback="��ֻ��˵������ɫä���㾹Ȼ�ǻ���ɫä���ǺǺǣ�"
        elif current_theme=="����10032��":
            feedback="�����������ȱ�ݵ�����Radio Noise������������������˵�������š�"
        elif "(" in current_theme and ")" in current_theme:
            feedback="���ǰ����ӣ����������ӣ���һ���Ҿͱ����ڡ������š����ˣ���������"
    if not feedback:
        try:
            feedback = movie(info)
        except:
            pass
        if feedback:
            special_format=True
    if not feedback:
        try:
            feedback = zhidao(info)
        except:
            pass
    if not feedback:
        try:
            feedback = wiki(info)
        except:
            pass
        if feedback:
            special_format=True
    if not feedback:
        if info[-4:]=="��˭":
            info1=info[:-4]
            try:
                feedback = wiki(info1)
            except:
                pass
            if feedback:
                special_format=True
        elif info[:4]=="˭��":
            info1=info[4:]
            try:
                feedback = wiki(info1)
            except:
                pass
            if feedback:
                special_format=True
    if not feedback or feedback=='<p style="font-family:Microsoft Yahei;font:24px">����������������</p>'or feedback=='����������������':
        temp = None
        temp = blur(info,q)
        if temp:
            feedback=temp
    if not feedback:
        style_path_file=open("data/settings/style_path.txt","r")
        style_path=style_path_file.read()
        style_path_file.close()
        href_file=open(style_path+"href.txt","r")
        href=href_file.read()
        href_file.close()
        feedback = '��֪����'+origin_info+'����ʲô��˼�������<a style="text-decoration:none;color:#'+href+'"href="http://www.baidu.com/baidu?word='+origin_info+'">�ٶ�һ��</a>'
    if special_format:
        feedback = '<p style="font-family:Microsoft Yahei;font:24px">'+current_theme+'��</p>'+feedback
    else:
        if current_theme=="����10032��":
            adv=["һ��������","һ��������","һ��������","�����","ǿ����Ц��","���ĵ�","���ε�","������","������"]
            feedback = '<p style="font-family:Microsoft Yahei;font:24px">'+current_theme+'��'+feedback+'��do������'+random.choice(adv)+'˵��</p>'
        else:
            feedback = '<p style="font-family:Microsoft Yahei;font:24px">'+current_theme+'��'+feedback+'</p>'
    return feedback
