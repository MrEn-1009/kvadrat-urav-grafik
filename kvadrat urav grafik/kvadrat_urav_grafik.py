from tkinter import *
def otv(event):
    pass
aken=Tk()       
aken.geometry('500x250')
lbl=Label(aken,text='Решение квадратного уравнения',font='Arial 16',fg='green',bg='lightblue',height=1,width=29)
uks=Entry(aken,width=3,font='Arial 16',fg='green',bg='lightblue')
lbl1=Label(aken,text='x**2',font='Arial 16',fg='green',height=1,width=4)
kaks=Entry(aken,width=3,font='Arial 16',fg='green',bg='lightblue')
lbl2=Label(aken,text='x+',font='Arial 16',fg='green',height=1,width=2)
kolm=Entry(aken,width=3,font='Arial 16',fg='green',bg='lightblue')
lbl3=Label(aken,text='=0',font='Arial 16',fg='green',height=1,width=2)
btm=Button(aken,text='Решить',font='Arial 16',fg='black',bg='green')
rezult=Label(aken,text='Решение',font='Arial 16',fg='black',bg='yellow',height=1,width=7)
btm.bind('<Button-1>',otv)
lbl.pack(side=TOP)
rezult.pack(side=BOTTOM)
uks.pack(side=LEFT)
lbl1.pack(side=LEFT)
kaks.pack(side=LEFT)
lbl2.pack(side=LEFT)
kolm.pack(side=LEFT)
lbl3.pack(side=LEFT)
btm.pack(side=RIGHT)
aken.mainloop()