# -*coding:UTF-8*-
from tkinter import messagebox as tkmessagebox
from tkinter import simpledialog
from tkinter import Tk
from tkinter import Label as label
from tkinter import Button as Button
from tkinter import Menu as menu
from tkinter import Canvas,HIDDEN,NORMAL
import tkinter.font as tkFont
from tkinter import Text
from pygame import mixer
from time import sleep
import sys
import os
import random
import webbrowser
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 使用说明的文字
one='TkOS2.0使用教程\n'
two='1.打开并运行TkOS：\n您只需要打开main.py就可以运行\n'
three='2.使用TkOS：您可以打开开始菜单，进行天气查看；您也可以玩小游戏，和朋友们一起玩【快照抓拍】，\n或进入多功能区，也可以听音乐......随您所想！\n'
four='3.对TkOS的维护：作者会定期更新您的TkOS，并且我们会保留旧版，具体请关注TkOS2.0网站\n'
five='4.TkOS2.0的附加功能：您可以使用tkvision文本阅读器，对文本进行放大，来更方便的阅读文本\n'
six='5.TkOS的声明：作者zhihongwang250，保留一切权利！\n'
seven='以上内容并不完全代表本版的所有内容，各个版本有差异，您当前使用的是：\nTkOS2.0：普通实用版'

# 使用文档的文字
one1='请您在使用TkOS时仔细阅读文档，并正确使用，遵守条款！\n'
two2='1.对TkOS的安装：您在使用TkOS时，必须要安装pygame库，否则无法使程序启动！\n'
three3='2.对TkOS的声明：我们的TkOS TKVISION文本阅读器并非在所有场合时使用（仅在以下功能使用：自定义文档阅读，阅读教程，阅读使用文档），\n请悉知！\n'
four4='3.TkOS的版本更新：TkOS更新时，会在聊天区提示，您可以到TkOS2.0官网去下载\n'
five5='4.版权声明：TkOS1.0 2.0 作者：zhihongwang250，保留一切权利！\n如您要根据TkOS进行改编时，请在作品建议栏提示！\n\n'
six6='感谢您选择TkOS，请仔细阅读说明'

def tianqi():
    sf=tkmessagebox.askyesno('提示','我们即将打开天气预报，请在主页选择您的城市并查看，点击否停止')
    if sf==True:
        webbrowser.open('http://www.weather.com.cn/')
    else:
        return

def jiao():
    ft1 = tkFont.Font(family='等线', size=50, weight=tkFont.NORMAL)
    wenzi=Tk()
    wenzi.title("tkvision文本阅读器")
    wenzi.geometry('800x400')
    wenzi.iconbitmap("wenben.ico")
    wenben=label(wenzi,text=one+'\n'+two+'\n'+three+'\n'+four+'\n'+five+'\n'+six+'\n'+seven,font=ft1)
    wenben.pack()
    wenzi.mainloop()

def github():
    webbrowser.open('https://github.com/zhihongwang250/TkOS2.0')

def liao():
    webbrowser.open('https://gitter.im/TkOS10/community')

def hua():
    huahua = Tk()
    huahua.title('画图板')
    huahua.iconbitmap("qianbi.ico")
    w = Canvas(huahua, width=400, height=200, background='white')
    w.pack()
    def paint(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        w.create_oval(x1, y1, x2, y2, fill='red')
    w.bind('<B1-Motion>', paint)  #<B1-Motion>绑定鼠标左键事件

def jisuanqi():
    while True:
        number = simpledialog.askstring('计算器','请输入数学表达式: ')
        if not number:
            return
        try:
            tkmessagebox.showinfo('计算结果是：',eval(number)) # 计算数字 eval
            break
        except Exception:
            tkmessagebox.showerror('请注意！','表达式出现错误')
        finally:
            print('\n')

def jisuan_help():
    jisuan_help_gui=Tk()
    jisuan_help_gui.title("TkOS帮助：计算器的使用")
    jisuan_help_gui.iconbitmap("yiwen.txt")
    j=label(jisuan_help_gui,text='您可以点击计算器功能，然后输入数学表达式，即可帮您计算（可以进行有括号的计算）。\n\
            如果数学表达式出现错误，我们会将错误反馈给您，如果不想使用计算器，您可以点击取消键。')
    j.pack()
    jisuan_help_gui.mainloop()

def txt_help():
    txt_help_gui=Tk()
    txt_help_gui.title("TkOS帮助：txt文件怎么编辑")
    txt_help_gui.iconbitmap("yiwen.txt")
    o=label(txt_help_gui,text='您直接点击多功能区下面的【编辑文档】，即可编辑！')
    o.pack()
    txt_help_gui.mainloop()

def liao_help():
    liao_help_gui=Tk()
    liao_help_gui.title("TkOS帮助：聊天区的功能")
    liao_help_gui.iconbitmap("yiwen.ico")
    l=label(liao_help_gui,text='聊天区可以报告bug，提交建议，进行人工客服询问等，作者会在聊天区里通报作者最新的作品')
    l.pack()
    liao_help_gui.mainloop()

def wendang():
    wendang_gui=Tk()
    wendang_gui.title("tkvision文本阅读器")
    wendang_gui.iconbitmap("wenben.ico")
    wendang_gui.geometry('1020x500')
    ft2 = tkFont.Font(family='等线', size=50, weight=tkFont.NORMAL)
    wendang2=label(wendang_gui,text=one1+'\n'+two2+'\n'+three3+'\n'+four4+'\n'+five5+'\n'+six6+'\n',font=ft2)
    wendang2.pack()
    wendang_gui.mainloop()

def about():
    about_gui=Tk()
    about_gui.title("关于TkOS2.0")
    about_gui.iconbitmap("yiwen.ico")
    a=label(about_gui,text='TkOS2.0\n制作人zhihongwang250，\n保留一切权利！\n如果想了解更多信息，')
    a.pack()
    button5=Button(about_gui,text='请阅读我们的文档',command=wendang)
    button5.pack()
    about_gui.mainloop()

def bang():
    bang=Tk()
    bang.title("TkOS帮助")
    bang.iconbitmap("yiwen.ico")
    bang.geometry('300x200')
    bang1=label(bang,text='您好！欢迎来到TkOS帮助，您要问的是不是这些问题：')
    bang1.pack()
    button1=Button(bang,text='txt文件怎么编辑',command=txt_help)
    button1.pack()
    button2=Button(bang,text='计算器怎么使用',command=jisuan_help)
    button2.pack()
    button4=Button(bang,text='聊天区可以干什么',command=liao_help)
    button4.pack()
    label2=label(bang,text='如果您要问的不是这些，请')
    label2.pack()
    button3=Button(bang,text='点击此处',command=liao)
    button3.pack()
    bang.mainloop()

def doc_file():
    word=simpledialog.askstring('我的文档.txt：编辑','请输入您要编辑的内容：')
    if not word:
        return
    else:
        with open('my_doc.txt','a') as file:
            file.write('\n'+word)
            tkmessagebox.showinfo('提示','文件已成功保存！')

def look_file():
    file_gui=Tk()
    file_gui.title('tkvision文本阅读器：我的文档.txt')
    file_gui.geometry('500x500')
    file_gui.iconbitmap("wenben.ico")
    file=open('my_doc.txt')
    s=file.read()
    fileword=label(file_gui,text=s)
    fileword.pack()
    file_gui.mainloop()

def kong_file():
    filekong=open('my_doc.txt', "r+")
    filekong.truncate()
    tkmessagebox.showinfo('提示','文件已成功清空！')

def closer():
    mixer.music.stop()

def nidedaan():
    mixer.init()
    mixer.music.load("你的答案.wav")
    mixer.music.play()
    ww=tkmessagebox.askyesno('播放音乐','正在播放【你的答案】，播放完后会自动退出播放程序,点击否停止播放')
    if ww==True:
        close=1
    else:
        close=0
        mixer.music.stop()

def xiashan():
    mixer.init()
    mixer.music.load("下山.wav")
    mixer.music.play()
    cc=tkmessagebox.askyesno('播放音乐','正在播放【下山】，播放完后会自动退出播放程序,点击否停止播放')
    if cc==True:
        pass
    else:
        mixer.music.stop()

def jingcai():
    huida=['2/8/6','2/6/8','6/2/8','6/8/2','8/6/2','8/2/6']
    def kaishi():
        score=0
        one=simpledialog.askstring('请听题！得分'+str(score),'什么最重要？')
        if one=='wifi':
            tkmessagebox.showinfo('哈哈哈哈！','恭喜你，答对了！我相信，你肯定是网上办公过！')
            score=score=1
        else:
            tkmessagebox.showerror('哈哈哈哈！','hahahha~答错了，没有WiFi你如何下载这个程序？')
            score=score+0
        twotwo=simpledialog.askstring('请听题！得分'+str(score),'孔子是著名的？')
        if twotwo=='老人家':
            tkmessagebox.showinfo('哈哈哈哈！','恭喜你，答对了！甭管什么家，老人家就对了！')
            score=score+1
        else:
            tkmessagebox.showerror('哈哈哈哈！','hahahaha~答错了，甭管什么家，老人家就对了！')
            score=score+0
        three=simpledialog.askstring('请听题！得分'+str(score),'一个人前面看有3根头发，后面看有2根头发，他jiu jing有多少根头发？（有坑）（请回答数字）')
        if three=='0':
            tkmessagebox.showinfo('哈哈哈哈！','恭喜你，答对了！jiujing，都揪浄了，没头发了！')
            score=score+1
        else:
            tkmessagebox.showerror('哈哈哈哈！','hahahaha~答错了，jiujing，都揪浄了，没头发了！')
            score=score+0
        four=simpledialog.askstring('请听题！得分'+str(score),'苹果手机为什么要叫苹果手机？')
        if four=='因为乔布斯喜欢吃苹果':
            tkmessagebox.showinfo('哈哈哈哈！','恭喜你，答对了！乔布斯喜不喜欢吃苹果我不知道，但他们家肯定有喜欢吃苹果的！')
            score=score+1
        else:
            tkmessagebox.showerror('哈哈哈哈！','hahahaha~答错了，乔布斯喜不喜欢吃苹果我不知道，但他们家肯定有喜欢吃苹果的！')
            score=score+0
        five=simpledialog.askstring('卡脖子问题！得分'+str(score),'填空：三个臭皮匠，___________。')
        if four=='臭味都一样':
            tkmessagebox.showinfo('哈哈哈哈！','恭喜你，答对了！他们都是一个皮革厂出来的！')
            score=score+1
        else:
            tkmessagebox.showerror('哈哈哈哈！','hahahaha~答错了，他们都是一个皮革厂出来的！')
            score=score+0
        six=simpledialog.askstring('请听题！得分'+str(score),'一加一等于几？（有多个答案，回答时请以以下方式回答：你好/你好（回答数字））')
        if six in huida:
            tkmessagebox.showinfo('哈哈哈哈！','恭喜你，答对了！不信拿手指头数啊！')
            score=score+1
        else:
            tkmessagebox.showerror('哈哈哈哈！','hahahaha~答错了，不信拿手指头数啊！')
            score=score+0
        tkmessagebox.showinfo('颁奖','答错了？没奖励！答对了？也没奖励！哈哈哈哈哈，没有办法我就是这么强大！')
    jingcai=Tk()
    jingcai.title("有奖竞猜（共计六题，满分6分）")
    jingcai.iconbitmap("game.ico")
    jingcai.geometry("100x100")
    jingcailable=label(jingcai,text='点它开始有奖竞猜↓')
    jingcailable.pack()
    jingcaibutton=Button(jingcai,text='点我~',command=kaishi)
    jingcaibutton.pack()
    jingcai.mainloop()

def gameing():
    ran=random.randrange(15)
    for i in range(6):
        ans=simpledialog.askstring('猜数字游戏','请猜一个1到15的数字：')
        if not ans:
            return
        if ans==ran:
            tkmessagebox.showinfo('猜数字游戏','恭喜你，猜对了！游戏结束！')
            break
        else:
            tkmessagebox.showwarning('猜数字游戏','你猜错了，点击【确定】，再猜一次!')
            continue
    tkmessagebox.showinfo('猜数字游戏','数字是'+str(ran)+',加油！')

def game():
    kaishi=tkmessagebox.askyesno('猜数字游戏','确定要开始游戏吗？')
    if kaishi==True:
        gameing()
    else:
        return

def kuaizhao():
    def next_shape():
        nonlocal shape
        nonlocal previous_color
        nonlocal current_color

        previous_color=current_color
        
        c.delete(shape)
        if len(shapes)>0:
            shape=shapes.pop()
            c.itemconfigure(shape,state=NORMAL)
            current_color=c.itemcget(shape,'fill')
            root.after(1000,next_shape)
        else:
            c.unbind('q')
            c.unbind('p')
            if player1_score>player2_score:
                c.create_text(200,200,text='玩家一赢了！')
            elif player2_score>player1_score:
                c.create_text(200,200,text='玩家二赢了！')
            else:
                c.create_text(200,200,text='平局')
            c.pack()

    def snap(event):
        global shape
        global player1_score
        global player2_score
        vaild=False
        c.delete(shape)
        if previous_color==current_color:
            vaild=True

        if vaild:
            if event.char=='q':
                player1_score=player_score+1
            else:
                player2_score=player2_score+1
            shape=c.create_text(200,200,text='欧欧！增加1分！')
            c.pack()
        else:
            if event.char=='q':
                player1_score=player_score-1
            else:
                player2_score=player2_score-1
            shape=c.create_text(200,200,text='欧欧！减少1分！')
        c.pack()
        kuai.update_idletasks()
        sleep(1)
    
    kuai=Tk()
    kuai.title("快照抓拍小游戏")
    c=Canvas(kuai,width=400,height=400)

    shapes=[]

    circle=c.create_oval(35,20,365,350,outline='black',fill='black',state=HIDDEN)
    shapes.append(circle)
    circle=c.create_oval(35,20,365,350,outline='red',fill='red',state=HIDDEN)
    shapes.append(circle)
    circle=c.create_oval(35,20,365,350,outline='green',fill='green',state=HIDDEN)
    shapes.append(circle)
    circle = c.create_oval(35,20,365,350,outline='blue',fill='blue',state=HIDDEN)
    shapes.append(circle)

    rectangle=c.create_rectangle(35,100,365,270,outline='black',fill='black',state=HIDDEN)
    shapes.append(rectangle)
    rectangle=c.create_rectangle(35,100,365,270,outline='red',fill='red',state=HIDDEN)
    shapes.append(rectangle)
    rectangle= c.create_rectangle(35,100,365,270,outline='green',fill='green',state=HIDDEN)
    shapes.append(rectangle)
    rectangle=c.create_rectangle(35,100,365,270,outline='blue',fill='blue',state=HIDDEN)
    shapes.append(rectangle)

    square=c.create_rectangle(35,20,365,350,outline='black',fill='black',state=HIDDEN)
    shapes.append(square)
    square=c.create_rectangle(35,20,365,350,outline='red',fill='red',state=HIDDEN)
    shapes.append(square)
    square=c.create_rectangle(35,20,365,350,outline='green',fill='green',state=HIDDEN)
    shapes.append(square)
    square= c.create_rectangle(35,20,365,350,outline='blue',fill='blue',state=HIDDEN)
    shapes.append(square)
    c.pack()

    random.shuffle(shapes)

    shape=None

    previous_color=''
    current_color=''
    player1_score=0
    player2_score=0
    
    kuai.after(3000,next_shape)
    c.bind('q',snap)
    c.bind('p',snap)
    c.focus_set()

    kuai.mainloop()


def china():
    webbrowser.open('https://voice.baidu.com/act/newpneumonia/newpneumonia')

def us():
    webbrowser.open('https://voice.baidu.com/act/newpneumonia/newpneumonia?city=%E7%BE%8E%E5%9B%BD-%E7%BE%8E%E5%9B%BD')

def brazil():
    webbrowser.open('https://voice.baidu.com/act/newpneumonia/newpneumonia?city=%E5%B7%B4%E8%A5%BF-%E5%B7%B4%E8%A5%BF')

def india():
    webbrowser.open('https://voice.baidu.com/act/newpneumonia/newpneumonia?city=%E5%8D%B0%E5%BA%A6-%E5%8D%B0%E5%BA%A6')

def looking():
    tkmessagebox.showinfo('版本记录：1.0.0','可以听歌曲\n一个猜数字游戏\n计算器\n可以通过打开网页的方式查看疫情')

def looking2():
    tkmessagebox.showinfo('版本记录1.0.2',
    '修复一些bug\n听歌曲功能更人性化\n可打开项目的github界面\n美观了一些界面\n计算器更人性化\n可检测是否为Python2\n'+
    '搭配一个聊天区（网址https://gitter.im/TkOS10/community）')

def looking3():
    tkmessagebox.showinfo('版本记录1.0.6','新增一些小游戏\n可显示版本记录\n修改了一些计算器的代码，使其更完善')

def this():
    tkmessagebox.showinfo('版本记录2.1.0','保留了TkOS1.0的特色\n新增开始菜单\n对计算器进行优化\n游戏更加完善\n新增tkvision文本阅读器')

mixer.init()
mixer.music.load('MitsubishiModernDoorClose2.wav')
mixer.music.play()

root=Tk()
root.title("TkOS")
root.iconbitmap("tkos.ico")
root.geometry('700x300')
ft = tkFont.Font(family='等线', size=30, weight=tkFont.NORMAL)
thelabel=label(root,text='用Tk,写OS！',font=ft)
thelabel.pack()
label1=label(root,text='TkOS2.0 2.1.0')
label1.pack()

menubar = menu(root)
filemenu = menu(menubar, tearoff=0)
submenu = menu(filemenu)
submenuw = menu(filemenu)

root.config(menu=menubar)
aa = menu(menubar, tearoff=0)
aa.add_separator()
menubar.add_cascade(label='开始', menu=aa)
aa.add_command(label='天气预报', command=tianqi)
aa.add_command(label='查看使用教程', command=jiao)
root.config(menu=menubar)
aa.add_separator()

root.config(menu=menubar)
bb = menu(menubar, tearoff=0)
bb.add_separator()
menubar.add_cascade(label='多功能区', menu=bb)
bb.add_command(label='画板', command=hua)
bb.add_command(label='计算器', command=jisuanqi)
bb.add_cascade(label='文档编辑器', menu=submenu, underline=0)
submenu.add_command(label='编辑文档', command=doc_file)
submenu.add_command(label='查看文档', command=look_file)
submenu.add_command(label='清空文档', command=kong_file)
bb.add_command(label='帮助', command=bang)
root.config(menu=menubar)
bb.add_separator()

filemenu.add_separator()
menubar.add_cascade(label='播放音乐', menu=filemenu)
filemenu.add_command(label='你的答案', command=nidedaan)
filemenu.add_command(label='下山', command=xiashan)
root.config(menu=menubar)

mm = menu(menubar, tearoff=0)
menubar.add_cascade(label='小游戏',menu=mm)
mm.add_command(label='猜数字',command=game)
mm.add_command(label='有奖竞猜小游戏',command=jingcai)
mm.add_command(label='快照抓拍小游戏',command=kuaizhao)

root.config(menu=menubar)
bb = menu(menubar, tearoff=0)
bb.add_separator()
menubar.add_cascade(label='查看疫情', menu=bb)
bb.add_command(label='查看中国疫情', command=china)
bb.add_command(label='查看美国疫情', command=us)
bb.add_command(label='查看巴西疫情', command=brazil)
bb.add_command(label='查看印度疫情', command=india)
root.config(menu=menubar)
bb.add_separator()

cc = menu(menubar, tearoff=0)
menubar.add_cascade(label='查看版本',menu=cc)
cc.add_cascade(label='查看1.0版本', menu=submenuw, underline=0)
submenuw.add_command(label='查看1.0.0更新', command=looking)
submenuw.add_command(label='查看1.0.2更新', command=looking2)
submenuw.add_command(label='查看1.0.6更新', command=looking3)
cc.add_command(label='查看2.0版本', command=this)

menubar.add_command(label='关于',command=about)

b1=Button(root,text='打开项目的github界面',command=github)
b1.pack()
b1l=label(root,text='看看作者的项目')
b1l.pack()
b3=Button(text='关闭所有音乐',command=closer)
b3.pack()
b3l=label(root,text='仅在播放音乐时有效')
b3l.pack()
b2=Button(root,text='进入聊天区\n（和1.0是同一个）',command=liao)
b2.pack()
b2l=label(root,text='发现bug？现在报告！')
b2l.pack()
root.mainloop()