import tkinter as tk
from PIL import ImageTk,Image
import datetime

AGE_MESSAGE = 'You are {age} years old'
LABEL_BG = 'white'
ENTRY_BG = 'lightgrey'

FONT = ('Tahoma',16)
GEOMETRY = '400x400'

IMAGE = 'Images/cake-logo-vector-25934828.jpg'
IMAGE_SIZE = (400,400)

TITLE = 'Age calculator'

def main() -> None:
	def message(*args):
		nonlocal date, month, year, l4, root
		test = [len(date.get()),len(month.get()),len(year.get())]
		if 0 in test:
			pass
		else: 
			today=datetime.datetime.now()
			
			today_month_date = (f'{today.month:02}',f'{today.day:02}')
			birthday_month_date = (f'{int(month.get()):02}',f'{int(date.get()):02}')

			age = int(today.year) - int(year.get())
			if str(today_month_date) < str(birthday_month_date):
				age-=1

			# remove any previously-defined l4 widget. This is because we are creating a new one.
			# Everytime this code block runs (inside 'else'), it removes an l4 that could have been created by this function previously.
			l4.destroy()
			l4 = tk.Label(root, font = font, bg = LABEL_BG, text = AGE_MESSAGE.format(age = age))
			l4.place(relx = .5, rely = .4, anchor = tk.CENTER)

	font = FONT
	
	root = tk.Tk()	

	date = tk.StringVar()
	month = tk.StringVar()
	year = tk.StringVar()

	root.title(TITLE)
	root.geometry(GEOMETRY)

	try:
		base_img = Image.open(IMAGE)
	except (FileNotFoundError):
		print("Cannot run app. You need to have a cake image downloaded and put its directory on the IMAGE variable, else the app will not work.")
		
		return None
	
	resize_img = base_img.resize(IMAGE_SIZE)
	final_img = ImageTk.PhotoImage(resize_img)

	bg = tk.Label(root, image = final_img)
	bg.place(relx = 0)

	l1 = tk.Label(root, font = font, text = 'Date', bg = LABEL_BG)
	l1.place(relx = .1, rely = .1)

	e1 = tk.Entry(root, font = font, textvariable = date, bg = ENTRY_BG)
	e1.place(relx = .07, rely = .2, relwidth = .2)
	date.trace_add('write', message)

	l2 = tk.Label(root, font = font, text = 'Month', bg = LABEL_BG)
	l2.place(relx = .4,rely = .1)

	e2 = tk.Entry(root, font = font, textvariable = month, bg = ENTRY_BG)
	e2.place(relx = .39, rely = .2, relwidth = .2)
	month.trace_add('write', message)

	l3=tk.Label(root, font = font, text = 'Year', bg = LABEL_BG)
	l3.place(relx = .7, rely = .1)

	e3=tk.Entry(root, font = font, textvariable = year, bg = ENTRY_BG)
	e3.place(relx= .67, rely = .2, relwidth = .2)
	year.trace_add('write', message)

	# define l4 to be so the function runs properly
	l4 = tk.Label(bg)
	
	root.mainloop()

if __name__ == "__main__":
	main()