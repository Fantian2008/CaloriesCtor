from tkinter import *

root = Tk()
root.title("卡路里计算器")

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

class Kcalmath:
    def __init__(self,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11):
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

    def mi(self):

        n = ""
        e = 0.0
        f = 0.0
        n = u.get()
        e = float(m.get())
        f = float(d.get())
        
        if n == "仰卧起坐":
            self.b1 = f*10*e
            g.set(self.b1)
            
        if n == "散步":
            self.b2 = f*4.5*e
            g.set(self.b2)
            
        if n == "跳绳":
            self.b3 = f*12*e
            g.set(self.b3)
            
        if n == "慢跑":
            self.b4 = f*8.9*e
            g.set(self.b4)
            
        if n == "骑单车":
            self.b5 = f*13.27*e
            g.set(self.b5)
            
        if n == "篮球":
            self.b6 = f*6.57*e
            g.set(self.b6)
            
        if n == "排球":
            self.b7 = f*8.27*e
            g.set(self.b7)
            
        if n == "快跑":
            self.b8 = f*10.2*e
            g.set(self.b8)
            
        if n == "引体向上":
            self.b9 = f*0.83*e
            g.set(self.b9)
            
        if n == "网球":
            self.b10 = f*6.33*e
            g.set(self.b10)
            
        if n == "蛙泳":
            self.b11 = self.f*4.5*self.e
            g.set(self.b11)


    def delall(self):
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

    def sumall(self):
        
        ofall = self.b1+self.b2+self.b3+self.b4+self.b5+self.b6+self.b7+self.b8+self.b9+self.b10+self.b11
        t.set(ofall)

    def winquit(self):
        root.destroy()
        

u = StringVar()
m = StringVar()
d = StringVar()
g = StringVar()
t = StringVar()

kcalm =Kcalmath(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11)



frame = Frame(root)
frame.pack(padx=8, pady=8, ipadx=4)

lab1 = Label(frame,font=('微软雅黑',11), text="运动方式/类型:")
lab1.grid(row=1, column=0, padx=5, pady=5, sticky=W)

lab2 = Label(frame,font=('微软雅黑',10), text="可计算卡路里的运动方式有:\n散步(小时h)、跳绳(小时h)、慢跑(小时h)、快跑(小时h)、\n仰卧起坐(下)、骑单车(小时h)、篮球(小时h)、排球(小时h)、\n网球(小时h)、蛙泳(小时h)、引体向上(个)。")
lab2.grid(row=0, column=0, padx=5, pady=5, sticky=W)

lab3 = Label(frame, font=('微软雅黑',11),text="你的体重(千克kg):")
lab3.grid(row=2, column=0, padx=5, pady=5, sticky=W)

lab3 = Label(frame, font=('微软雅黑',11),text="你运动的量:")
lab3.grid(row=3, column=0, padx=5, pady=5, sticky=W)

lab4 = Label(frame,font=('微软雅黑',11), text="你运动消耗的能量(卡路里cal):")
lab4.grid(row=4, column=0, padx=5, pady=5, sticky=W)

lab5 = Label(frame,font=('微软雅黑',11), text="你今日总共消耗的能量(卡路里cal):")
lab5.grid(row=5, column=0, padx=5, pady=5, sticky=W)

lab6 = Label(frame,font=('微软雅黑',8), text="注:运动总量求和功能中,每项运动消耗的能量只能保存最近一次所计算的结果!")
lab6.grid(row=6, column=0, padx=5, pady=5, sticky=W)

lab7 = Label(frame, font=('微软雅黑',6),text="Version 1.2a - 10 . 25 . 2022Copyright (C) 2022 -2032  丁子麟(Zilin Ding)  email: DZL20081110@163.com  QQ:2302368576")
lab7.grid(row=9, padx=5, pady=5, sticky=W)

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


button1 = Button(frame, text="计算", command=kcalm.mi, default='active')
button1.grid(row=7, column=0)

button2 = Button(frame, text="求和", command=kcalm.sumall, default='active')
button2.grid(row=7, column=1)

button3 = Button(frame, text="归零", command=kcalm.delall, default='active')
button3.grid(row=8, column=0)

button4 = Button(frame, text="退出", command=kcalm.winquit, default='active')
button4.grid(row=8, column=1)

root.update_idletasks()

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))

root.mainloop()
