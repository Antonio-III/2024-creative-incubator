import tkinter as tk
# Defeault settings
TITLE='Employee Class'
GEOMETRY='500x500'
BG_COLOR='lightgoldenrod1'
FONT=('Tahoma',16)
TEXT_COLOR=('Tahoma',16)

EMPLOYEE_1={'name':'Antonio','position':'CEO','salary':12000,'eid':1}
EMPLOYEE_2={'name':'Miguel','position':'Manager','salary':1000,'eid':2}
EMPLOYEE_3={'name':'Jo','position':'Senior Dev','salary':2000,'eid':3}
EMPLOYEE_4={'name':'Intal','position':'Junior Dev','salary':300,'eid':4}
EMPLOYEE_5={'name':'III','position':'Intern','salary':100,'eid':5}

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title(TITLE)
        self.geometry(GEOMETRY)

        self['bg']=BG_COLOR
        self.font=FONT
        self.w_preset={'font':self.font,'bg':self['bg'],'fg':TEXT_COLOR}
        self.e_p_preset={'rely':.8,'relwidth':.2}

        self.e_ind=tk.IntVar()
        self.e_nam=tk.StringVar()
        self.e_pos=tk.StringVar()
        self.e_sal=tk.StringVar()
        self.e_id=tk.StringVar()
        
        self.employee_1=self.Employee(**EMPLOYEE_1)
        self.employee_2=self.Employee(**EMPLOYEE_2)
        self.employee_3=self.Employee(**EMPLOYEE_3)
        self.employee_4=self.Employee(**EMPLOYEE_4)
        self.employee_5=self.Employee(**EMPLOYEE_5)
        
        # employee l
        self.employee_list=[self.employee_1,self.employee_2,self.employee_3,self.employee_4,self.employee_5]
        
        # widget l
        self.widget_list=[]

        self.outputStart()
        
        
        # widgets

        self.label_1=tk.Label(self,**self.w_preset,text='Name')
        self.label_1.place(x=0)

        self.label_2=tk.Label(self,**self.w_preset,text='Position')
        self.label_2.place(relx=.25)

        self.label_3=tk.Label(self,**self.w_preset,text='Salary')
        self.label_3.place(relx=.5)

        self.label_4=tk.Label(self,**self.w_preset,text='ID')
        self.label_4.place(relx=.75)

        self.label_5=tk.Label(self,**self.w_preset,text='Index')
        self.label_5.place(relx=.5,rely=.6,anchor='n')

        self.entry_1=tk.Entry(self,font=self.font,textvariable=self.e_ind)
        self.entry_1.place(relx=.5,rely=.7,anchor='n',relwidth=.2)
        
        self.entry_2=tk.Entry(self,font=self.font,textvariable=self.e_nam)
        self.entry_2.place(**self.e_p_preset) # type: ignore
    
        self.entry_3=tk.Entry(self,font=self.font,textvariable=self.e_pos)
        self.entry_3.place(**self.e_p_preset,relx=.25) # type: ignore

        self.entry_4=tk.Entry(self,font=self.font,textvariable=self.e_sal)
        self.entry_4.place(**self.e_p_preset,relx=.5) # type: ignore

        self.entry_5=tk.Entry(self,font=self.font,textvariable=self.e_id)
        self.entry_5.place(**self.e_p_preset,relx=.75) # type: ignore
        
        self.button_1=tk.Button(self,**self.w_preset,text='Set Data',command=self.setData)
        self.button_1.place(relx=.3,rely=.9,anchor='n')

        self.button_2=tk.Button(self,**self.w_preset,text='Print Data',command=self.getData)
        self.button_2.place(relx=.6,rely=.9,anchor='n')

    class Employee():
        def __init__(self,name,position,salary,eid):
            self.name=name
            self.position=position
            self.salary=salary
            self.id=eid
    def outputStart(self) -> None:
        self.incy=.1
        for classes in self.employee_list:
            self.incx=.25
            
            self.display_name=tk.Label(self,**self.w_preset,text=classes.name)
            self.display_name.place(rely=self.incy)

            self.display_position=tk.Label(self,**self.w_preset,text=classes.position)
            self.display_position.place(relx=self.incx,rely=self.incy)

            self.display_salary=tk.Label(self,**self.w_preset,text=classes.salary)
            self.display_salary.place(relx=self.incx+.25,rely=self.incy)

            self.display_id=tk.Label(self,**self.w_preset,text=classes.id)
            self.display_id.place(relx=self.incx+.5,rely=self.incy)
            
            self.incy+=.1
            
            self.widget_list.append(self.display_name)
            self.widget_list.append(self.display_position)
            self.widget_list.append(self.display_salary)
            self.widget_list.append(self.display_id)
            
    def setData(self) -> None:   
        self.index=self.e_ind.get()
        self.name=self.e_nam.get()
        self.position=self.e_pos.get()
        self.salary=self.e_sal.get()
        self.id=self.e_id.get()
        
        if len(self.widget_list)>0:
            for i in self.widget_list:
                i.destroy()
        
            # remove all elements after destroying widgets
            self.widget_list.clear()

        if self.index in range(len(self.employee_list)):
            self.outputEmployees()
                            
    def outputEmployees(self) -> None:
        self.employee_list[self.index].name=self.name
        self.employee_list[self.index].position=self.position
        self.employee_list[self.index].salary=self.salary
        self.employee_list[self.index].id=self.id

        self.incy=.1
        for classes in self.employee_list:
            self.checker={}
            for attr_k,attr_v in vars(classes).items():
                if attr_v=='':
                    # correction gets added to checker
                    self.checker[attr_k]='null'
                    
            # checker updates the current iteration's dictionary
            classes.__dict__.update(self.checker)
                
            
            self.incx=.25
            
            # output the attributes of the classes post-update
            self.display_name=tk.Label(self,**self.w_preset,text=classes.name)
            self.display_name.place(rely=self.incy)
            self.widget_list.append(self.display_name)
            
            self.display_position=tk.Label(self,**self.w_preset,text=classes.position)
            self.display_position.place(relx=self.incx,rely=self.incy)
            self.widget_list.append(self.display_position)
            
            self.display_salary=tk.Label(self,**self.w_preset,text=classes.salary)
            self.display_salary.place(relx=self.incx+.25,rely=self.incy)
            self.widget_list.append(self.display_salary)

            self.display_id=tk.Label(self,**self.w_preset,text=classes.id)
            self.display_id.place(relx=self.incx+.5,rely=self.incy)
            self.widget_list.append(self.display_id)
            
            self.incy+=.1
            
              
    def getData(self) -> None:
        print('Employee List:\n')
        for classes in self.employee_list:
            print(f'{classes.name}\n{classes.position}\n{classes.salary}\n{classes.id}\n')

        
def main() -> None:
    App().mainloop()

if __name__ == "__main__":
	main()