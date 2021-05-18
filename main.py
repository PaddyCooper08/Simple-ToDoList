from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('ToDo List')
root.geometry("500x500")

#Define font
my_font = Font(
	family="Caveat",
	size=25,
	weight='normal')

#Create frame
my_frame = Frame(root)
my_frame.pack(pady=10)
#Create listbox
my_list = Listbox(my_frame,
	font=my_font,
	width=30,
	height=5,
	bg="SystemButtonFace",
	bd=0,
	fg="#464646",
	highlightthickness=0,
	selectbackground="#a6a6a6",
	activestyle="none"




	)
my_list.pack(side=LEFT, fill=BOTH)
#Create dummy list

stuff = ['Yeet', 'nan', 'pog', 'ur nan', 'e', 'f', 'x']
#Add dummy list to list box

for item in stuff:
	my_list.insert(END, item)

#functions
def delete_item():
	my_list.delete(ANCHOR)

def add_item():
	my_list.insert(END, my_entry.get())
	my_entry.delete(0, END)
def cross_off():
	pass
def uncross_off():
	pass







#Scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)
#Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# Create entry box to add items
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

#Create a button frame

button_frame = Frame(root)
button_frame.pack(pady=20)


#add buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off)
uncross_off_button = Button(button_frame, text="Uncross Item ", command=uncross_off)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_off_button.grid(row=0, column=3, padx=20)






root.mainloop()
