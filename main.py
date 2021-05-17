from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('ToDo List')
root.geometry("500x500")

#Define font
my_font = Font(
	family="Caveat",
	size=30,
	weight='normal')

#Create frame
my_frame = Frame(root)
my_frame.pack(pady=10)
#Create listbox
my_list = Listbox(my_frame,
	font=my_font,
	width=25,
	height=5,
	bg="SystemButtonFace",
	bd=0,
	fg="#464646",
	highlightthickness=0,
	selectbackground="#a6a6a6",
	activestyle="none"




	)
my_list.pack()
#Create dummy list

stuff = ['Yeet', 'nan', 'pog', 'ur nan']
#Add dummy list to list box

for item in stuff:
	my_list.insert(END, item)


root.mainloop()
