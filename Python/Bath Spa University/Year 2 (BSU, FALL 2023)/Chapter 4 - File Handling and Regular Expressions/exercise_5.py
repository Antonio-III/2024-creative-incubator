import re
import tkinter as tk
from tkinter import messagebox

# Default settings
TITLE='Validate Password'
GEOMETRY='500x500'
BG_COLOR='lightgoldenrod1'
FONT=('Tahoma',16)
TEXT_COLOR='cornflowerblue'

ENTER_BTN_COLOR='red'

MIN_PASS_LEN=6
MAX_PASS_LEN=12
PW_COND=r'(?=.*?[A-Z])(?=.*?\d)(?=.*?[a-z])(?=.*?[@#$])^[A-Za-z\d@#$]{6,12}$'

FAIL_MSG_TITLE='Fail'
FAIL_MSG_MSG='Incorrect password. Remaining attempts: {}.'

SUCCESS_MSG_TITLE='Success'
SUCCESS_MSG_MSG='You successfully broke into a bank!'

CAUGHT_MSG_TITLE='WEEWWOOOO'
CAUGHT_MSG_MSG='WEEEEEEEEEEWWOOOOOOOOOOOOO The police have been alerted! WEEEEEEEWOOOOOOOOOOOOO'

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(GEOMETRY)
        self['bg']=BG_COLOR
        
        #vars
        self.font=FONT
        self.w_preset={'font':self.font,'bg':BG_COLOR,'fg':TEXT_COLOR}
        self.p_preset={'relx':'.5','anchor':'n'}
        self.password_v=tk.StringVar()

        # default # tries
        self.tries=5
        # state default value
        self.state=True
        
        self.label_1=tk.Label(self,**self.w_preset,text='Enter Password')
        self.label_1.place(**self.p_preset)  # type: ignore

        self.entry_1=tk.Entry(self,font=self.font,textvariable=self.password_v)
        self.entry_1.place(**self.p_preset,rely=.1) # type: ignore

        self.button_1=tk.Button(self,font=self.font,bg=ENTER_BTN_COLOR,text='Enter',command=self.enter_pass_brute)
        self.button_1.place(relx=.8,rely=.08,anchor='n')
        
        self.entry_2=tk.Label(self,**self.w_preset,text='Must follow these rules:')
        self.entry_2.place(**self.p_preset,rely=.2) # type: ignore

        self.label_2=tk.Label(self,**self.w_preset,text='Minimum 1 letter from a-z')
        self.label_2.place(**self.p_preset,rely=.3) # type: ignore

        self.label_3=tk.Label(self,**self.w_preset,text='Minimum 1 digit from 0-9')
        self.label_3.place(**self.p_preset,rely=.4) # type: ignore

        self.label_4=tk.Label(self,**self.w_preset,text='Minimum 1 letter from A-Z')
        self.label_4.place(**self.p_preset,rely=.5) # type: ignore

        self.label_5=tk.Label(self,**self.w_preset,text='1 of these @#$ symbols')
        self.label_5.place(**self.p_preset,rely=.6) # type: ignore 

        self.label_6=tk.Label(self,**self.w_preset,text='Min/Max length: 6/12')
        self.label_6.place(**self.p_preset,rely=.7) # type: ignore

    def enter_pass_brute(self) -> None:
        password=self.password_v.get()
        self.state=True
        # ord returns the ASCII code of the argument. Which is a number we can iterate through. We then convert this ASCII to its character form, which is then stored in the variable
        letters_u=[chr(i) for i in range(ord('A'), ord('Z') +1)]
        letters_l=[x.lower() for x in letters_u]
        numbers=[str(y) for y in range(10)]
        special=['@','#','$']
        
        letters_u_c=sum(1 for char in password if char in letters_u)
        letters_l_c=sum(1 for char in password if char in letters_l)
        numbers_c=  sum(1 for char in password if char in numbers)
        special_c=  sum(1 for char in password if char in special)
        total_c=[letters_u_c,letters_l_c,numbers_c,special_c]

        # 1st condition of password. check min and max lengths. 2nd condition of password. check if certain chars are present
        first_condition_not_satisfied=len(password)<MIN_PASS_LEN or len(password)>MAX_PASS_LEN or 0 in total_c

        if first_condition_not_satisfied:
                self.state=False
   
        # 3rd condition. check if password has invalid chars
        for char in password:
            if char not in letters_u and char not in letters_l and char not in numbers and char not in special:
                self.state=False
                
        self.checkstate()
        self.checktries()

    def enter_pass_regex(self) -> None:
        password=self.password_v.get()
        condition=PW_COND
        self.state=True
        if re.match(condition,password)==None:
            self.state=False

        self.checkstate()
        self.checktries()

    def checkstate(self) -> None:
        if self.state==False:
            self.tries-=1
            messagebox.showerror(FAIL_MSG_TITLE,FAIL_MSG_MSG.format(self.tries))
        else:
            messagebox.showinfo(SUCCESS_MSG_TITLE,SUCCESS_MSG_MSG)

    def checktries(self) -> None:
        if self.tries==0:
            messagebox.showerror(CAUGHT_MSG_TITLE,CAUGHT_MSG_MSG)
            # close app
            self.destroy()

def main() -> None:
    App().mainloop()

if __name__ == "__main__":
	main()