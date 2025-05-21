import matplotlib.pyplot as plt


LINE=[(1,2),(6,8)]
DOTTED_DIAGRAM=[(1, 3) ,(2, 8), (6, 1) , (8, 10)]

def main()->None:
    target_one=LINE
    x_one=[tuple_elem for list_elem in target_one for tuple_elem in list_elem if list_elem.index(tuple_elem)==0]
    y_one=[tuple_elem for list_elem in target_one for tuple_elem in list_elem if list_elem.index(tuple_elem)==1]
    plt.plot(x_one,y_one)

    target_two=DOTTED_DIAGRAM
    x_two=[tuple_elem for list_elem in target_two for tuple_elem in list_elem if list_elem.index(tuple_elem)==0]
    y_two=[tuple_elem for list_elem in target_two for tuple_elem in list_elem if list_elem.index(tuple_elem)==1]
    plt.plot(x_two,y_two,marker='o')

    plt.show()

if __name__ == "__main__":
	main()