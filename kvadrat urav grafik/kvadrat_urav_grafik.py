from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
global D,t,graf
D=-1
graf=False
t='Нет решений'
def resh():
    global D,t,graf
    if (a.get()!='' and b.get()!='' and c.get()!=''):
        if (float(a.get())==0 and float(b.get())==0 and float(c.get())==0):
            t=0
            rezult.configure(text=f'Тут не должно быть {t}')
            a.configure(bg='lightblue')
            b.configure(bg='lightblue')
            c.configure(bg='lightblue')
            graf=False
        elif float(a.get())==0 and float(b.get())!=0 and float(c.get())!=0:
            b_=float(b.get())
            c_=float(c.get())
            x1_=round((-1*c_)/b_,2)
            t=f'X1={x1_}'
            rezult.configure(text=f'{t}')
            graf=False
        elif float(a.get())!=0:
            a_=float(a.get())
            b_=float(b.get())
            c_=float(c.get())
            D=b_**2-4*a_*c_
            if D>0:
                x1_=round((-1*b_+sqrt(D))/(2*a_),2)
                x2_=round((-1*b_-sqrt(D))/(2*a_),2)
                t=f'X1={x1_}, \nX2={x2_}'
                graf=True
            elif D==0:
                x1_=round((-1*b_)/(2*a_),2)
                t=f'X1={x1_}'
                graf=True
            else:
                t='Нет решений'
                graf=False
            rezult.configure(text=f'D={D}\n{t}')
            a.configure(bg='lightblue')
            b.configure(bg='lightblue')
            c.configure(bg='lightblue')
    else:
        if a.get()=='':
             a.configure(bg='red')
        if b.get()=='':
             b.configure(bg='red')
        if c.get()=='':
             c.configure(bg='red')
    return graf,D,t
def graafik():
    graf,D,t=resh()
    if graf==True:
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x= np.arange(x0-10, x0+10, 0.5)
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x,y,"b:o",x0,y0,"r-d")
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f'Вершина параболлы({x0},{y0})'
    else:
        text=f'График нет возможности построить'
    rezult.configure(text=f'D={D}\n{t}\n{text}')
aken=Tk()
aken.geometry('500x250')
lbl=Label(aken,text='Решение квадратного уравнения',font='Arial 16',fg='green',bg='lightblue',height=1,width=29)
a=Entry(aken,width=3,font='Arial 16',fg='green',bg='lightblue')
lbl1=Label(aken,text='x**2',font='Arial 16',fg='green',height=2,width=5)
b=Entry(aken,width=3,font='Arial 16',fg='green',bg='lightblue')
lbl2=Label(aken,text='x+',font='Arial 16',fg='green',height=2,width=3)
c=Entry(aken,width=3,font='Arial 16',fg='green',bg='lightblue')
lbl3=Label(aken,text='=0',font='Arial 16',fg='green',height=2,width=3)
btm=Button(aken,text='Решить',font='Arial 16',fg='black',bg='green',command=resh)
rezult=Label(aken,text='Решение',font='Arial 16',fg='black',bg='yellow',height=3,width=33)
grafik=Button(aken,text='График',font='Arial 16',fg='black',bg='green',command=graafik)
lbl.pack(side=TOP)
rezult.pack(side=BOTTOM)
a.pack(side=LEFT)
lbl1.pack(side=LEFT)
b.pack(side=LEFT)
lbl2.pack(side=LEFT)
c.pack(side=LEFT)
lbl3.pack(side=LEFT)
btm.pack(side=RIGHT)
grafik.pack(side=RIGHT)
aken.mainloop()