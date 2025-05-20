import tkinter as tk

# Default settings
GEOMETRY = '600x600'
TITLE = 'Ex03 - Login Page'

LABEL_TEXT_1 = 'Username: '
LABEL_TEXT_2 = 'Password: '
BUTTON_TEXT = 'Login'

BUTTON_PLACEMENT = {'sticky': 'e', 'row': 3, 'column': 1}

ENTRY_1_PLACEMENT = {'column': 1, 'row': 0}
ENTRY_2_PLACEMENT = {'row': 1, 'column': 1}

LABEL_2_PLACEMENT = {'row': 1}

def main() -> None:
	# create an output window
	main = tk.Tk()

	# set title
	main.title(TITLE)

	# set base window size
	main.geometry(GEOMETRY)

	# row 1
	tk.Label(main, text = LABEL_TEXT_1).grid()

	# specify row else it will be placed in {previous widget's row} + 1. doesn't apply to columns ???
	tk.Entry(main).grid(**ENTRY_1_PLACEMENT) # type: ignore

	# row 2
	tk.Label(main, text = LABEL_TEXT_2).grid(**LABEL_2_PLACEMENT) # type: ignore

	tk.Entry(main).grid(**ENTRY_2_PLACEMENT) # type: ignore

	# row 3
	# grid has sticky intead of anchor
	tk.Button(main, text=BUTTON_TEXT).grid(**BUTTON_PLACEMENT)

	# start the app
	main.mainloop()

if __name__ == "__main__":
	main()