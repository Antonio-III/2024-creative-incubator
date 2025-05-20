import tkinter 

# Default settings
LABELS = 4
HALF_LABELS = LABELS // 2

GEOMETRY = '600x600'

TITLE = 'GUI pack sample'
BD = 5

LEFT_FRAME_PLACEMENT = {'relw': 0.5, 'relh': 1}
RIGHT_FRAME_PLACEMENT = {'relw': 0.5, 'relh': 1, 'relx': 0.5 }

BLACK_LABELS_INDEX = [0, 3]

BLACK_LABELS_CONFIG = {'bg': 'black', 'fg': 'white'}
BLACK_LABELS_PACKING = {'expand': tkinter.YES, 'fill': tkinter.BOTH, 'anchor': 'n'}

WHITE_LABELS_CONFIG = {'bg': 'white'}
WHITE_LABELS_PACKING = {'expand': tkinter.YES, 'fill': tkinter.BOTH, 'anchor': 's'}

def main() -> None:
	# Create root window
	main = tkinter.Tk()

	# Create window size
	main.geometry(GEOMETRY)

	# Change default title 
	main.title(TITLE)

	# customizable options
	l_preset = {'bg': 'white', 'relief': 'groove'}
	r_preset = {'bg': 'white', 'relief': 'sunken'}

	left_frame = tkinter.Frame(main, bd = BD, **l_preset) # type: ignore
	right_frame = tkinter.Frame(main, bd = BD, **r_preset) # type: ignore

	# Output the frame. Must have set sizes to be visible
	left_frame.place(**LEFT_FRAME_PLACEMENT)
	right_frame.place(**RIGHT_FRAME_PLACEMENT)

	# list to store the 4 labels
	labels=[]

	# loop to create the 4 labels
	for i in range(LABELS):
		# first 2 iterations go to the left frame
		if i < HALF_LABELS: 
			l = tkinter.Label(left_frame)
			labels.append(l)
		else:
			l = tkinter.Label(right_frame)
			labels.append(l)

	# number for increment        
	index=0

	# list for iteration
	letters=['A','B','C','D']

	# customize the labels stored in the 'labels' list
	for label in labels:

		# all labels will have their text from here
		label.configure(text=f'{letters[index]}')
		index += 1

		# set colors of the labels and output them in their correct positions
		if labels.index(label) in BLACK_LABELS_INDEX:
			label.configure(**BLACK_LABELS_CONFIG)
			label.pack(**BLACK_LABELS_PACKING)
		else:
			label.configure(**WHITE_LABELS_CONFIG)
			label.pack(**WHITE_LABELS_PACKING)

	# Start the app. All codes must be before this line
	main.mainloop()

if __name__ == "__main__":
	main()