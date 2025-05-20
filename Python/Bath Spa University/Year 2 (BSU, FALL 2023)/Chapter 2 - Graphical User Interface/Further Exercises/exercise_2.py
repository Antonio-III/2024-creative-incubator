import tkinter as tk

# Default settings
FONT = ('Tahoma', 16)
GEOMETRY = '400x400'
HEADING_TEXT = 'Enter string:'
MAX_CHARS = 30
TITLE = 'Capitalize Letters'



def main() -> None:
	def capitalize_string(*strings) -> None:
		nonlocal labels        
		chars = string.get() # get the user input
		max_chars = MAX_CHARS # arbitrary max characters
		
		# list that stores an element up to 33 in length
		wrapper = [chars[i:i + max_chars] for i in range(0, len(chars), max_chars)]

		# destroy every object per  call so that that the labels update in real-time (backspace in input will reflect on output.)
		for i in labels:
			i.destroy()

		increment = 0
		y = .2
		for i in wrapper:
			# since the previous labels are 'destroyed' on the app (list unaffected), we have to reassign them instead of configuring.
			# Referencing elements from 'labels' is just so that we have objects to point to when destroying them again.
			labels[increment] = tk.Label(root, font=font, text = i.upper())
			labels[increment].place(relx = .5, rely = y,anchor = 'n')
			increment += 1
			y += .1

	font = FONT
	root = tk.Tk()
	root.geometry(GEOMETRY)
	root.title(TITLE)

	tk.Label(root, text = HEADING_TEXT, font = font).place(relx = .5, anchor = 'n')

	string = tk.StringVar()
	string.trace_add('write', capitalize_string)
	tk.Entry(root, textvariable = string, font = font).place(relx = .5, rely =.1, anchor = 'n')

	l1 = tk.Label(root, font = font)
	l2 = tk.Label(root, font = font)
	l3 = tk.Label(root, font = font)
	l4 = tk.Label(root, font = font)
	l5 = tk.Label(root, font = font)
	l6 = tk.Label(root, font = font)
	l7 = tk.Label(root, font = font)
	l8 = tk.Label(root, font = font)
	l9 = tk.Label(root, font = font)
	l10 = tk.Label(root, font = font)

	# these need to be objects because we will destroy and recreate them on function calls. Basically working in the same memory address instead of pointing to new ones.
	labels=[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]

	root.mainloop()
	
if __name__ == "__main__":
	main()