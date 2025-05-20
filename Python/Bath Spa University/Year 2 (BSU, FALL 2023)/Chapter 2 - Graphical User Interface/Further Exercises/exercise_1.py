import tkinter as tk

# Default settings
FONT = ('Tahoma', 16)
GEOMETRY = '400x400'
HEADING_TEXT = 'Enter a string'
TITLE = 'Count char'

def main() -> None:

	def output(*args) -> None:
		nonlocal l_list, font
		
		alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		vowels = ['a', 'e', 'i', 'o', 'u']
		
		l_count = 0
		v_count = 0
		c_count = 0
		s_count = 0
		
		for i in string_id.get():
			char = i.lower()
			if char in alphabet:
				l_count += 1
				if char in vowels:
					v_count += 1
				elif char not in vowels:
					c_count += 1
			else:
				s_count += 1

		counts = [l_count, v_count, c_count, s_count]
		
		string_n = ['Letter', 'Vowel', 'Consonant', 'Special Character']
		
		y = [.25, .35, .45, .55]
		
		increment = 0
		for i in l_list:
			i.destroy()
			
		l_list.clear()
		
		for i in range(len(string_n)):
			i = tk.Label(root, text = f'{string_n[increment]} count: {counts[increment]}', font = font)
			i.place(relx = .5, rely = y[increment], anchor = tk.CENTER)
			l_list.append(i)
			
			increment+=1
			
	font = FONT

	root = tk.Tk()

	root.title(TITLE)
	root.geometry(GEOMETRY)

	tk.Label(root, text = HEADING_TEXT, font = font).place(relx = .5, anchor = 'n')

	string_id=tk.StringVar()

	e1=tk.Entry(root, textvariable = string_id, font = font)
	e1.place(relx = .5 ,rely = .15, anchor = tk.CENTER)
	string_id.trace_add('write', output)

	l1 = tk.Label(root)
	l2 = tk.Label(root)
	l3 = tk.Label(root)
	l4 = tk.Label(root)

	l_list=[l1, l2, l3, l4]

	root.mainloop()

if __name__ == "__main__":
	main()