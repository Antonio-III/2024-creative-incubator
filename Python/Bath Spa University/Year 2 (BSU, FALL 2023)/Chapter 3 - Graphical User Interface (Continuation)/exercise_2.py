import tkinter as tk
from tkinter import ttk,messagebox
from PIL import ImageTk,Image

# Default settings
GEOMETRY='550x450'

TITLE='Cofee Vending Machine'
# Images must be named the same as the values in COFFEES. Ex: 'americano.jpg', 'black.jpg'
IMAGES_DIR='Images/{}.jpg' 

FONT=('Tahoma',16)

COFFEES=['americano','black','cappucino','espresso','latte','irish']
COFFEES_IMAGE_SIZE=(110,140)

COINS_TEXT='Coins: ${}'
COST_TEXT='Cost: ${}'

CONDIMENT_1_TEXT='Sugar: {}'
CONDIMENT_2_TEXT='Milk: {}'

COLLECT_BUTTON_TEXT='Collect'
SELECTED_TEXT='Selected:'

ERROR_TITLE='Error'
ERROR_TEXT_COFFEE='No coffee selected'
ERROR_TEXT_PURCHASE='Not enough funds'
INSERT_COIN_TEXT='Insert Coin'

SUCCESS_PURCHASE_TITLE='Success'
SUCCESS_PURCHASE_MESSAGE='You bought: {coffee} Coffee. With {sugar} spoon of sugar and {milk} spoon of milk. ${cost} was deducted to your balance.'

ON_SELECT_COLOR='red'
VENDING_MACHINE_COLOR='red'
INSERT_COIN_COLORS={'bg':'yellow','fg':'black'}
COST_LABEL_COLORS={'bg':'red','fg':'antiquewhite2'}
COLLECT_BUTTON_COLORS={'bg':'black','fg':'antiquewhite2'}


def main() -> None:
	root=tk.Tk()

	# All of these vars are global because they will be present in more than 1 function. Or they're reused.
	# because I don't like writing the tuple again and again
	font=FONT

	# variable to hold values of the sliders
	sugar_v=tk.IntVar()
	milk_v=tk.IntVar()

	deposit_v=tk.IntVar()

	# user's money. global because we need a counter for the amount of money the user has deposited, and it has to interact with different functions
	coin=0

	coffee=COFFEES

	# list of coffee images. global to prevent garbage collection and since we'll use it again
	l=[]

	# counter for cost. global because it interacts with at least 2 functions
	cost=0

	# gatekeep certain function codes unless set to True
	select_coffee=False

	# Snapshot price of coffee only
	c_cost=0

	# tracks the index value of the pressed coffee
	tracker=0


	def create_coffees():
		nonlocal coffee,l
		x=0
		y=0
		increment=0
		for i in coffee:
			base=Image.open(IMAGES_DIR.format(i))
			resize=base.resize(COFFEES_IMAGE_SIZE)
			img=ImageTk.PhotoImage(resize)
			l.append(img)
			button=tk.Button(root,image=l[increment], command= lambda index=increment: on_select_coffee(index),bg=ON_SELECT_COLOR)
			# prevent garbace collection by a var attaching to an object. This is because objects don't get their space in memory removed like function-defined variables (maybe???)
			# button.dont_garbagecollect=l[increment] . REMOVED BECAUSE 'l' is now global
			
			button.place(x=x,y=y)
			x+=115
			increment+=1
			if i==coffee[2]:
				x=0
				y+=145
				
	def on_slide(event):
		nonlocal select_coffee,sugar_v,milk_v,sugar_c, milk_c,cost,coffee_c,c_cost
		if select_coffee==True:
			# get sugar and milk values
			sugar=sugar_v.get()
			milk=milk_v.get()
			# update slider values to reflect changes
			sugar_c.configure(text=CONDIMENT_1_TEXT.format(sugar))
			milk_c.configure(text=CONDIMENT_2_TEXT.format(milk))
			
			# update cost. Disregard the previous 'cost' amount when using sliders because using it here will make the price stack indefinitely, so we use the snapshot instead
			price_calculation=sugar+(milk*2)+c_cost
			cost=price_calculation
			# update 'cost' text to reflect changes
			coffee_c.configure(text=COST_TEXT.format(cost))

		else:
			messagebox.showerror(ERROR_TITLE,ERROR_TEXT_COFFEE)
				
	def on_slide_c(event):
		nonlocal deposit_c,deposit_v
		# update values
		deposit_c.configure(text=deposit_v.get())

	def deposit_coin():
		nonlocal deposit_v,coin,usable_coin
		
		added_coin=deposit_v.get()
		# increase money count
		coin+=int(added_coin)
		# update text to reflect changes
		usable_coin.configure(text=COINS_TEXT.format(coin))

	def on_select_coffee(coffee):
		nonlocal l, c_cost, select_coffee,tracker,cost
		
		# Show display item
		selected_coffee.configure(image=l[coffee])
		
		# This var serves as a snapshot of the coffee cost itself
		c_cost= 0+coffee+1
		# 'cost' will update
		cost=c_cost
		
		# reflect changes
		coffee_c.configure(text=COST_TEXT.format(cost))
		
		# condition to track if the user has called this function (ie pressed one of the coffees)
		select_coffee=True

		# pass a value that represents one of the index position of 'l'. This is so that a function-defined var can become global
		tracker=coffee
		
	def buy_coffee():
		nonlocal select_coffee,coin,cost,tracker,usable_coin,sugar_v,milk_v
		sugar=sugar_v.get()
		milk=milk_v.get()
		if select_coffee==True:
			if coin>=cost:
				# transaction
				coin-=cost
				# transaction success
				messagebox.showinfo(SUCCESS_PURCHASE_TITLE,SUCCESS_PURCHASE_MESSAGE.format(coffee=coffee[tracker].title(),sugar=sugar,milk=milk,cost=cost))
				# update coin GUI
				usable_coin.configure(text=COINS_TEXT.format(coin))
			else:
				messagebox.showerror(ERROR_TITLE,ERROR_TEXT_PURCHASE)
			
	root.geometry(GEOMETRY)
	root.title(TITLE)
	root.resizable(False, False)
	# frame (vending machine bg)
	frame=tk.Frame(root,bg=VENDING_MACHINE_COLOR)
	frame.place(width=350,relheight=1)

	# coffee items
	create_coffees()

	# selected
	tk.Label(root,text=SELECTED_TEXT,font=font).place(x=390)
	selected_coffee=tk.Label(root)
	selected_coffee.place(x=390,rely=.1)

	# options (right-side)
	sugar_c=tk.Label(root,text=CONDIMENT_1_TEXT.format(sugar_v.get()),font=font)
	sugar_c.place(x=350,rely=.5)

	ttk.Scale(root,from_=0, to=10,variable=sugar_v,command=on_slide).place(x=450,rely=.5)

	milk_c=tk.Label(root,text=CONDIMENT_2_TEXT.format(milk_v.get()),font=font)
	milk_c.place(x=350,rely=.6)

	ttk.Scale(root,from_=0, to=10,variable=milk_v,command=on_slide).place(x=450,rely=.6)

	# currency
	# coins:0
	usable_coin= tk.Label(root,text=COINS_TEXT.format(coin),font=font)
	usable_coin.place(x=350,rely=.7)

	# 0 on left of slider
	deposit_c=tk.Label(root,text=deposit_v.get(),font=font)
	deposit_c.place(x=360,rely=.80)

	# slider
	ttk.Scale(root,from_=0,to=100,variable=deposit_v,command =on_slide_c).place(x=400,rely=.8)

	tk.Button(root,text=INSERT_COIN_TEXT,font=font,command=deposit_coin,**INSERT_COIN_COLORS).place(x=350,rely=.9,width=200) # type: ignore

	# collect coffee
	coffee_c=tk.Label(frame,text=COST_TEXT.format(cost),font=font,**COST_LABEL_COLORS) # type: ignore
	coffee_c.place(relx=.4,rely=.65)

	tk.Button(frame,text=COLLECT_BUTTON_TEXT,font=font,command=buy_coffee,**COLLECT_BUTTON_COLORS).place(x=0,rely=.75,relwidth=1,relheight=.25) # type: ignore

	root.mainloop()

if __name__ == "__main__":
	main()