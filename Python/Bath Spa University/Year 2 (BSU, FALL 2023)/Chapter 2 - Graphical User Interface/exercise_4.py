import tkinter
from PIL import ImageTk
from tkinter import ttk, messagebox

# Default Settings
BANNER_IMG = 'Images/BSULOGO.png' # This assumes that in the directory where this file is in, there is an "Images" folder, and in it, is a "BSULOGO.png" file.
EMPTY_ENTRY = 0
ENTRIES = 5
GEOMETRY = '413x620'
ROOT_CONFIG = {'bg': 'white'}
TITLE = 'Ex04 Registration Page with grid geometry'


TEXTS_TITLE = 'Student Management System'
TEXTS_TITLE_1 = 'New Student Registration'

TEXTS_ENTRY_1 = 'Student Name'
TEXTS_ENTRY_2 = 'Mobile Number'
TEXTS_ENTRY_3 = 'Email Id'
TEXTS_ENTRY_4 = 'Home Address'
TEXTS_ENTRY_5 = 'Gender'
TEXTS_ENTRY_6 = 'Course Enrolled'
TEXTS_ENTRY_7 = 'Languages Known'
TEXTS_ENTRY_8 = 'Rate your English communication skills'

COURSES = ['BSc CC', 'BSc CY', 'BSc PSY', 'BA & BM']
LANGUAGES = ['English', 'Tagalog', 'Hindu/Urdu']

BUTTON_TEXT_1 = 'Submit'
BUTTON_TEXT_2 = 'Clear'
# I don't know why I included this
EASTER_EGG = 0
EASTER_EGG_LYRICS = ["I'm a buff baby, but I dance like a man", "She a nice lady and she shakin' the yams", "Spent the whole summer trappin' out the sedan", "Marching wit' the bands 'cause I think that I can"]


# We do this using grid because 'why not?'

# notes:
#   total rows: 17
#   total columns: 3

#-------Functions--------
# In rows 1~16
def font(size: int = 12, **kwargs: dict) -> tuple: 
    if 'b' in kwargs:
        return ('Tahoma', size, 'bold')
    else:
        return ('Tahoma', size)

    

def main() -> None:

    # Deletes anything entered in the Entry widget
    def on_clear():
        all_entries=[e1,e2,e3,e4,e5]

        for i in all_entries:
            i.delete(0,'end')

    # In row 15
    # A function can have not-yet-defined variable perform an action. The error comes when calling the function whilst having an undefined variable. But the function must be defined before referencing or calling it
    def slider_changed(event):
        l11.configure(text=get_current_value())

    def get_current_value():
        return current_value.get()

    # In row 16
    def submitcheck():
        global EASTER_EGG, EASTER_EGG_LYRICS
        
        ENTRIES=[]
        for i in entry_dict:
            ENTRIES.append(len(entry_dict[i].get()))
            
        if EMPTY_ENTRY not in ENTRIES:
            messagebox.showinfo('Success','You have submitted your form to nowhere!')

        else:
            messagebox.showerror('Error','You must fill all entry fields')

        
        if EASTER_EGG == 4:
            EASTER_EGG = 0
                
        print(EASTER_EGG_LYRICS[EASTER_EGG])
        EASTER_EGG += 1
        
    global EASTER_EGG
        
    # create output window
    root=tkinter.Tk()

    # set a base window size
    root.geometry(GEOMETRY)

    # make it unresizable
    root.resizable(False, False)

    # set a title
    root.title(TITLE)

    # set default bg
    root.configure(ROOT_CONFIG)
        
        #------Variables---------
    label_n_checkb_preset= {'font':font,'bg':'#f5f5f6'}
    entry_preset={'font':font,'bg':'#adaeb7'}
    radiob_preset={'font':font(11),'bg':'#f5f5f6'}
    button_preset={'font':font,'width':8,'bg':'#22263d','fg':'white'}

    # Create a dict for all the Entry widgets. To be stored by the widgets' 'textvariable' argument
    entry_dict = {}
    for i in range(1,ENTRIES+1):
        entry_dict[f'entry{i}']=tkinter.StringVar()

    # Variable to store an integer. In row 15
    current_value = tkinter.IntVar()
        
    #---------------------
    # row 0
    # create image
    try:
        banner_img=ImageTk.PhotoImage(file=BANNER_IMG)
    except FileNotFoundError:
        print(f'An image must be in the directory: "{BANNER_IMG}", else the program will not work.')
    else:
        # output image
        tkinter.Label(root,image=banner_img).grid(columnspan=3)

    # row 1
    # Frame
    frame=tkinter.Frame(root,bg='#f5f5f6')
    frame.grid(row=1,rowspan=16,columnspan=3,padx=10)

    l1=tkinter.Label(frame,text=TEXTS_TITLE, font=font(18,b='yes')) # type: ignore
    l1.grid(row=1,columnspan=3)

    # row 2
    l2=tkinter.Label(frame,text=TEXTS_TITLE_1,font=font(15,b='yes')) # type: ignore
    l2.grid(row=2,columnspan=3)

    # row 3
    l3=tkinter.Label(frame,text=TEXTS_ENTRY_1,**label_n_checkb_preset)
    l3.grid(row=3,sticky='w')

    e1=tkinter.Entry(frame,**entry_preset,textvariable=entry_dict['entry1'])
    e1.grid(row=3,column=1,sticky='w',columnspan=2)

    # row 4
    l4=tkinter.Label(frame,text=TEXTS_ENTRY_2,**label_n_checkb_preset)
    l4.grid(row=4,sticky='w')

    e2=tkinter.Entry(frame,**entry_preset,textvariable=entry_dict['entry2'])
    e2.grid(row=4,column=1,sticky='w',columnspan=2)

    # row 5
    l5=tkinter.Label(frame,text=TEXTS_ENTRY_3,**label_n_checkb_preset)
    l5.grid(row=5,sticky='w')

    e3=tkinter.Entry(frame,**entry_preset,textvariable=entry_dict['entry3'])
    e3.grid(row=5,column=1,sticky='w',columnspan=2)

    # row 6
    l6=tkinter.Label(frame,text=TEXTS_ENTRY_4,**label_n_checkb_preset)
    l6.grid(row=6,sticky='w')

    e4=tkinter.Entry(frame,**entry_preset,textvariable=entry_dict['entry4'])
    e4.grid(row=6,column=1,sticky='w',columnspan=2)

    # row 7
    l7=tkinter.Label(frame,text=TEXTS_ENTRY_5,**label_n_checkb_preset)
    l7.grid(row=7,sticky='w')

    e5=tkinter.Entry(frame,**entry_preset,textvariable=entry_dict['entry5'])
    e5.grid(row=7,column=1,sticky='w',columnspan=2)

    # row 8
    l8=tkinter.Label(frame,text=TEXTS_ENTRY_6,**label_n_checkb_preset)
    l8.grid(row=8,sticky='w')

    r1=tkinter.Radiobutton(frame,text=COURSES[0],**radiob_preset,value=0)
    r1.grid(row=8,sticky='w',column=1)

    # row 9
    r2=tkinter.Radiobutton(frame,text=COURSES[1],**radiob_preset,value=1)
    r2.grid(row=9,sticky='w',column=1)

    # row 10
    r3=tkinter.Radiobutton(frame,text=COURSES[2],**radiob_preset,value=2)
    r3.grid(row=10,sticky='w',column=1)

    # row 11
    r4=tkinter.Radiobutton(frame,text=COURSES[3],**radiob_preset,value=3)
    r4.grid(row=11,sticky='w',column=1)

    # row 12
    l9=tkinter.Label(frame,text=TEXTS_ENTRY_7,**label_n_checkb_preset)
    l9.grid(row=12,sticky='w')

    c1=tkinter.Checkbutton(frame,text=LANGUAGES[0],**label_n_checkb_preset)
    c1.grid(row=12,column=1,sticky='w')

    c2=tkinter.Checkbutton(frame,text=LANGUAGES[1],**label_n_checkb_preset)
    c2.grid(row=12,column=2)

    # row 13
    c3=tkinter.Checkbutton(frame,text=LANGUAGES[2],**label_n_checkb_preset)
    c3.grid(row=13,column=1,sticky='w')

    # row 14
    # sticky is centered by default (???). 'we' does the same thing
    l10=tkinter.Label(frame,text=TEXTS_ENTRY_8,**label_n_checkb_preset)
    l10.grid(row=14,columnspan=3)

    # row 15
    # tkinter.scale orientation is vertical by default 
    slider = ttk.Scale(frame,from_=0,to=10,variable=current_value,command=slider_changed)
    slider.grid(row=15,columnspan=2)

    # In the case of creating objects, always separate the geometry management from the object
    # display the value of the Scale 
    l11 = tkinter.Label(frame,text=get_current_value(),**label_n_checkb_preset)
    l11.grid(row=15, column=2,sticky='w')

    # row 16
    tkinter.Button(frame,text=BUTTON_TEXT_1,**button_preset,command=submitcheck).grid(row=16,sticky='w')
    tkinter.Button(frame,text=BUTTON_TEXT_2,**button_preset,command=on_clear).grid(row=16,column=2)

    # start the app
    root.mainloop()

if __name__ == "__main__":
	main()