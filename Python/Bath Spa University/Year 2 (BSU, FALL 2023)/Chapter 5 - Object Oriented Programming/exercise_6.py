import tkinter as tk
from tkinter import ttk
import re

# Default settings
TITLE='Arithmetic Operation'

GEOMETRY='400x400'

FONT=('Tahoma',12)
BG_COLOR='lightgoldenrod1'
TEXT_COLOR='cornflowerblue'
class App(tk.Tk):

    class ArithmeticOperations:
        def __init__(self,parent,**kwargs):
            self.param1=kwargs.get('param1', 0)
            self.param2=kwargs.get('param2', 0)
            
            self.parent=parent

            if re.match(r'^\d+$',self.param1+self.param2):
                self.Calculate()

        def Calculate(self)->None:
            self.mode=self.parent.selected_opt.get()
            self.operation_signs=('+','-','*','/')
            
            self.selected_operation=self.parent.operations.index(self.mode)

            result=eval(self.param1 +self.operation_signs[self.selected_operation]+ self.param2)

            self.parent.label_w2.configure(text=result)

    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(GEOMETRY)

        self['bg']=BG_COLOR
        
        self.font=FONT
        self.w_preset={'font':self.font,'bg':self['bg'],'fg':TEXT_COLOR}

        #widgets
        self.label_w=tk.Label(self,**self.w_preset,text='Select Operation')
        self.label_w.place(relx=.5,rely=.1,anchor=tk.CENTER)

        self.selected_opt=tk.StringVar()
        self.operations=('Addition','Subtraction','Multiplication','Division')
        self.options_w=ttk.Combobox(self,font=self.font,values=self.operations,textvariable=self.selected_opt)
        self.options_w.place(relx=.5,rely=.2,anchor=tk.CENTER)

        self.param_one=tk.StringVar()
        self.param_two=tk.StringVar()
        
        self.entry_w_one=tk.Entry(self,font=self.font,textvariable=self.param_one)
        self.entry_w_one.place(relx=.2,rely=.3,anchor=tk.CENTER,relwidth=.25)

        self.entry_w_two=tk.Entry(self,font=self.font,textvariable=self.param_two)
        self.entry_w_two.place(relx=.8,rely=.3,anchor=tk.CENTER,relwidth=.25)

        self.button_w=tk.Button(self,**self.w_preset,command=self.operation,text='Calculate')
        self.button_w.place(relx=.5,rely=.5,anchor=tk.CENTER)

        self.label_w2=tk.Label(self,**self.w_preset,text='Result will be displayed here')
        self.label_w2.place(relx=.5,rely=.6,anchor=tk.CENTER)
        
    def operation(self)->None:
        self.ArithmeticOperations(parent=self,param1=self.param_one.get(),param2=self.param_two.get())

def main()->None:
    App().mainloop()

if __name__ == "__main__":
	main()