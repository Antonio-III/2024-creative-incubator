import tkinter as tk

# Default settings
GEOMETRY = '370x600'
TITLE = 'Calculator'
SCREEN_SETTINGS = {'bg': 'white','height': 5, 'font': ('Tahoma', 12, 'bold')}
KEY_DIMENSIONS = {'width': 12, 'height': 6}
CLEAR_SYMBOL = 'C'
EQUAL_SYMBOL = '='

ONE = 1
SYMBOLS_AMOUNT = 3

def main() -> None:
# root window
	root = tk.Tk()
	root.geometry(GEOMETRY)
	root.title(TITLE)
	root.resizable(False, False)

	def onclick(character) -> None:
		current_text = screen.cget('text')
		screen.configure(text = current_text + str(character))
		
		print(screen.cget('text'))
		print(type(screen.cget('text')))

	def calculate(expression: str) -> None:
		output = str(eval(expression))
		screen.configure(text = output)
		
		print(screen.cget('text'))
		print(type(screen.cget('text')))

	def clear() -> None:
		screen.configure(text = '')

	# app (grid starts at 0)

	# screen of the calc
	screen=tk.Label(root,**SCREEN_SETTINGS)
	screen.grid(row=0, columnspan=4, sticky='we')

	# var here for iteration purposes
	n=0

	# 2 different lists to be iterated separately 
	symbols = ['+', '-', '*', '/']
	symbols_2 = ['9', '%', '/']

	# these will be the 3x3 from numbers 0 to 8
	for x in range(ONE, SYMBOLS_AMOUNT + ONE):
		for y in range(SYMBOLS_AMOUNT):
			# we need to store in a lambda because it is an iteration, all the values will be on the latest iteration, so we need a lambda variable to snapshot the current iteration
			tk.Button(root, text = str(n), command = lambda a = n: onclick(a), **KEY_DIMENSIONS).grid(row = x, column = y) # type: ignore
			n += 1
	# var here to iterate through indexes
	i = 0

	# this will be the loop for the operator symbols
	for x in range(ONE, SYMBOLS_AMOUNT + ONE):
		tk.Button(root, text = symbols[i], command = lambda a = symbols[i]: onclick(a)).grid(row = x, column = 3)
		i += 1 # increment by 1, so it will go through a different elements
		
	# reset to zero for the code below
	i = 0

	# loop for the remaining symbols
	for y in range(SYMBOLS_AMOUNT):
		tk.Button(root, text = symbols_2[i], command = lambda a = symbols_2[i]: onclick(a), **KEY_DIMENSIONS).grid(row = 4, column = y) # type: ignore
		i += 1

	# these two are not included in the loop because of their command attribute
	tk.Button(root, text = CLEAR_SYMBOL, command = clear, **KEY_DIMENSIONS).grid(row = 5) # type: ignore
	tk.Button(root, text = EQUAL_SYMBOL, command = lambda: calculate(screen.cget('text')), **KEY_DIMENSIONS).grid(row = 4, column = 3) # type: ignore

	# start app
	root.mainloop()

if __name__ == "__main__":
	main()