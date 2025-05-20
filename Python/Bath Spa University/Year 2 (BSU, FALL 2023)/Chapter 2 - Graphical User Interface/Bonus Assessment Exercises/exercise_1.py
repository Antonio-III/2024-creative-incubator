import tkinter as tk
from PIL import ImageTk, Image
import re

# Default settings
IMAGE = 'images/temperature-thermometer-icon-free-vector.jpg'
IMAGE_SIZE = (400, 400)
GEOMETRY = '400x400'
TITLE = 'Temperature Converter'

CELSIUS_LABEL_SETTINGS = {'text': 'Celsius', 'background': 'white'}
FARENH_LABEL_SETTINGS = {'text': 'Fahrenheit', 'background': 'white'}

FRAME_1_ENTRY_COLOR = 'lightgray'
FRAME_2_ENTRY_COLOR = 'lightgray'

def main() -> None:

	def switch() -> None:
		nonlocal first_frames, second_frames
		for i in second_frames:
			i.tkraise()
		first_frames, second_frames = second_frames, first_frames
		
	def ctoF(*args) -> None:
		if re.match(r'^\d+$',l_input.get()):
			c = float(l_input.get())
			celsius_to_farenh = c * 9 / 5 + 32
			
			f = celsius_to_farenh
			fahrenheit.set(f'{f:.2f}')
		else:
			pass

	def ftoC(*args) -> None:
		if re.match(r'^\d+$',l_input.get()):
			f = float(l_input.get())
			farenh_to_celsius = (f - 32) * 5 / 9
			c = farenh_to_celsius
			celsius2.set(f'{c:.2f}')
		else:
			pass

	def font(**kwargs) -> tuple:
		size = kwargs.get('size', 20)
		font = ('Tahoma', size)
			
		return font
		
	# root window
	root = tk.Tk()

	root.geometry(GEOMETRY)
	root.resizable(False, False)
	root.title(TITLE)

	# app (column, left to right)
	base_img = Image.open(IMAGE)
	resize_img = base_img.resize(IMAGE_SIZE)
	final_img = ImageTk.PhotoImage(resize_img)

	background = tk.Label(root, image=final_img)
	background.place(x=0)

	# frame 1
	f1 = tk.Frame(root, bg = 'white')
	f1.place(relwidth = .35, relheight = 1)

	l1 = tk.Label(f1, font = font(), **CELSIUS_LABEL_SETTINGS) # type: ignore
	l1.place(relx = .5, rely= .1, anchor = tk.CENTER)

	l_input = tk.StringVar()
	l_input.trace_add('write', ctoF)
	e1 = tk.Entry(f1, font = font(), bg = FRAME_1_ENTRY_COLOR, textvariable = l_input)
	e1.place(relx = .5, rely = .2, relwidth = .9, anchor = tk.CENTER)


	b1 = tk.Button(background, text = 'switch', font = font(size = 12), command = switch)
	b1.place(relx = .47, rely = .1, anchor = tk.CENTER)

	f1_2 = tk.Frame(root, bg = 'white')
	f1_2.place(relx = .65, relwidth= .35 , relheight = 1)

	l2 = tk.Label(f1_2, font = font(), **FARENH_LABEL_SETTINGS) # type: ignore
	l2.place(relx = .5, rely = .1, anchor = tk.CENTER)

	fahrenheit = tk.StringVar()
	e2 = tk.Label(f1_2, font = font(), bg = FRAME_1_ENTRY_COLOR, textvariable = fahrenheit)
	e2.place(relx = .5, rely = .2, relwidth = .9, anchor = tk.CENTER)

	# frame 2
	f2 = tk.Frame(root, bg = 'white')
	f2.place(relwidth = .35, relheight = 1)

	l1_2 = tk.Label(f2, font=font(), **FARENH_LABEL_SETTINGS) # type: ignore
	l1_2.place(relx = .5, rely = .1, anchor = tk.CENTER)


	l_input.trace_add('write',ftoC)
	e1_2 = tk.Entry(f2, font = font(), bg = FRAME_2_ENTRY_COLOR, textvariable = l_input)
	e1_2.place(relx = .5, rely = .2, relwidth = .9, anchor = tk.CENTER)

	f2_2 = tk.Frame(root, bg='white')
	f2_2.place(relx = .65, relwidth = .35, relheight = 1)

	l2_2 = tk.Label(f2_2, font=font(), **CELSIUS_LABEL_SETTINGS) # type: ignore
	l2_2.place(relx = .5, rely = .1, anchor = tk.CENTER)

	celsius2 = tk.StringVar()
	e2_2 = tk.Label(f2_2, font = font(), bg = FRAME_2_ENTRY_COLOR,textvariable = celsius2)
	e2_2.place(relx = .5, rely = .2, relwidth = .9, anchor = tk.CENTER)

	first_frames = [f1, f1_2]
	second_frames = [f2, f2_2]

	for i in first_frames:
		i.tkraise()
	# start app
	root.mainloop()

if __name__ == "__main__":
	main()