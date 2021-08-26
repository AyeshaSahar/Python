from tkinter import *
 
def MainFunc(source, side):
    Obj = Frame(source, borderwidth=4, bd=4, bg="purple")
    Obj.pack(side=side, expand =YES, fill =BOTH)
    return Obj
 
def button(source, side, text, command=None):
    Obj = Button(source, text=text, command=command)
    Obj.pack(side=side, expand = YES, fill=BOTH)
    return Obj
 
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 24 bold')
        self.pack(expand = YES, fill =BOTH)
        self.master.title('Calculator')
 
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
          justify='right'
          , bd=30, bg="powder blue").pack(side=TOP,
                                          expand=YES, fill=BOTH)
 
        for clearButton in (["C"]):
            erase = MainFunc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    Obj=display, q=ichar: Obj.set(''))
 
        for numButton in ("789/", "456*", "123-", "0.+"):
         FunctionNum = MainFunc(self, TOP)
         for iEquals in numButton:
            button(FunctionNum, LEFT, iEquals, lambda
                Obj=display, q=iEquals: Obj
                   .set(Obj.get() + q))
 
        EqualButton = MainFunc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self,
                                Obj=display: s.calc(Obj), '+')
 
 
            else:
                btniEquals = button(EqualButton, LEFT, iEquals,
                                    lambda Obj=display, s=' %s ' % iEquals: Obj.set
                                    (Obj.get() + s))
 
    def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")
 
 
if __name__=='__main__':
 app().mainloop()