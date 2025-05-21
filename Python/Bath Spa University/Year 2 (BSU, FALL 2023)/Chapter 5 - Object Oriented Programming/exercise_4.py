import tkinter as tk
from PIL import ImageTk,Image
import math
import re

# Default settings
TITLE='Shapes'

GEOMETRY='300x300'

FONT=('Tahoma',12)
BG_COLOR='lightgoldenrod1'
TEXT_COLOR='cornflowerblue'

IMAGE_SIZE=(100,100)

IMAGES_DIR='Images/{shape_name}.png'

SHAPE_FILE_NAMES=['circle','triangle','rectangle']

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title=TITLE
        self.geometry(GEOMETRY)

        self['bg']=BG_COLOR

        self.font=FONT
        self.w_preset={'font':self.font,'bg':self['bg'],'fg':TEXT_COLOR}

        self.images=[]

        self.param_1=tk.IntVar()
        self.param_2=tk.IntVar()
        
        self.shapes=SHAPE_FILE_NAMES
        
        # widgets
        
        self.place_shapes()

        # label
        self.place_widgets()

        
    def resize_img(self,directory)->None:
        b_img=Image.open(directory)
        r_img=b_img.resize(IMAGE_SIZE)
        # always keep the photoimage in a persisting variable ie doesn't get garbage collected after function execution eg a class attribute if inside a class    
        self.img=ImageTk.PhotoImage(r_img)
        # append already-persisting object inside a list so there is always a pointer to the photoimage.
        # This is useful because if this function runs again, it'll replace the attribute's (self.img) value with a different photoimage, so we need a place to reference the previous photoimage
        self.images.append(self.img)
        
    def place_shapes(self)->None:
        self.incx=0
        for i in self.shapes:
            self.resize_img(IMAGES_DIR.format(shape_name=i))
            
            self.place_shape=tk.Label(self,image=self.images[-1])
            self.place_shape.place(relx=self.incx)
            
            self.incx+=.33
            
    def place_widgets(self)->None:
        self.label_1=tk.Label(self,**self.w_preset,text='radius/base/width')
        self.label_1.place(relx=.3,rely=.7,anchor='s')

        self.label_1=tk.Label(self,**self.w_preset,text='height')
        self.label_1.place(relx=.4,rely=.8,anchor='s')
        
        self.entry_1=tk.Entry(self,font=self.font,textvariable=self.param_1)
        self.entry_1.place(relx=.7,rely=.7,anchor='s',relwidth=.3)
        
        self.entry_2=tk.Entry(self,font=self.font,textvariable=self.param_2)
        self.entry_2.place(relx=.7,rely=.8,anchor='s',relwidth=.3)

        self.entry_3=tk.Label(self,**self.w_preset,text='a')
        self.entry_3.place(relx=.165,rely=.4,anchor=tk.CENTER)

        self.entry_4=tk.Label(self,**self.w_preset,text='b')
        self.entry_4.place(relx=.165+.33,rely=.4,anchor=tk.CENTER)
        
        self.entry_5=tk.Label(self,**self.w_preset,text='c')
        self.entry_5.place(relx=.165+.66,rely=.4,anchor=tk.CENTER)
        
        self.button_1=tk.Button(self,**self.w_preset,text='Get Area',command=self.get_area)
        self.button_1.place(relx=.5,rely=.95,anchor='s')
        
    def get_area(self)->None:
  
        self.input_1=str(self.param_1.get())
        self.input_2=str(self.param_2.get())
        
        self.input_params=self.input_1+self.input_2
    
        if re.match(r'^\d+$',self.input_params):
            
            self.shapes_instance=self.Shapes(param1=self.input_1,param2=self.input_2
                                             )
            self.circle_area=self.Circle(param1=self.shapes_instance.param1,param2=self.input_2).area()
            self.rectangle_area=self.Rectangle(param1=self.shapes_instance.param1,param2=self.input_2).area()
            self.triangle_area=self.Triangle(param1=self.shapes_instance.param1,param2=self.input_2).area()

            self.update_label()
            
    def update_label(self)->None:
        self.entry_3.configure(text=self.circle_area)
        self.entry_4.configure(text=self.triangle_area)
        self.entry_5.configure(text=self.rectangle_area)

    # classes 
    class Shapes:
        def __init__(self,**kwargs):
            self.param1=int(kwargs.get('param1', 0))
            self.param2=int(kwargs.get('param2', 0))
            
    class Circle(Shapes):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)

        def area(self)->float:
            return round(math.pi*self.param1**2,3)
        
    class Triangle(Shapes):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)

        def area(self)->float:
            return (self.param1*self.param2)/2
            
    class Rectangle(Shapes):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)

        def area(self)->int:
            return self.param1*self.param2

def main()->None:
    try:
        App().mainloop()
    except FileNotFoundError:
        print(f'A directory "{IMAGES_DIR}" must exist in the current directory with the names ("shape_name"={SHAPE_FILE_NAMES}). The directory can be changed at the top of the code file.')

if __name__ == "__main__":
	main()