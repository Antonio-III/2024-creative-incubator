import tkinter as tk
from PIL import ImageTk,Image
import re

# Default settings
TITLE='Student Class'
GEOMETRY='600x600'

FONT=('Tahoma',16)

BG_COLOR='lightgoldenrod1'
TEXT_COLOR='cornflowerblue'

STUDENT_1_IMG_DIR='Images/student_1.png'
STUDENT_2_IMG_DIR='Images/student_2.jpg'

IMG_SIZE=(300,300)

STUDENT_1_NAME='You'
STUDENT_1_MARKS=('69','80','75')

STUDENT_2_NAME='Me'
class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(GEOMETRY)

        self['bg']=BG_COLOR

        #vars
        self.font=FONT
        self.w_preset={'font':self.font,'bg':self['bg'],'fg':TEXT_COLOR}
        self.p_preset={'relx':.75,'anchor':'n'}
        self.p_preset_2={'relx':.86,'anchor':'n','relwidth':.1,'relheight':.04}
        self.mark_1_input=tk.StringVar()
        self.mark_2_input=tk.StringVar()
        self.mark_3_input=tk.StringVar()

        # objects
        self.student_1=self.Student(STUDENT_1_NAME,mark1=STUDENT_1_MARKS[0],mark2=STUDENT_1_MARKS[1],mark3=STUDENT_1_MARKS[2])
        self.student_2=self.Student(STUDENT_2_NAME)
        
        # widgets student 1 guis (left)
        self.student_1_image=self.resize(STUDENT_1_IMG_DIR)
        self.student_1_label=tk.Label(self,**self.w_preset,image=self.student_1_image)
        self.student_1_label.place(x=0)
        
        self.student_2_image=self.resize(STUDENT_2_IMG_DIR)
        self.student_2_label=tk.Label(self,**self.w_preset,image=self.student_2_image)
        self.student_2_label.place(rely=.5)

        self.student_1_details=tk.Label(self,**self.w_preset,text=self.student_1.display())
        self.student_1_details.place(**self.p_preset)

        #student 2 guis (right)
        self.student_2_details=tk.Label(self,**self.w_preset,text=self.student_2.display(mode=1))
        self.student_2_details.place(**self.p_preset,rely=.5)

        self.entry_1=tk.Entry(self,font=self.font,textvariable=self.mark_1_input)
        self.entry_1.place(**self.p_preset_2,rely=.59)

        self.entry_2=tk.Entry(self,font=self.font,textvariable=self.mark_2_input)
        self.entry_2.place(**self.p_preset_2,rely=.67)

        self.entry_3=tk.Entry(self,font=self.font,textvariable=self.mark_3_input)
        self.entry_3.place(**self.p_preset_2,rely=.75)


        
        self.button_1=tk.Button(self,**self.w_preset,text='Get Average',command=self.studentupdate)
        self.button_1.place(**self.p_preset,rely=.9)

        
    def resize(self,directory: str) -> ImageTk.PhotoImage:
        b_img=Image.open(directory)
        r_img=b_img.resize(IMG_SIZE)
        return ImageTk.PhotoImage(r_img)

    def studentupdate(self) -> None:
        self.list=[self.student_2_details,self.entry_1,self.entry_2,self.entry_3]
        # widget destroy
        for i in self.list:
            i.destroy()
        
        # object
        self.student_2=self.Student(STUDENT_2_NAME,mark1=self.mark_1_input.get(),mark2=self.mark_2_input.get(),mark3=self.mark_3_input.get())
        
        # widget
        self.student_2_details=tk.Label(self,**self.w_preset,text=self.student_2.display(mode=1))
        self.student_2_details.place(**self.p_preset,rely=.5)
        
        self.entry_1=tk.Entry(self,font=self.font,textvariable=self.mark_1_input)
        self.entry_1.place(**self.p_preset_2,rely=.59)

        self.entry_2=tk.Entry(self,font=self.font,textvariable=self.mark_2_input)
        self.entry_2.place(**self.p_preset_2,rely=.67)

        self.entry_3=tk.Entry(self,font=self.font,textvariable=self.mark_3_input)
        self.entry_3.place(**self.p_preset_2,rely=.75)
        
    class Student():
        def __init__(self,name,**kwargs):
            self.name=name
            
            self.mark1=kwargs.get('mark1','')
            self.mark2=kwargs.get('mark2','')
            self.mark3=kwargs.get('mark3','')

        def calcGrade(self):
            self.list=[self.mark1,self.mark2,self.mark3]
            
            for i in self.list:
                if not re.match(r'^\d+$',str(i)):
                    self.list[self.list.index(i)]=0   


            return round(sum(int(i) for i in self.list)/len(self.list),3)
            
        def display(self,**kwargs):
            self.operation=kwargs.get('mode','')
            if self.operation!='':
                return f'Name: {self.name}\n\nMark 1:\n\nMark 2:\n\nMark 3:\n\nAverage: {self.calcGrade()}'
            else:
                return f'Name: {self.name}\n\nMark 1: {self.mark1}\n\nMark 2: {self.mark2}\n\nMark 3: {self.mark3}\n\nAverage: {self.calcGrade()}'
                
def main() -> None:
    try:
        Main().mainloop()
    except FileNotFoundError:
        print(f"There must be these files: '{STUDENT_1_IMG_DIR}', '{STUDENT_2_IMG_DIR}' in the current directory or the app cannot work.")

if __name__ == "__main__":
	main()