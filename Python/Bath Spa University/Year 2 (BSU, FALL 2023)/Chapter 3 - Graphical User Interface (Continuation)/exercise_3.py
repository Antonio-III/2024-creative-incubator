import tkinter as tk
import math
root=tk.Tk()

# Default settings
FONT=('Tahoma',16)

CIRCLE_CALC_TEXT='A ≈ {}'
SHAPES_CALC_TEXT='A = {}'


CIRCLE_FORMULA_TEXT='A = π r^2'
SQUARE_FORMULA_TEXT='A = s^2'
RECT_FORMULA_TEXT='A = wl'
TITLE='Area Function'
GEOMETRY='500x500'


MAIN_BG='red'

CIRCLE_BG_COLOR='aqua'
CIRCLE_OUTLINE_COLOR='darkorchid2'
CIRCLE_DIAMETER_COLOR='darkorchid2'
RADIUS_COLOR='crimson'


SQUARE_BG_COLOR='lightgoldenrod1'
SQUARE_COLOR='cornflowerblue'

RECT_BG_COLOR='chartreuse'
RECT_COLOR='red'

def main() -> None:
	# VARS
	font=FONT

	# radius
	string_vr=tk.StringVar()

	# side
	string_vs=tk.StringVar()

	# width
	string_vw=tk.StringVar()
	# length
	string_vl=tk.StringVar()

	# frames.place() preset
	f_place_p={'relx':0,'rely':.1,'relwidth':1,'relheight':.9}


	# FUNCTS

	def switch_tabs(target_tab) -> None:
		nonlocal shapes_f,canvas
		shapes_f[target_tab].tkraise()

	def getr(*args) -> None:
		nonlocal string_vr
		input_r=(string_vr.get())
		if ' ' in input_r or len(input_r)==0:
			input_rint=0
		else:
			input_rint=int(input_r)

		calculation=math.pi*input_rint**2
		formula_c.configure(text=CIRCLE_CALC_TEXT.format(calculation))

	def gets(*args) -> None:
		nonlocal string_vs
		input_s=(string_vs.get())
		if ' ' in input_s or len(input_s)==0:
			input_sint=0
		else:
			input_sint=int(input_s)

		calculation=input_sint**2

		formula_s.configure(text=SHAPES_CALC_TEXT.format(calculation))

	def getwl(*args) -> None:
		width=string_vw.get()
		length=string_vl.get()
		wl=[width,length]
		inc=0
		usable=bool
		for _ in wl:
			if len(wl[inc])==0 or ' ' in wl[inc]:
				usable=False
			inc+=1

		if usable !=False:
			w_int=int(width)
			l_int=int(length)

			calculation=w_int*l_int
			formula_r.configure(text=SHAPES_CALC_TEXT.format(calculation))

	# header 
	root.title(TITLE)
	root.geometry(GEOMETRY)


	# (root,from_,to,bg,fg,font,text,command)
	# main
	tabs=tk.Frame(root,bg=MAIN_BG)
	tabs.place(relwidth=1,relheight=.1)

	tk.Button(tabs,font=font,text='circle',command=lambda: switch_tabs(0)).place(relwidth=.2,relheight=1)
	tk.Button(tabs,font=font,text='square',command=lambda: switch_tabs(1)).place(relx=.2,relwidth=.2,relheight=1)
	tk.Button(tabs,font=font,text='rectangle',command=lambda: switch_tabs(2)).place(relx=.4,relwidth=.2,relheight=1)

	# color bg of every tab: aqua, lightgoldenrod1, chartreuse

	# circle tab
	circle_f=tk.Frame(root,bg=CIRCLE_BG_COLOR)
	circle_f.place(**f_place_p)

	# formula
	formula_c=tk.Label(circle_f,bg=CIRCLE_BG_COLOR,font=font,text=CIRCLE_FORMULA_TEXT)
	formula_c.place(relx=.5,anchor='n')

	# canvas
	canvas=tk.Canvas(circle_f,bg=CIRCLE_BG_COLOR,highlightthickness=0)
	canvas.place(relx=.5,rely=.4,width=300,height=300,anchor=tk.CENTER)


	# make colors into consts

	#circle and diameter line
	circle=canvas.create_oval(10,10,290,290,outline=CIRCLE_OUTLINE_COLOR,width=5)
	diameter_l=canvas.create_line(10,150,290,150,fill=CIRCLE_DIAMETER_COLOR,width=5)

	# radius line, 'r', 
	radius_l=canvas.create_line(150,145,235,45,fill=RADIUS_COLOR,width=5)

	letter_r=tk.Label(canvas,font=font,bg=CIRCLE_BG_COLOR,fg=RADIUS_COLOR,text='r')
	letter_r.place(relx=.6,rely=.29)

	# 'radius' and entry 
	radius_t=tk.Label(circle_f,font=font,bg=CIRCLE_BG_COLOR,fg=RADIUS_COLOR,text='radius')
	radius_t.place(relx=.2,rely=.8)

	entry_c=tk.Entry(circle_f,font=font,bg=CIRCLE_BG_COLOR,fg=RADIUS_COLOR,highlightthickness=1,highlightbackground='grey',textvariable=string_vr)
	entry_c.place(relx=.35,rely=.8)
	string_vr.trace_add('write',getr)
	#---

	# square tab
	square_f=tk.Frame(root,bg=SQUARE_BG_COLOR)
	square_f.place(**f_place_p)

	# formula
	formula_s=tk.Label(square_f,bg=SQUARE_BG_COLOR,font=font,text=SQUARE_FORMULA_TEXT)
	formula_s.place(relx=.5,anchor='n')

	#canvas
	canvas_s=tk.Canvas(square_f,bg=SQUARE_BG_COLOR,highlightthickness=0)
	canvas_s.place(relx=.5,rely=.4,width=300,height=300,anchor=tk.CENTER)

	# square shape
	square=canvas_s.create_rectangle(10,10,290,290,outline=SQUARE_COLOR,width=5)

	# s label
	letter_s=tk.Label(canvas_s,font=font,bg=SQUARE_BG_COLOR,fg=SQUARE_COLOR,text='s')
	letter_s.place(relx=.94,rely=.45)

	# 'side' and entry
	side_t=tk.Label(square_f,font=font,bg=SQUARE_BG_COLOR,fg=SQUARE_COLOR,text='side')
	side_t.place(relx=.2,rely=.8)

	entry_s=tk.Entry(square_f,font=font,bg=SQUARE_BG_COLOR,fg=SQUARE_COLOR,highlightthickness=1,highlightbackground='grey',textvariable=string_vs)
	entry_s.place(relx=.35,rely=.8)
	string_vs.trace_add('write',gets)
	#---
	# rectangle tab
	rectangle_f=tk.Frame(root,bg=RECT_BG_COLOR)
	rectangle_f.place(**f_place_p)

	# formula
	formula_r=tk.Label(rectangle_f,bg=RECT_BG_COLOR,font=font,text=RECT_FORMULA_TEXT)
	formula_r.place(relx=.5,anchor='n')

	#canvas
	canvas_r=tk.Canvas(rectangle_f,bg=RECT_BG_COLOR,highlightthickness=0)
	canvas_r.place(relx=.5,rely=.4,width=500,height=300,anchor=tk.CENTER)

	# rectangle shape
	rectangle=canvas_r.create_rectangle(50,50,450,250,outline=RECT_COLOR,width=5)

	# w and l label
	letter_w=tk.Label(rectangle_f,font=font,bg=RECT_BG_COLOR,fg=RECT_COLOR,text='w')
	letter_w.place(relx=.08,rely=.37)

	letter_l=tk.Label(rectangle_f,font=font,bg=RECT_BG_COLOR,fg=RECT_COLOR,text='l')
	letter_l.place(relx=.5,rely=.59)

	# 'width' and 'length' text

	width_t=tk.Label(rectangle_f,font=font,bg=RECT_BG_COLOR,fg=RECT_COLOR,text='width')
	width_t.place(relx=.2,rely=.7)

	length_t=tk.Label(rectangle_f,font=font,bg=RECT_BG_COLOR,fg=RECT_COLOR,text='length')
	length_t.place(relx=.2,rely=.8)
	# w and l entry

	entry_rw=tk.Entry(rectangle_f,font=font,bg=RECT_BG_COLOR,fg=RECT_COLOR,textvariable=string_vw)
	entry_rw.place(relx=.35,rely=.7)
	string_vw.trace_add('write',getwl)

	entry_rl=tk.Entry(rectangle_f,font=font,bg=RECT_BG_COLOR,fg=RECT_COLOR,textvariable=string_vl)
	entry_rl.place(relx=.35,rely=.8)
	string_vl.trace_add('write',getwl)
	#---
	shapes_f=[circle_f,square_f,rectangle_f]
	shapes_f[0].tkraise()

	root.mainloop()

if __name__ == "__main__":
	main()
	