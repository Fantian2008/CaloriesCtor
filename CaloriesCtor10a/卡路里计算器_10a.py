from tkinter import *
root = Tk()
root.title("卡路里计算器")
n = ""
e = 0.0
f = 0.0
g = 0.0
def mi():
    n = u.get()
    e = float(m.get())
    f = float(d.get())
    if n == "仰卧起坐":
        b = f*10*e
    if n == "散步":
        b = f*4.5*e
    if n == "跳绳":
        b = f*12*e
    if n == "慢跑":
        b = f*8.9*e
    if n == "骑单车":
        b = f*13.27*e
    if n == "篮球":
        b = f*6.57*e
    if n == "排球":
        b = f*8.27*e
    if n == "快跑":
        b = f*10.2*e
    if n == "引体向上":
        b = f*0.83*e
    if n == "网球":
        b = f*6.33*e
    if n == "蛙泳":
        b = f*4.5*e
    g.set(b)
frame = Frame(root)
frame.pack(padx=8, pady=8, ipadx=4)

lab1 = Label(frame, text="运动热量计算:")
lab1.grid(row=1, column=0, padx=5, pady=5, sticky=W)

lab2 = Label(frame, text="可计算卡路里的运动方式有:\n散步(小时h)、跳绳(小时h)、慢跑(小时h)、快跑(小时h)、\n仰卧起坐(下)、骑单车(小时h)、篮球(小时h)、排球(小时h)、\n网球(小时h)、蛙泳(小时h)、引体向上(个)。")
lab2.grid(row=0, column=0, padx=5, pady=5, sticky=W)

lab3 = Label(frame, text="你的体重(千克kg):")
lab3.grid(row=2, column=0, padx=5, pady=5, sticky=W)

lab3 = Label(frame, text="你运动的量:")
lab3.grid(row=3, column=0, padx=5, pady=5, sticky=W)

lab4 = Label(frame, text="你消耗的能量(卡路里cal):")
lab4.grid(row=4, column=0, padx=5, pady=5, sticky=W)

lab5 = Label(frame, text="Version 1.0a - 10 . 20 . 2022\nCopyright (C) 2022 -2032  丁子麟(Zilin Ding)\nemail: DZL20081110@163.com\nQQ:2302368576")
lab5.grid(row=5, column=0, padx=5, pady=5, sticky=W)

u = StringVar()
m = StringVar()
d = StringVar()
g = StringVar()

ent1 = Entry(frame, textvariable=u)
ent1.grid(row=1, column=1, sticky='ew', columnspan=2)

ent2 = Entry(frame, textvariable=m)
ent2.grid(row=2, column=1, sticky='ew', columnspan=2)

ent3 = Entry(frame, textvariable=d)
ent3.grid(row=3, column=1, sticky='ew', columnspan=2)

ent4 = Entry(frame,textvariable=g)
ent4.grid(row=4, column=1, sticky='ew', columnspan=2)


button = Button(frame, text="计算", command=mi, default='active')
button.grid(row=6, column=1)

root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.mainloop()
