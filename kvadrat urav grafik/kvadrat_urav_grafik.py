from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
global D,t,graf,k
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
k=0
def uvel():
    global k
    if k==0:
        aken.geometry(str(aken.winfo_width())+'x'+str(aken.winfo_height()+200))
        okno.config(text='Уменьшить окно')
        k=1
    else:
        aken.geometry(str(aken.winfo_width())+'x'+str(aken.winfo_height()-200))
        okno.config(text='Увеличить окно')
        k=0
def kit():
    x1= np.arange(0, 9.5, 0.5)
    y1=(2/27)*x1**2-3
    x2= np.arange(-10, 0.5, 0.5)
    y2=0.04*x2**2-3
    x3= np.arange(-9, -2.5, 0.5)
    y3=(2/9)*(x3+6)**2+1
    x4= np.arange(-3,9.5,0.5)
    y4= -(1/12)*(x4-3)**2+6
    x5= np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6= np.arange(5,8.5,0.5)
    y6= (1/8)*(x6-7)**2+1.5
    x7= np.arange(-13,-8.5,0.5)
    y7= -0.75*(x7+11)**2+6
    x8= np.arange(-15,-12.5,0.5)
    y8= -0.5*(x8+13)**2+3
    x9= np.arange(-15,-10,0.5)
    y9= [1]*len(x9)
    x10= np.arange(3,4,0.5)
    y10= [3]*len(x10)
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,"r-d")
    plt.title('Кит')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def oshki():
    x1= np.arange(-9, -1, 0.5)
    y1=-(1/16)*(x1+5)**2+2
    x2= np.arange(1, 9, 0.5)
    y2=-(1/16)*(x2-5)**2+2
    x3= np.arange(-9, -1, 0.5)
    y3=(1/4)*(x3+5)**2-3
    x4= np.arange(1,9,0.5)
    y4=(1/4)*(x4-5)**2-3
    x5= np.arange(-9,-6,0.5)
    y5= -(x5+7)**2+5
    x6= np.arange(6,9.5)
    y6= -(x6-7)**2+5
    x7= np.arange(-1,1,0.5)
    y7= -0.5*x7**2+1.5
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,"r-d")
    plt.title('Очки')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def zontik():
    x1= np.arange(-12,12, 0.5)
    y1= -(1/18)*x1**2+12
    x2= np.arange(-4, 4, 0.5)
    y2= -(1/8)*x2**2+6
    x3= np.arange(-12, -4, 0.5)
    y3=-(1/8)*(x3+8)**2+6
    x4= np.arange(4,12,0.5)
    y4= -(1/8)*(x4-8)**2+6
    x5= np.arange(-4,-0.3,0.5)
    y5= 2*(x5+3)**2-9
    x6= np.arange(-4,0.2,0.5)
    y6= 1.5*(x6+3)**2-10
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,"r-d")
    plt.title('Зонтик')
    plt.ylabel('y')
    plt.xlabel('x') 
    plt.grid(True)
    plt.show()
def baba():
    x1= np.arange(-9, 1, 0.5)
    y1=-(1/8)*(x1+9)**2+8
    x2= np.arange(1,9, 0.5)
    y2=-(1/8)*(x2-9)**2+8
    x3= np.arange(-9, -8, 0.5)
    y3=7*(x3+8)**2+1
    x4= np.arange(8,9,0.5)
    y4= 7*(x4-8)**2+1
    x5= np.arange(-8,-1,0.5)
    y5=(1/49)*(x5+1)**2
    x6= np.arange(1,8,0.5)
    y6= (1/49)*(x6-1)**2

    x7= np.arange(-8, -1, 0.5)
    y7=-(4/49)*(x7+1)**2
    x8= np.arange(1,8, 0.5)
    y8=-(4/49)*(x8-1)**2
    x9= np.arange(-8, -2, 0.5)
    y9=(1/3)*(x9+5)**2-7
    x10= np.arange(2,8,0.5)
    y10= (1/3)*(x10-5)**2-7
    x11= np.arange(-2,-1,0.5)
    y11=-2*(x11+1)**2-2
    x12= np.arange(1,2,0.5)
    y12= -2*(x12-1)**2-2
    x13= np.arange(-1, 1, 0.5)
    y13= -4*x13**2+2
    x14=np.arange(-1,1,0.5)
    y14= 4*x14**2-6
    x15= np.arange(-2,0,0.5)
    y15= -1.5*x15+2
    x16= np.arange(0,2,0.5)
    y16= 1.5*x16+2
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16,"r-d")
    plt.title('Бабочка')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
aken=Tk()
aken.geometry('500x200')
aken.title('Квадратные уравнения')
f1=Frame(aken,width=500,height=200)
f1.pack(side=TOP)
f2=Frame(aken,width=500,height=200)
f2.pack(side=BOTTOM)
lbl=Label(f1,text='Решение квадратного уравнения',font='Arial 16',fg='green',bg='lightblue',height=1,width=29)
a=Entry(f1,width=3,font='Arial 16',fg='green',bg='lightblue')
lbl1=Label(f1,text='x**2',font='Arial 16',fg='green',height=2,width=5)
b=Entry(f1,width=3,font='Arial 16',fg='green',bg='lightblue')
lbl2=Label(f1,text='x+',font='Arial 16',fg='green',height=2,width=3)
c=Entry(f1,width=3,font='Arial 16',fg='green',bg='lightblue')
lbl3=Label(f1,text='=0',font='Arial 16',fg='green',height=2,width=3)
btm=Button(f1,text='Решить',font='Arial 16',fg='black',bg='green',command=resh)
rezult=Label(f1,text='Решение',font='Arial 16',fg='black',bg='yellow',height=3,width=33)
grafik=Button(f1,text='График',font='Arial 16',fg='black',bg='green',command=graafik)
okno=Button(f1,text='Увеличить окно',font='Arial 16',fg='black',bg='green',command=uvel)
var=StringVar()
var.set('Один')
r1=Radiobutton(f2,text='Кит',variable=var,value='Один',command=kit)
r2=Radiobutton(f2,text='Очки',variable=var,value='Два',command=oshki)
r3=Radiobutton(f2,text='Зонтик',variable=var,value='Три',command=zontik)
r4=Radiobutton(f2,text='Бабочка',variable=var,value='Четыре',command=baba)
r5=Radiobutton(f2,text='Лягушка',variable=var,value='Пять')
lbl.pack(side=TOP)
okno.pack(side=BOTTOM)
rezult.pack(side=BOTTOM)
a.pack(side=LEFT)
lbl1.pack(side=LEFT)
b.pack(side=LEFT)
lbl2.pack(side=LEFT)
c.pack(side=LEFT)
lbl3.pack(side=LEFT)
btm.pack(side=RIGHT)
grafik.pack(side=RIGHT)
r1.pack(side=BOTTOM)
r2.pack(side=BOTTOM)
r3.pack(side=BOTTOM)
r4.pack(side=BOTTOM)
r5.pack(side=BOTTOM)
aken.mainloop()