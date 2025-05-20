# Create a GUI with 4 labels using the pack() geometry as shown in the below images. The first image on the left shows the original display and the second image on right shows what happens when the window is resized.

# Import tkinter module
import tkinter

# Default settings
GEOMETRY = '600x600'

LABELS_BG = ['red', 'yellow', 'blue', 'white']
LABELS_TEXT = ['A', 'B', 'C', 'D']
LABELS_WIDTH = 20

def main() -> None:
	# Create an output window
	root= tkinter.Tk()

	# Set a base resize window
	root.geometry(GEOMETRY)

	# Create the labels
	letter_A=tkinter.Label(root, text = LABELS_TEXT[0], bg = LABELS_BG[0], relief= tkinter.GROOVE)
	letter_B=tkinter.Label(root, text = LABELS_TEXT[1], bg = LABELS_BG[1], width = LABELS_WIDTH, relief = tkinter.RAISED)
	letter_C=tkinter.Label(root, text = LABELS_TEXT[2], bg = LABELS_BG[2], width = LABELS_WIDTH)
	letter_D=tkinter.Label(root, text = LABELS_TEXT[3], bg = LABELS_BG[3], width = LABELS_WIDTH)

	# Output the labels
	# 'anchor' default: 'center' after applying 'side'
	letter_A.pack(side=tkinter.TOP, fill = tkinter.X, expand = tkinter.YES)

	letter_B.pack(side=tkinter.BOTTOM)

	letter_C.pack(side = tkinter.LEFT,expand=tkinter.YES)

	letter_D.pack(side=tkinter.RIGHT)
	# Start the app
	root.mainloop()

if __name__ == "__main__":
	main()