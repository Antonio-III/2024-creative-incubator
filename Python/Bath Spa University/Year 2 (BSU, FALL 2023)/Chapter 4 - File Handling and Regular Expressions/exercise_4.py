import tkinter as tk
# Default settings
TITLE='Return Letter Count'
GEOMETRY='500x500'
BG_COLOR='lightgoldenrod1'
TEXT_COLOR='cornflowerblue'
FONT=('Tahoma',16)
TEXT_FILE_DIR='Text Files/sentences.txt'
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(GEOMETRY)
        self['bg']=BG_COLOR
        self.entry_1_v=tk.StringVar()
        #vars
        self.font=FONT
        self.w_preset={'font':self.font,'bg':self['bg'],'fg':TEXT_COLOR}
        self.file=TEXT_FILE_DIR
        
        self.label_1=tk.Label(self,**self.w_preset,text='Find any occurences of the input string in File')
        self.label_1.place(relx=.5,anchor='n')
        
        self.entry_1=tk.Entry(self,font=self.font,textvariable=self.entry_1_v)
        self.entry_1.place(relx=.5,rely=.1,anchor='n')

        self.button_1=tk.Button(self,**self.w_preset,text='Search',command=self.search)
        self.button_1.place(relx=.81,rely=.09,anchor='n')
        
        self.label_2=tk.Label(self)

        self.label_3=tk.Label(self,**self.w_preset,text='File contents')
        self.label_3.place(relx=.5,rely=.3,anchor='n')
    
        self.text_1=tk.Text(self,font=self.font)
        self.text_1.place(relx=.5,rely=.4,anchor='n',relwidth=.9,relheight=.55)
        self.insert_content()
        
        self.scroll=tk.Scrollbar(self,orient='vertical')
        self.scroll.place(relx=.966,rely=.4,anchor='n',relheight=.55)

        self.scroll.config(command=self.text_1.yview)
        self.text_1.config(yscrollcommand=self.scroll.set)
        
    def search(self):
        query=self.entry_1_v.get()

        file=self.file

        self.label_2.destroy()

        
        with open(file) as file_handler:
            file_list=file_handler.readlines()           
        count=sum(1 for element in file_list if query in element)

        if len(query)==0 or ' ' in query:
            count=0

        self.label_2=tk.Label(self,**self.w_preset,text=f'{count} found.')
        self.label_2.place(relx=.5,rely=.2,anchor='n')

    def insert_content(self):
        file=self.file
        text=self.text_1
        
        with open(file) as file_handler:
            content=file_handler.read()
        text.insert(tk.END,content)
        
if __name__=='__main__':
    App().mainloop()