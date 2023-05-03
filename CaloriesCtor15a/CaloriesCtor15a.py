#Version 1.5a - 10 . 30 . 2022
#
#Copyright (C) 2022 -2032  Zilin Ding
#email: DZL20081110@163.com
#QQ:2302368576
from tkinter import *
import tkinter.messagebox as tm
import time as ti

root = Tk()
root.title("卡路里计算器 Version 1.5a")

b1=0.0
b2=0.0
b3=0.0
b4=0.0
b5=0.0
b6=0.0
b7=0.0
b8=0.0
b9=0.0
b10=0.0
b11=0.0
count=0

class Kcalmath:
    def __init__(self,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,count):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
        self.b10 = b10
        self.b11 = b11
        self.count = int(count)

    def mi(self):

        n = ""
        e = 0.0
        f = 0.0
        n = u.get()
        k=m.get()
        kl=d.get()

        if n !=""and k !=''and kl!='':
        
            e = float(k)
            f = float(kl)
            
            if n == "仰卧起坐":
                self.b1 = f*10*e
                g.set(self.b1)
                tm.showinfo('提示','你进行[%s]运动消耗了<%f>卡路里'%(n,self.b1))
                
            if n == "散步":
                self.b2 = f*4.5*e
                g.set(self.b2)
                tm.showinfo('提示','你进行[%s]运动消耗了<%f>卡路里'%(n,self.b2))
                
            if n == "跳绳":
                self.b3 = f*12*e
                g.set(self.b3)
                tm.showinfo('提示','你进行[%s]运动消耗了<%f>卡路里'%(n,self.b3))
                
            if n == "慢跑":
                self.b4 = f*8.9*e
                g.set(self.b4)
                tm.showinfo('提示','你进行[%s]运动消耗了<%f>卡路里'%(n,self.b4))
                
            if n == "骑单车":
                self.b5 = f*13.27*e
                g.set(self.b5)
                tm.showinfo('提示','你进行[%s]运动消耗了<%f>卡路里'%(n,self.b5))
                
            if n == "篮球":
                self.b6 = f*6.57*e
                g.set(self.b6)
                tm.showinfo('提示','你进行[%s]运动消耗了<%f>卡路里'%(n,self.b6))
                
            if n == "排球":
                self.b7 = f*8.27*e
                g.set(self.b7)
                tm.showinfo('提示','你进行[%s]运动消耗了<%f>卡路里'%(n,self.b7))
                
            if n == "快跑":
                self.b8 = f*10.2*e
                g.set(self.b8)
                tm.showinfo('提示','你进行[%s]运动消耗了<%f>卡路里'%(n,self.b8))
                
            if n == "引体向上":
                self.b9 = f*0.83*e
                g.set(self.b9)
                tm.showinfo('提示','你进行[%s]运动消耗了<%f>卡路里'%(n,self.b9))
                
            if n == "网球":
                self.b10 = f*6.33*e
                g.set(self.b10)
                tm.showinfo('提示','你进行[%s]运动消耗了<%f>卡路里'%(n,self.b10))
                
            if n == "蛙泳":
                self.b11 = f*4.5*e
                g.set(self.b11)
                tm.showinfo('提示','你进行[%s]运动消耗了<%f>卡路里'%(n,self.b11))
        else:
            tm.showwarning('提示','请正确输入')

            

    def delall(self):
        info=tm.askquestion('提示','是否要清除缓存数据?')
        if info == 'yes':
            self.b1=0.0
            self.b2=0.0
            self.b3=0.0
            self.b4=0.0
            self.b5=0.0
            self.b6=0.0
            self.b7=0.0
            self.b8=0.0
            self.b9=0.0
            self.b10=0.0
            self.b11=0.0
            self.count=0
            tm.showinfo('提示','缓存数据已清除!')
        else:
            pass

    def sumall(self):
        info=tm.askquestion('提示','是否要计算所有运动消耗的总热量?')
        if info == 'yes':
            ofall = self.b1+self.b2+self.b3+self.b4+self.b5+self.b6+self.b7+self.b8+self.b9+self.b10+self.b11
            t.set(ofall)
            tm.showinfo('提示','你所有运动消耗的总热量为<%f>'%ofall)
        else:
            pass

    def winquit(self):
        
        info=tm.askquestion('提示','你确定要退出吗?')
        if info=='yes':
            root.destroy()
        else:
            pass

    def saveas(self):
        
        name = ''

        num = 0.0
        
        name = str(u.get())

        nu = g.get()

        txt = ''
        txt = ti.strftime('%Y年%m月%d日 %H:%M',ti.localtime(ti.time()))

        lines=[]

        if nu != '':

            num = float(nu)

            if name != ''and num != None:

                info=tm.askquestion('提示','是否要保存运动日志?')

                if info == 'yes':
                    
                    f=open("data/sportsdata.txt",'r')
                    for line in f:
                        lines.append(line)
                    f.close()
                    lsen=len(lines)
                    lines.insert(lsen,"%s--运动记录:运动项目[%s]:消耗的热量为<%f>卡路里\n"%(txt,name,num))
                    s=''.join(lines)
                    f=open("data/sportsdata.txt",'w+')
                    f.write(s)
                    f.close()
                    del lines[:]
                    tm.showinfo('提示','保存成功\n你于%s保存的运动日志的日志号为%d'%(txt,lsen+1))
                else:
                    pass
            else:
                tm.showwarning('提示','请正确输入')
        else:
            tm.showwarning('提示','输入不能为空')
        
        
    def savedel(self):
        
        lines=[]
        
        f=open("data/sportsdata.txt",'r')
        for line in f:
            lines.append(line)
        f.close()
        lsen=len(lines)-1
        info=tm.askquestion('提示','是否要清除上条运动日志?')
        if info == 'yes':
            if lines != []:
                del lines[lsen]
                s=''.join(lines)
                f=open("data/sportsdata.txt",'w+')
                f.write(s)
                f.close()
                del lines[:]
                tm.showinfo('提示','已成功清除上条运动日志')
            else:
                tm.showwarning('提示','日志为空')
        else:
            del lines[:]
            pass
        
    def finddata(self):
        lines=[]
        f=open("data/sportsdata.txt",'r')
        for line in f:
            lines.append(line)
        f.close()
        qw = sd.get()
        if qw != '':
            info=tm.askquestion('提示','是否要查找日志?(日志号为[%s])'%qw)
            if info == 'yes':
                if lines != []:
                    flen = int(sd.get())-1
                    sf.set(lines[flen])
                    tm.showinfo('提示','已打开日志')
                else:
                    tm.showwarning('提示','日志为空')
            else:
                pass
        else:
            tm.showwarning('注意','输入不能为空')
        
    def delfinddata(self):
        lines=[]
        f=open("data/sportsdata.txt",'r')
        for line in f:
            lines.append(line)
        f.close()
        qw = sd.get()
        if qw != '':
            info=tm.askquestion('提示','是否要删除日志?(日志号为[%s])'%qw)
            if info == 'yes':
                if lines != []:
                    dllen = int(sd.get())-1
                    if dllen>=len(lines):
                        tm.showwarning('注意','没有此日志')
                    else:
                        del lines[dllen]
                        s=''.join(lines)
                        f=open("data/sportsdata.txt",'w+')
                        f.write(s)
                        f.close()
                        del lines[:]
                        tm.showinfo('提示','已删除日志(日志号为[%s])'%qw)
                else:
                    tm.showwarning('注意','日志为空')
            else:
                pass
        else:
            tm.showwarning('注意','输入不能为空')

    def opendata(self):
        lines=[]
        f=open("data/sportsdata.txt",'r')
        for line in f:
            lines.append(line)
        f.close()
        qw=len(lines)-self.count
        info=tm.askquestion('提示','是否打开上条日志?(日志号为[%d])'%qw)
        if info == 'yes':
            if lines != []: 
                dlen = len(lines)-1-self.count
                sf.set(lines[dlen])
                self.count += 1
                tm.showinfo('提示','已打开日志(日志号为[%d])'%qw)
            else:
                tm.showwarning('提示','日志为空')
        else:
            pass

    def delalldata(self):
        info=tm.askquestion('提示','是否要清除所有运动日志?')
        if info == 'yes':
            f=open("data/sportsdata.txt",'w')
            f.write("")
            tm.showinfo('提示','已清除所有日志')
        else:
            pass
        
    def winupdate(self):
        info=tm.askquestion('提示','是否要刷新窗口?')
        if info == 'yes':
            mn=""
            u.set(mn)
            m.set(mn)
            d.set(mn)
            g.set(mn)
            t.set(mn)
            sd.set(mn)
            sf.set(mn)
            self.count=0
            tm.showinfo('提示','窗口已刷新')
        else:
            pass

u = StringVar()
m = StringVar()
d = StringVar()
g = StringVar()
t = StringVar()
sd = StringVar()
sf = StringVar()

kcalm =Kcalmath(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,count)



frame = Frame(root)
frame.pack(padx=8, pady=8, ipadx=4)

lab1 = Label(frame,font=('微软雅黑',11), text="运动方式/类型:")
lab1.grid(row=1, column=0, padx=5, pady=5, sticky=W)

lab2 = Label(frame,font=('微软雅黑',10), text="可计算卡路里的运动方式有:\n散步(小时h)、跳绳(小时h)、慢跑(小时h)、快跑(小时h)、\n仰卧起坐(下)、骑单车(小时h)、篮球(小时h)、排球(小时h)、\n网球(小时h)、蛙泳(小时h)、引体向上(个)。")
lab2.grid(row=0, column=0, padx=5, pady=5, sticky=W)

lab3 = Label(frame, font=('微软雅黑',11),text="你的体重(千克kg):")
lab3.grid(row=2, column=0, padx=5, pady=5, sticky=W)

lab10 = Label(frame, font=('微软雅黑',11),text="你运动的量:")
lab10.grid(row=3, column=0, padx=5, pady=5, sticky=W)

lab4 = Label(frame,font=('微软雅黑',11), text="你运动消耗的能量(卡路里cal):")
lab4.grid(row=4, column=0, padx=5, pady=5, sticky=W)

lab5 = Label(frame,font=('微软雅黑',11), text="你今日总共消耗的能量(卡路里cal):")
lab5.grid(row=5, column=0, padx=5, pady=5, sticky=W)

lab6 = Label(frame,font=('微软雅黑',11), text="搜索运动日志(日志号):")
lab6.grid(row=6, column=0, padx=5, pady=5, sticky=W)

lab9 = Label(frame,font=('微软雅黑',11), text="运动日志内容:")
lab9.grid(row=7, column=0, padx=5, pady=5, sticky=W)

lab7 = Label(frame,font=('微软雅黑',8), text="注:1.运动总量求和功能中,每项运动消耗的能量只能保存最近一次所计算的结果!\n2.日志号为日志的序号,从第一次记录为1开始。\n3.运动日志的路径为:data\sportsdata.txt。\n4.请注意输入内容和输入位置,以免无法计算。\n5.删除指定日志后,该日志往后的所有日志的日志号会被更改(日志号-1)。")
lab7.grid(row=9, column=0, padx=5, pady=5, sticky=W)

lab8 = Label(frame, font=('微软雅黑',6),text="Version 1.5a - 10 . 30 . 2022 Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
lab8.grid(row=10, padx=5, pady=5, sticky=W)

ent1 = Entry(frame, textvariable=u)
ent1.grid(row=1, column=1, sticky='ew', columnspan=2)

ent2 = Entry(frame, textvariable=m)
ent2.grid(row=2, column=1, sticky='ew', columnspan=2)

ent3 = Entry(frame, textvariable=d)
ent3.grid(row=3, column=1, sticky='ew', columnspan=2)

ent4 = Entry(frame,textvariable=g)
ent4.grid(row=4, column=1, sticky='ew', columnspan=2)

ent5 = Entry(frame,textvariable=t)
ent5.grid(row=5, column=1, sticky='ew', columnspan=2)

ent6 = Entry(frame,textvariable=sd)
ent6.grid(row=6, column=1, sticky='ew', columnspan=2)

ent7 = Entry(frame,textvariable=sf)
ent7.grid(row=7, column=1, sticky='ew', columnspan=2)


button1 = Button(frame, text="运动热量计算", command=kcalm.mi, default='active')
button1.grid(row=1, column=3,padx=5)

button2 = Button(frame, text="运动热量求和", command=kcalm.sumall, default='active')
button2.grid(row=2, column=3,padx=5)

button3 = Button(frame, text="缓存数据清空", command=kcalm.delall, default='active')
button3.grid(row=3, column=3,padx=5)

button4 = Button(frame, text="退出", command=kcalm.winquit, default='active')
button4.grid(row=9, column=1,pady=5,columnspan=2)

button5 = Button(frame, text="保存运动日志", command=kcalm.saveas, default='active')
button5.grid(row=4, column=3,padx=5)

button6 = Button(frame, text="删除上条日志", command=kcalm.savedel, default='active')
button6.grid(row=7, column=3,padx=5)

button7 = Button(frame, text="打开指定日志", command=kcalm.finddata, default='active')
button7.grid(row=6, column=3,padx=5)

button10 = Button(frame, text="删除指定日志", command=kcalm.delfinddata, default='active')
button10.grid(row=5, column=3,padx=5)

button8 = Button(frame, text="打开上条日志", command=kcalm.opendata, default='active')
button8.grid(row=8, column=3,padx=5,pady=3)

button11 = Button(frame, text="清空运动日志", command=kcalm.delalldata, default='active')
button11.grid(row=9, column=3,padx=5)

button9 = Button(frame, text="刷新窗口", command=kcalm.winupdate, default='active')
button9.grid(row=8, column=1,padx=5,columnspan=2)

root.update_idletasks()

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))

root.mainloop()
