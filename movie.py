#!/usr/bin/env python
#-*- encoding: gbk -*-
import urllib2,requests,string,webbrowser,time,thread,Image
from urllib2 import Request, urlopen
from delete_pic import *
def movie(Key):
    page1=None
    feedback = None
    point=None
    juqing=False
    key=Key.decode('gbk').encode('utf8')
    url1='http://movie.douban.com/subject_search?search_text='+Key+'&cat=1002'
    try:
        page1 = urllib2.urlopen(url1)
    except:
        feedback = '<p style="font-family:Microsoft Yahei;font:24px">����������������</p>'
    if page1:
        url2=page1.read()
        if "�ʴ�".decode('gbk').encode('utf8') in url2 and "����".decode('gbk').encode('utf8') in url2:
            url2=url2[url2.index("�ʴ�".decode('gbk').encode('utf8')):url2.index("����".decode('gbk').encode('utf8'))]
            if key in url2:
                url2=url2[:url2.index(key)]
                if 'nbg" href='.decode('gbk').encode('utf8') in url2 and "onclick".decode('gbk').encode('utf8') in url2:
                    url2=url2[url2.index('nbg" href='.decode('gbk').encode('utf8'))+11:url2.index("onclick".decode('gbk').encode('utf8'))-2]
                    url2=url2.decode('utf8').encode('gbk')
                    page2=None
                    try:
                        page2 = urllib2.urlopen(url2)
                    except:
                        feedback = '<p style="font-family:Microsoft Yahei;font:24px">����������������</p>'
                    if page2:
                        text=page2.read()
                        text2=text
                        if "<title>".decode('gbk').encode('utf8') in text and "</title>".decode('gbk').encode('utf8') in text:
                            title=text[text.index("<title>".decode('gbk').encode('utf8'))+7:text.index("</title>".decode('gbk').encode('utf8'))].replace(" (����)".decode('gbk').encode('utf8'),"")
                        if "�ʴ�".decode('gbk').encode('utf8') in text and "����".decode('gbk').encode('utf8') in text:
                            text=text[text.index("�ʴ�".decode('gbk').encode('utf8')):text.index("����".decode('gbk').encode('utf8'))]
                            if "��������ຣ��".decode('gbk').encode('utf8') in text:
                                url3=text[text.index("��������ຣ��".decode('gbk').encode('utf8')):text.index("��������ຣ��".decode('gbk').encode('utf8'),text.index("��������ຣ��".decode('gbk').encode('utf8'))+1)]
                                if "src=".decode('gbk').encode('utf8') in url3 and "title=".decode('gbk').encode('utf8') in url3:
                                    url3=url3[url3.index("src=".decode('gbk').encode('utf8'))+5:url3.index("title=".decode('gbk').encode('utf8'))-2]      
                            if "������������".decode('gbk').encode('utf8')in text:
                                point=None
                            elif "v:votes".decode('gbk').encode('utf8') in text:
                                votes=text[text.index("v:votes".decode('gbk').encode('utf8'))+9:-10]
                                if int(votes)<=10000:
                                    point=None
                                elif "v:average".decode('gbk').encode('utf8') in text and "</strong>".decode('gbk').encode('utf8') in text:
                                    point=text[text.index("v:average".decode('gbk').encode('utf8'))+11:text.index("</strong>".decode('gbk').encode('utf8'))]
                            if point:
                                if "����".decode('gbk').encode('utf8') in text:
                                    if "IMDb".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("IMDb".decode('gbk').encode('utf8'))]
                                    elif "����".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("����".decode('gbk').encode('utf8'))]
                                    elif "Ƭ��".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("Ƭ��".decode('gbk').encode('utf8'))]
                                    elif "����".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("����".decode('gbk').encode('utf8'))]
                                    elif "�ײ�".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("�ײ�".decode('gbk').encode('utf8'))]
                                elif "���".decode('gbk').encode('utf8') in text:
                                    if "IMDb".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("���".decode('gbk').encode('utf8')):text.index("IMDb".decode('gbk').encode('utf8'))]
                                    elif "����".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("���".decode('gbk').encode('utf8')):text.index("����".decode('gbk').encode('utf8'))]
                                    elif "Ƭ��".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("���".decode('gbk').encode('utf8')):text.index("Ƭ��".decode('gbk').encode('utf8'))]
                                    elif "����".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("���".decode('gbk').encode('utf8')):text.index("����".decode('gbk').encode('utf8'))]
                                    elif "�ײ�".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("���".decode('gbk').encode('utf8')):text.index("�ײ�".decode('gbk').encode('utf8'))]
                                elif "����".decode('gbk').encode('utf8') in text:
                                    if "IMDb".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("IMDb".decode('gbk').encode('utf8'))]
                                    elif "����".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("����".decode('gbk').encode('utf8'))]
                                    elif "Ƭ��".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("Ƭ��".decode('gbk').encode('utf8'))]
                                    elif "����".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("����".decode('gbk').encode('utf8'))]
                                    elif "�ײ�".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("�ײ�".decode('gbk').encode('utf8'))]
                                elif "����".decode('gbk').encode('utf8') in text:
                                    if "IMDb".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("IMDb".decode('gbk').encode('utf8'))]
                                    elif "����".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("����".decode('gbk').encode('utf8'))]
                                    elif "Ƭ��".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("Ƭ��".decode('gbk').encode('utf8'))]
                                    elif "����".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("����".decode('gbk').encode('utf8'))]
                                    elif "�ײ�".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("����".decode('gbk').encode('utf8')):text.index("�ײ�".decode('gbk').encode('utf8'))]
                                if "������".decode('gbk').encode('utf8') in text2:
                                    if "&copy;����".decode('gbk').encode('utf8') in text2:
                                        juqing=True
                                        text2=text2[text2.index("������".decode('gbk').encode('utf8')):text2.index("&copy;����".decode('gbk').encode('utf8'))]
                                    else:
                                        if "��Ԥ��Ƭ��ͼƬ".decode('gbk').encode('utf8') in text2:
                                            juqing=True
                                            text2=text2[text2.index("������".decode('gbk').encode('utf8')):text2.index("��Ԥ��Ƭ��ͼƬ".decode('gbk').encode('utf8'))-len(key)]
                                        elif "��ͼƬ".decode('gbk').encode('utf8') in text2:
                                            juqing=True
                                            text2=text2[text2.index("������".decode('gbk').encode('utf8')):text2.index("��ͼƬ".decode('gbk').encode('utf8'))-len(key)]
                                        elif "�ĵ��Ӿ�ͼƬ".decode('gbk').encode('utf8') in text2:
                                            juqing=True
                                            text2=text2[text2.index("������".decode('gbk').encode('utf8')):text2.index("�ĵ��Ӿ�ͼƬ".decode('gbk').encode('utf8'))-len(key)]
                                if juqing:
                                    if "(չ��ȫ��)".decode('gbk').encode('utf8') in text2:
                                        text2="������:".decode('gbk').encode('utf8')+text2[text2.index("(չ��ȫ��)".decode('gbk').encode('utf8'))+14:]
                                
                                if juqing:
                                    text=text+text2
                                while "<".decode('gbk').encode('utf8') in text and ">".decode('gbk').encode('utf8') in text :
                                    text=text[:text.index("<".decode('gbk').encode('utf8'))]+text[text.index(">".decode('gbk').encode('utf8'))+1:]
                                text=text.replace(" ","").replace("&nbsp;".decode('gbk').encode('utf8'),"").replace("������������".decode('gbk').encode('utf8'),":").replace("&copy;����".decode('gbk').encode('utf8'),"").replace("\n\n","\n").replace("\n\n","\n").replace("\n\n","\n").replace("\n\n","\n").replace("\n\n","\n").strip("\n").replace("\n","<br>")
                                text=text.decode('utf8').encode('gbk')
                                url3=url3.decode('utf8').encode('gbk')
                                title=title.decode('utf8').encode('gbk')
                                page3=None
                                try:
                                    page3 = urllib2.urlopen(url3)
                                except:
                                    feedback = '<p style="font-family:Microsoft Yahei;font:24px">����������������</p>'
                                if page3:
                                    file_name="cache/"+time.strftime("%Y%m%d%H%M%S", time.localtime())
                                    image_info=requests.get(url3)
                                    with open(file_name+".jpg", "wb") as code:
                                        code.write(image_info.content)
                                        code.flush()
                                        code.close()
                                    im=Image.open(file_name+".jpg")
                                    im.save(file_name+".png")
                                    thread.start_new_thread(delete_pic,(file_name,))
                                style_path_file=open("data/settings/style_path.txt","r")
                                style_path=style_path_file.read()
                                style_path_file.close()
                                href_file=open(style_path+"href.txt","r")
                                href=href_file.read()
                                href_file.close()
                                if point:
                                    feedback='<div align=center><p style="font-family:Microsoft Yahei;font:24px">'+title+'</p></div><br><img src="'+file_name+'.png" style="float:left"/><div align=right><span style="font-family:Microsoft Yahei;font:20px;color:#'+href+'">�������֣�</span><span style="font-family:Microsoft Yahei;font:40px;color:#'+href+'">'+point+'</span></div><p style="font-family:Microsoft Yahei;font:15px">'+text+'<div align=right><a style="text-decoration:none;color:#'+href+'" href="'+url2+'">�����꿴</a></p></div><div align=left><a></a></div>'
                                else:
                                    feedback='<div align=center><p style="font-family:Microsoft Yahei;font:24px">'+title+'</p></div><br><img src="'+file_name+'.png" style="float:left"/><p style="font-family:Microsoft Yahei;font:15px">'+text+'<div align=right><a style="text-decoration:none;color:#'+href+'" href="'+url2+'">�����꿴</a></p></div><div align=left></div>'
    return feedback
if __name__=='__main__':
    info=raw_input('����Ϊ����Щʲô��')
    print movie(info)
