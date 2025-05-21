import tkinter as tk
# Default settings
HELLO_MSG='Hi! My name is {}!'

NOISE_AMOUNT=3
NOISE_MSG='This animal says: {}'

DETAILS_MSG='Details\n Type: {type}, Color: {color}, Age: {age}, Weight: {weight}, Noise: {noise}'

TITLE='Playing around with Classes'

GEOMETRY='400x400'

BG_COLOR='lightgoldenrod1'
TEXT_COLOR='cornflowerblue'

FONT=('Tahoma',12)

# type, name, color, age, weight, noise
ANIMAL_1=('Dog','Anthony','Blue',12,'10kg','bark')
ANIMAL_2=('Cat','Fantano','White',10,'5kg','meow')

class App(tk.Tk):
    class Animal:
        def __init__(self,c_type,c_name,c_color,c_age,c_weight,c_noise):
            self.type=c_type
            self.name=c_name
            self.color=c_color
            self.age=c_age
            self.weight=c_weight
            self.noise=c_noise
        def sayHello(self)->None:
            print(HELLO_MSG.format(self.name))
        def makeNoise(self)->None:
            print(NOISE_MSG.format(self.noise*NOISE_AMOUNT))
        def animalDetails(self)->None:
            print(DETAILS_MSG.format(type=self.type,color=self.color,age=self.age,weight=self.weight,noise=self.noise))
            
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(GEOMETRY)

        self['bg']=BG_COLOR
        
        self.w_preset={'font':FONT,'bg':self['bg'],'fg':TEXT_COLOR}

        self.dog=self.Animal(*ANIMAL_1)
        self.cat=self.Animal(*ANIMAL_2)
        
        self.animals_list=[self.dog,self.cat]


        self.place_widgets()

    def place_widgets(self)->None:
        self.relx=0

        for i,animal in enumerate(self.animals_list,start=1):
            self.label_widget=tk.Label(self,**self.w_preset,text=f'Animal {i}')
            self.label_widget.place(relx=self.relx)
            
            self.button_widget=tk.Button(self,**self.w_preset,text='sayHello',command=animal.sayHello)
            self.button_widget.place(relx=self.relx,rely=.1)

            self.button_widget_two=tk.Button(self,**self.w_preset,text='makeNoise',command=animal.makeNoise)
            self.button_widget_two.place(relx=self.relx,rely=.2)

            self.button_widget_three=tk.Button(self,**self.w_preset,text='animalDetails',command=animal.animalDetails)
            self.button_widget_three.place(relx=self.relx,rely=.3)

            self.relx+=.5

def main()->None:
    App().mainloop()

if __name__ == "__main__":
	main()