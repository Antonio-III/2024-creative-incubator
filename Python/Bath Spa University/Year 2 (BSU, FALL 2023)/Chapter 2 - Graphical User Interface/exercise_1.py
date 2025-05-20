# Import module
import tkinter as tk

# Default settings
BG_COLOR = 'lightblue'
FONT = ('Roboto', 25, 'bold')
GEOMETRY = '600x600'
TEXT = 'Welcome to Tkinter'

TEXT_PLACEMENT_X = 0.5
TEXT_PLACEMENT_Y = 0.1
TEXT_ANCHOR = 'center'

def main() -> None:
	# Create an output window
	main = tk.Tk()

	# Set a base window size
	main.geometry(GEOMETRY)

	#(2)
	main.resizable(False, False)

	#(1)
	text = tk.Label(main, text=TEXT, font=FONT, bg=BG_COLOR)

	# Place the label on the app
	text.place(relx= TEXT_PLACEMENT_X, rely=TEXT_PLACEMENT_Y, anchor=TEXT_ANCHOR)

	#(3)
	main['bg'] = BG_COLOR

	# Start the app
	main.mainloop()

if __name__ == "__main__":
	main()