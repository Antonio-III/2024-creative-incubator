import tkinter as tk
# Default settings
TITLE='Write to txt file'
GEOMETRY='500x500'

BG_COLOR='lightgoldenrod1'
TEXT_COLOR='cornflowerblue'

FONT=('Tahoma',15)
# Create a file called `bio.txt` in the folder `Text Files`
TEXT_FILE_DIR='Text Files/bio.txt'
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(GEOMETRY)
        self['bg']=BG_COLOR
        # vars
        font=FONT
        w_preset={'font':font,'bg':BG_COLOR,'fg':TEXT_COLOR}
        self.file=TEXT_FILE_DIR
        
        self.name_v=tk.StringVar()
        self.age_v=tk.StringVar()
        self.hometown_v=tk.StringVar()
        


        # widget rules (root,from_,to,bg,fg,font,text,command)

        # name
        tk.Label(self,**w_preset,text='Name: ').place(x=0)
    
        tk.Entry(self,font=font,textvariable=self.name_v).place(relx=.25)

        # age
        tk.Label(self,**w_preset,text='Age: ').place(rely=.1)
  
        tk.Entry(self,font=font,textvariable=self.age_v).place(relx=.25,rely=.1)

        # hometown
        tk.Label(self,**w_preset,text='Hometown: ').place(rely=.2)
        
        tk.Entry(self,font=font,textvariable=self.hometown_v).place(relx=.25,rely=.2)

        # button write
        tk.Button(self,**w_preset,text='Write to file',command=self.write).place(relx=.5,rely=.35,anchor=tk.CENTER)

        # button output
        tk.Button(self,**w_preset,text='Output file',command=self.output).place(relx=.5,rely=.45,anchor=tk.CENTER)

        self.txt_w=tk.Text(self,font=font)
        self.txt_w.place(relx=.5,rely=.55,relwidth=.9,relheight=.4,anchor='n')

        
    # functions
    def write(self):
        bio=self.file
        name=self.name_v.get()
        age=self.age_v.get()
        hometown=self.hometown_v.get()

        with open(bio,'w') as file_handler:
            file_handler.write(f'Name: {name}\n')
            file_handler.write(f'Age: {age}\n')
            file_handler.write(f'Hometown: {hometown}\n')


    def output(self):
        bio=self.file
        # get the text
        with open(bio) as file_handler:
            content=file_handler.read()
        #delete text first
        self.txt_w.delete('1.0','end')
        # insert
        self.txt_w.insert(tk.END,content)

def main() -> None:
	App().mainloop()	

if __name__ == "__main__":
	main()