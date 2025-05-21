import tkinter as tk
from PIL import ImageTk, Image

# Default settings
TITLE='WOof woof'
GEOMETRY='500x500'
BG_COLOR='lightgoldenrod1'
FONT=('Tahoma',16)
TEXT_COLOR='cornflowerblue'

DOG_1_NAME='Victor'
DOG_1_AGE=1
DOG_1_IMG_DIR='Images/small dog.jpg'

DOG_2_NAME='Donald'
DOG_2_AGE=42
DOG_2_IMG_DIR='Images/big dog.jpg'

DOG_IMG_SIZE=(250,250)

BARK_MSG='WOOF WOOF'

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(GEOMETRY)
        
        self['bg']=BG_COLOR

        # vars
        self.w_preset={'font':FONT,'bg':BG_COLOR,'fg':TEXT_COLOR}
        self.p_preset={'relx':.75,'anchor':'n'}

        # dog instances (backend)
        self.dog_1=self.Dog(DOG_1_NAME,DOG_1_AGE)
        self.dog_2=self.Dog(DOG_2_NAME,DOG_2_AGE)        

         # dog images
        self.dog_1_label=tk.Label(self,image=self.dog_1.image())
        self.dog_1_label.place(x=0)

        self.dog_2_label=tk.Label(self,image=self.dog_2.image())
        self.dog_2_label.place(rely=.5)

        # texts
        self.label_3=tk.Label(self,**self.w_preset,text='Dog Characteristics')
        self.label_3.place(**self.p_preset)


        # details
        self.dog_1_details=tk.Label(self,**self.w_preset,text=self.dog_1.details())
        self.dog_1_details.place(**self.p_preset,rely=.1)
        self.bark_1=tk.Label(self)
        
        self.dog_2_details=tk.Label(self,**self.w_preset,text=self.dog_2.details())
        self.dog_2_details.place(**self.p_preset,rely=.6)

        self.bark_2=tk.Label(self)


        # button
        self.button_1=tk.Button(self,**self.w_preset,text='Bark',command=self.bark)
        self.button_1.place(**self.p_preset,rely=.9)
        
    class Dog():
        def __init__(self,name,age):
            self.name=name
            self.age=age
            self.dog_img=None
            
        def details(self) -> str:
            return 'Name: {self.name}\nAge: {self.age}'
            

        def resize(self,directory,width,height) -> ImageTk.PhotoImage:
            b_img= Image.open(directory)
            r_img=b_img.resize((width,height))
            self.dog_img=ImageTk.PhotoImage(r_img)
            return self.dog_img
        
        def image(self) -> ImageTk.PhotoImage:
            if self.age<DOG_2_AGE:
                return self.resize(DOG_1_IMG_DIR,*DOG_IMG_SIZE)
            else:
                return self.resize(DOG_2_IMG_DIR,*DOG_IMG_SIZE)

    def bark(self) -> None:
        def bark_1():
            self.bark_1=tk.Label(self,**self.w_preset,text=BARK_MSG)
            self.bark_1.place(**self.p_preset,rely=.25)

        def bark_2():
            self.bark_2=tk.Label(self,**self.w_preset,text=BARK_MSG)
            self.bark_2.place(**self.p_preset,rely=.75)
        

        # destroy existing labels. these 2 have to be created by the end of this function call. we do this to save memory and because I want to make things harder for myself (kinda)
        self.bark_1.destroy()
        self.bark_2.destroy()

        if self.dog_1.age>self.dog_2.age:
            bark_1()
            
            # we need to create label because the top of the function code block requires it to exist for it to be destroyed
            self.bark_2=tk.Label(self)

        elif self.dog_2.age>self.dog_1.age:
            # we need to create label because the top of the function code block requires it to exist for it to be destroyed
            self.bark_1=tk.Label(self)
            
            bark_2()
                
def main() -> None:
    try:
        App().mainloop()
    except FileNotFoundError:
        print(f'There must be these files: "{DOG_1_IMG_DIR}", "{DOG_2_IMG_DIR}" in the current directory or the app will not work.')

if __name__ == "__main__":
	main()