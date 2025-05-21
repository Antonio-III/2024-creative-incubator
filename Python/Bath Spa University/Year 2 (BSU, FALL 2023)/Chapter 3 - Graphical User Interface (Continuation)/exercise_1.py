import tkinter as tk

# Default settings
BACK_BUTTON_TEXT='<-'
BUTTON_TEXT='Update Greeting'
COLOR_OPTIONS=('Orange','Violet','Red')
DEFAULT_BG='green'
DEFAULT_TEXT_COLOR='blue'
FONT=('Tahoma',16)
GEOMETRY='400x400'
GREETING_TEXT='Greetings, {}'
HEADER_TEXT='Greeting app'
TITLE='Greeting App'

def main() -> None:
	font=FONT	

	root=tk.Tk()
	name=tk.StringVar()
	color=tk.StringVar()	

	def switch():
		nonlocal frames
		DisplayFrame.configure(bg=color.get())
		l1.configure(text=GREETING_TEXT.format(name.get()),bg=color.get())
		frames[-1].tkraise()
		frames[0],frames[-1]=frames[-1],frames[0]

	root.geometry(GEOMETRY)
	root.title(TITLE)

	InputFrame=tk.Frame(root,bg=DEFAULT_BG)
	InputFrame.place(relwidth=1,relheight=1)

	tk.Label(InputFrame,text=HEADER_TEXT,font=font,fg=DEFAULT_TEXT_COLOR,bg=DEFAULT_BG).place(relx=.5,anchor='n')
	tk.Entry(InputFrame,textvariable=name,font=font).place(relx=.5,rely=.1,anchor='n')

	color.set(COLOR_OPTIONS[0])
	tk.OptionMenu(InputFrame,color,*COLOR_OPTIONS).place(relx=.5,rely=.2,anchor='n')

	tk.Button(InputFrame,text=BUTTON_TEXT,font=font,fg=DEFAULT_TEXT_COLOR,bg=DEFAULT_BG,command=switch).place(relx=.5,rely=.3,anchor='n')


	DisplayFrame=tk.Frame(root,bg=color.get())
	DisplayFrame.place(relwidth=1,relheight=1)

	l1=tk.Label(DisplayFrame,font=font,bg=color.get())
	l1.place(relx=.5,anchor='n')

	tk.Button(DisplayFrame,text=BACK_BUTTON_TEXT,font=font,command=switch).place(relx=0)
	InputFrame.tkraise()
	frames=[InputFrame,DisplayFrame]

	root.mainloop()

if __name__ == "__main__":
	main()