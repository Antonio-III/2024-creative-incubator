import tkinter as tk

# Default settings
TITLE='Count String'
GEOMETRY='500x500'
BG_COLOR='lightgoldenrod1'
FONT=('Tahoma',16)
TEXT_COLOR='cornflowerblue'
TEXT_FILE_DIR='Text Files/sentences.txt'
TARGET_STRS=['Hello my name is Peter Parker','I love Python Programming','Love','Enemy']

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title(TITLE)
        self.geometry(GEOMETRY)
        self['bg']=BG_COLOR

        # vars
        font=FONT
        self.w_preset=w_preset={'font':font,'bg':BG_COLOR,'fg':TEXT_COLOR}
        self.file=TEXT_FILE_DIR
        self.search_v=tk.StringVar()
        self.target_strings=TARGET_STRS
        

        # (root,from_,to,bg,fg,font,text,command)
        tk.Label(self,**w_preset,text='Count the amount of times these strings occurred:').place(relx=.0)
        
        self.item_1=tk.Label(self,**w_preset)
        self.item_1.place(rely=.1)

        self.item_2=tk.Label(self,**w_preset)
        self.item_2.place(rely=.2)

        self.item_3=tk.Label(self,**w_preset)
        self.item_3.place(rely=.3)

        self.item_4=tk.Label(self,**w_preset)
        self.item_4.place(rely=.4)

        # execute function
        self.count_sentences()

        # Extension
        tk.Label(self,**w_preset,text='Extension:').place(relx=.5,rely=.5,anchor=tk.CENTER)
        
        self.entry=tk.Entry(self,font=font,textvariable=self.search_v)
        self.entry.place(relx=.5,rely=.6,anchor=tk.CENTER)
        
        tk.Button(self,**w_preset,text='Find',command=self.search).place(relx=.8,rely=.6,anchor=tk.CENTER)

        self.count=tk.Label(self)
        
    def count_sentences(self) -> None:
        file=self.file
        strings_t=self.target_strings
        
        item_1=self.item_1
        item_2=self.item_2
        item_3=self.item_3
        item_4=self.item_4
        
        with open(file) as file_handler:
            string_l=file_handler.readlines()
            t_1_c=sum(1 for element in string_l if strings_t[0].lower() in element.lower())
            t_2_c=sum(1 for element in string_l if strings_t[1].lower() in element.lower())
            t_3_c=sum(1 for element in string_l if strings_t[2].lower() in element.lower())
            t_4_c=sum(1 for element in string_l if strings_t[3].lower() in element.lower())

        item_1.configure(text=f'"{strings_t[0]}" count: {t_1_c}')
        item_2.configure(text=f'"{strings_t[1]}" count: {t_2_c}')
        item_3.configure(text=f'"{strings_t[2]}" count: {t_3_c}')
        item_4.configure(text=f'"{strings_t[3]}" count: {t_4_c}')


    def search(self) -> None:
        query=self.search_v.get()
        file=self.file


        self.count.destroy()
    
        with open(file) as file_handler:
            count=sum(1 for element in file_handler if query in element)
            
            if len(query)==0:
                count=0

            self.count=tk.Label(self,**self.w_preset,text=f'{count} found')    
            self.count.place(relx=.4,rely=.65)
                               

def main() -> None:
    try:
        App().mainloop()	
    except FileNotFoundError:
        print("There must be a folder and text named 'Text Files/sentences.txt' in the current directory for the app to start. You can change this value at the top of the code file.")
        
if __name__ == "__main__":
	main()