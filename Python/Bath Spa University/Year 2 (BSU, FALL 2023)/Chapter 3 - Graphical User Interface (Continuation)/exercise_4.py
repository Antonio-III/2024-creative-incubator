import tkinter as tk


# Default settings
FONT=('Tahoma',16)
TITLE='Draw Shape'
GEOMETRY='400x400'

CLEAR_KEY='<Key-c>' # Corresponds to C on the keyboard
PLACE_SHAPE_KEY='<Button-1>'# Corresponds to left mouse button on mouse

CANVAS_BG='black'

OVAL_OUTLINE='red'
OVAL_FILL='red'

RECT_OUTLINE='blue'
RECT_FILL='blue'

SQUARE_OUTLINE='green'
SQUARE_FILL='green'

TRIANGLE_OUTLINE='yellow'
TRIANGLE_FILL='yellow'

def main() -> None:
    root=tk.Tk()
    def place_shape(mousepos) -> None:
        nonlocal canvas,created_shapes
        x,y=mousepos.x,mousepos.y
        
        c_shape = 0

        if active_shape == 'oval':
            c_shape = canvas.create_oval(x,y,x+70,y+50,fill=OVAL_FILL,outline=OVAL_OUTLINE,width=5)
        elif active_shape == 'rectangle':
            c_shape=canvas.create_rectangle(x,y,x+70,y+50,fill=RECT_FILL,outline=RECT_OUTLINE,width=5)
        elif active_shape == 'square':
            c_shape=canvas.create_rectangle(x,y,x+50,y+50,fill=SQUARE_FILL,outline=SQUARE_OUTLINE,width=5)
        elif active_shape == 'triangle':
            points=[x,y,x-20,y+40,x+20,y+40]
            c_shape = canvas.create_polygon(points,fill=TRIANGLE_FILL,outline=TRIANGLE_OUTLINE,width=5)
            
        created_shapes.append(c_shape) 
        
    def change_shape(new_shape) -> None:
        nonlocal active_shape
        active_shape=new_shape

    def clear(*args) -> None:
        nonlocal created_shapes
        
        for i in created_shapes:
            canvas.delete(i)
            
        if len(created_shapes)>0:
            created_shapes.clear()
    font=FONT
    root.title(TITLE)
    root.geometry(GEOMETRY)


    options=tk.Frame(root,bg='white')
    options.place(relwidth=1,relheight=.1)

    # oval, rectangle, square, triangle
    # (root,from_,to,bg,fg,font,text,command)
    oval_b=tk.Button(options,font=font,text='oval',command=lambda:change_shape('oval'))
    oval_b.place(relwidth=.25)

    rectangle_b=tk.Button(options,font=font,text='rectangle',command=lambda:change_shape('rectangle'))
    rectangle_b.place(relx=.25,relwidth=.25)

    square_b=tk.Button(options,font=font,text='square',command=lambda:change_shape('square'))
    square_b.place(relx=.5,relwidth=.25)

    triangle_b=tk.Button(options,font=font,text='triangle',command=lambda:change_shape('triangle'))
    triangle_b.place(relx=.75,relwidth=.25)

    canvas=tk.Canvas(root,bg=CANVAS_BG)
    canvas.place(y=40,relwidth=1,relheight=1)


    canvas.bind(PLACE_SHAPE_KEY,place_shape)
    root.bind(CLEAR_KEY,clear)

    active_shape='oval'
    created_shapes=[]
    root.mainloop()

if __name__ == "__main__":
	main()