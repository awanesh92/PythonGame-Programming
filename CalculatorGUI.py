from tkinter import *

class Calc:
    def __init__(self,mast):
        self.mast=mast
        mast.title("Calculator")

        self.total=0
        self.input_num=0
        self.total_txt=IntVar()
        self.total_txt.set(self.total)
        self.total_label=Label(mast,textvariable=self.total_txt)

        self.label =Label(mast,text='Total: ')

        vcmd=mast.register(self.validate)
        self.entry=Entry(mast,validate='key',validatecommand=(vcmd,'%P'))

        self.add_button = Button(mast,text='+',command=lambda : self.update('add'))
        self.sub_button = Button(mast,text='-',command=lambda : self.update('sub'))
        self.reset_button = Button(mast,text='Reset',command=lambda : self.update('reset'))

        self.label.grid(row=0,column=0,sticky=W)
        self.total_label.grid(row=0,column=1,columnspan=2,sticky=E)

        self.entry.grid(row=1,column=0,columnspan=3,sticky=W+E)

        self.add_button.grid(row=2,column=0)
        self.sub_button.grid(row=2,column=1)
        self.reset_button.grid(row=3,column=2,sticky=W+E)

    def validate(self,nt):
        if not nt:
            self.input_num=0
            return True

        try:
            self.input_num=int(nt)
            return True
        except ValueError:
            return False

    def update(self,mthdname):
        if mthdname=='add':
            self.total+=self.input_num
        elif mthdname='sub':
            self.total-=self.input_num
        else:
            self.total=0

        self.total_txt.set(self.total)
        self.entry.delete(0,END)

r=Tk()
mg=Calc(r)
r.mainloop()
