from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle
global globalfilename
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
	activestyle="none",





	)
my_list.pack(side=LEFT, fill=BOTH)
#Create dummy list

#stuff = ['Yeet', 'nan', 'pog', 'ur nan', 'e', 'f', 'x']
#Add dummy list to list box

#for item in stuff:
	#my_list.insert(END, item)








#Scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)
#Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# Create entry box to add items
my_entry = Entry(root, font=("Helvetica", 24), width=26)
my_entry.pack(pady=20)

#Create a button frame

button_frame = Frame(root)
button_frame.pack(pady=20)

#functions
globalfilename = ""
def delete_item(event):
	my_list.delete(ANCHOR)
	global globalfilename
	if not globalfilename == "":
		print('fail')
		file_name = globalfilename
		if file_name:
			if file_name.endswith(".dat"):
				pass
			else:
				file_name = f'{file_name}.dat'
			#delete crossed items before saving
			count = 0
			while count < my_list.size():
				if my_list.itemcget(count, "fg") == "#dedede":
					my_list.delete(my_list.index(count))
				else:
					count += 1
			#grab all the stuff from the list
			stuff = my_list.get(0, END)


			#open file
			output_file = open(file_name, 'wb')

			#actually add the stuff to the file
			pickle.dump(stuff, output_file)
		




	else:
		pass

def delete_item_button():
	my_list.delete(ANCHOR)
	global globalfilename
	if not globalfilename == "":
		print('fail')
		file_name = globalfilename
		if file_name:
			if file_name.endswith(".dat"):
				pass
			else:
				file_name = f'{file_name}.dat'
			#delete crossed items before saving
			count = 0
			while count < my_list.size():
				if my_list.itemcget(count, "fg") == "#dedede":
					my_list.delete(my_list.index(count))
				else:
					count += 1
			#grab all the stuff from the list
			stuff = my_list.get(0, END)


			#open file
			output_file = open(file_name, 'wb')

			#actually add the stuff to the file
			pickle.dump(stuff, output_file)
		




	else:
		pass

def add_item_button():
	my_list.insert(END, my_entry.get())
	my_entry.delete(0, END)
	global globalfilename
	if not globalfilename == "":
		print('fail')
		file_name = globalfilename
		if file_name:
			if file_name.endswith(".dat"):
				pass
			else:
				file_name = f'{file_name}.dat'
			#delete crossed items before saving
			count = 0
			while count < my_list.size():
				if my_list.itemcget(count, "fg") == "#dedede":
					my_list.delete(my_list.index(count))
				else:
					count += 1
			#grab all the stuff from the list
			stuff = my_list.get(0, END)


			#open file
			output_file = open(file_name, 'wb')

			#actually add the stuff to the file
			pickle.dump(stuff, output_file)
		




	else:
		pass

def cross_off_button():
	my_list.itemconfig(
		my_list.curselection(),
		fg="#dedede")	
	#Get rid of selection bar
	my_list.selection_clear(0, END)
		
def uncross_off():
	my_list.itemconfig(
		my_list.curselection(),
		fg="#464646")	
	#Get rid of selection bar
	my_list.selection_clear(0, END)
	global globalfilename
	if not globalfilename == "":
		print('fail')
		file_name = globalfilename
		if file_name:
			if file_name.endswith(".dat"):
				pass
			else:
				file_name = f'{file_name}.dat'
			#delete crossed items before saving
			count = 0
			while count < my_list.size():
				if my_list.itemcget(count, "fg") == "#dedede":
					my_list.delete(my_list.index(count))
				else:
					count += 1
			#grab all the stuff from the list
			stuff = my_list.get(0, END)


			#open file
			output_file = open(file_name, 'wb')

			#actually add the stuff to the file
			pickle.dump(stuff, output_file)
		




		else:
			pass

def delete_crossed(event):
	count = 0
	while count < my_list.size():
		if my_list.itemcget(count, "fg") == "#dedede":
			my_list.delete(my_list.index(count))
		else:
			count += 1
		global globalfilename
		if not globalfilename == "":
			print('fail')
			file_name = globalfilename
			if file_name:
				if file_name.endswith(".dat"):
					pass
				else:
					file_name = f'{file_name}.dat'
				#delete crossed items before saving
				count = 0
				while count < my_list.size():
					if my_list.itemcget(count, "fg") == "#dedede":
						my_list.delete(my_list.index(count))
					else:
						count += 1
				#grab all the stuff from the list
				stuff = my_list.get(0, END)


				#open file
				output_file = open(file_name, 'wb')

				#actually add the stuff to the file
				pickle.dump(stuff, output_file)
			




		else:
			pass
def cross_off(event):
	my_list.itemconfig(
		my_list.curselection(),
		fg="#dedede")	
	#Get rid of selection bar
	my_list.selection_clear(0, END)

def add_item(event):
	entry_data = (my_entry.get())
	
	if not len(entry_data) == 0:
		add_item_button()
		global globalfilename
		if not globalfilename == "":
			print('fail')
			file_name = globalfilename
			if file_name:
				if file_name.endswith(".dat"):
					pass
				else:
					file_name = f'{file_name}.dat'
				#delete crossed items before saving
				count = 0
				while count < my_list.size():
					if my_list.itemcget(count, "fg") == "#dedede":
						my_list.delete(my_list.index(count))
					else:
						count += 1
				#grab all the stuff from the list
				stuff = my_list.get(0, END)


				#open file
				output_file = open(file_name, 'wb')

				#actually add the stuff to the file
				pickle.dump(stuff, output_file)
			




		else:
			pass

	else:
		pass
def delete_crossed_button():
	count = 0
	while count < my_list.size():
		if my_list.itemcget(count, "fg") == "#dedede":
			my_list.delete(my_list.index(count))
		else:
			count += 1
		global globalfilename
		if not globalfilename == "":
			print('fail')
			file_name = globalfilename
			if file_name:
				if file_name.endswith(".dat"):
					pass
				else:
					file_name = f'{file_name}.dat'
				#delete crossed items before saving
				count = 0
				while count < my_list.size():
					if my_list.itemcget(count, "fg") == "#dedede":
						my_list.delete(my_list.index(count))
					else:
						count += 1
				#grab all the stuff from the list
				stuff = my_list.get(0, END)


				#open file
				output_file = open(file_name, 'wb')

				#actually add the stuff to the file
				pickle.dump(stuff, output_file)
			




		else:
			pass

def save_list_button():
	global globalfilename
	if not globalfilename == "":
		print('fail')
		file_name = globalfilename
		if file_name:
			if file_name.endswith(".dat"):
				pass
			else:
				file_name = f'{file_name}.dat'
			#delete crossed items before saving
			count = 0
			while count < my_list.size():
				if my_list.itemcget(count, "fg") == "#dedede":
					my_list.delete(my_list.index(count))
				else:
					count += 1
			#grab all the stuff from the list
			stuff = my_list.get(0, END)


			#open file
			output_file = open(file_name, 'wb')

			#actually add the stuff to the file
			pickle.dump(stuff, output_file)
		




	else:
		file_name = filedialog.asksaveasfilename(
			initialdir = ("C:/Users/1210/OneDrive - RGS LPS/Documents/Frequent/Coding/ToDoList/Data"),
			title="Save File",
			filetypes=(("Dat Files", "*.dat",),
						("All Files", "*.*"))
			)
		if file_name:
			if file_name.endswith(".dat"):
				pass
			else:
				file_name = f'{file_name}.dat'
			#delete crossed items before saving
			count = 0
			while count < my_list.size():
				if my_list.itemcget(count, "fg") == "#dedede":
					my_list.delete(my_list.index(count))
				else:
					count += 1
			#grab all the stuff from the list
			stuff = my_list.get(0, END)


			#open file
			output_file = open(file_name, 'wb')

			#actually add the stuff to the file
			pickle.dump(stuff, output_file)
			 
			
			globalfilename = file_name
	

def save_list(event):
	global globalfilename
	if not globalfilename:
		file_name = globalfilename
		if file_name:
			if file_name.endswith(".dat"):
				pass
			else:
				file_name = f'{file_name}.dat'
			#delete crossed items before saving
			count = 0
			while count < my_list.size():
				if my_list.itemcget(count, "fg") == "#dedede":
					my_list.delete(my_list.index(count))
				else:
					count += 1
			#grab all the stuff from the list
			stuff = my_list.get(0, END)


			#open file
			output_file = open(file_name, 'wb')

			#actually add the stuff to the file
			pickle.dump(stuff, output_file)
		




	else:
		file_name = filedialog.asksaveasfilename(
			initialdir = ("C:/Users/1210/OneDrive - RGS LPS/Documents/Frequent/Coding/ToDoList/Data"),
			title="Save File",
			filetypes=(("Dat Files", "*.dat",),
						("All Files", "*.*"))
			)
		if file_name:
			if file_name.endswith(".dat"):
				pass
			else:
				file_name = f'{file_name}.dat'
			#delete crossed items before saving
			count = 0
			while count < my_list.size():
				if my_list.itemcget(count, "fg") == "#dedede":
					my_list.delete(my_list.index(count))
				else:
					count += 1
			#grab all the stuff from the list
			stuff = my_list.get(0, END)


			#open file
			output_file = open(file_name, 'wb')

			#actually add the stuff to the file
			pickle.dump(stuff, output_file)
			 

			globalfilename = file_name









					
	

def open_list(event):
	file_name = filedialog.askopenfilename(	initialdir = ("C:/Users/1210/OneDrive - RGS LPS/Documents/Frequent/Coding/ToDoList/Data"),
		title="Save File",
		filetypes=(("Dat Files", "*.dat",),
					("All Files", "*.*")))

	if file_name:
		#delete current list
		my_list.delete(0, END)


		#open file
		input_file = open(file_name, 'rb')

		#load data
		stuff = pickle.load(input_file)

		#output data to the sreen

		for item in stuff:
			my_list.insert(END, item)



def open_list_button():
	file_name = filedialog.askopenfilename(	initialdir = ("C:/Users/1210/OneDrive - RGS LPS/Documents/Frequent/Coding/ToDoList/Data"),
		title="Save File",
		filetypes=(("Dat Files", "*.dat",),
					("All Files", "*.*")))

	if file_name:
		#delete current list
		my_list.delete(0, END)


		#open file
		input_file = open(file_name, 'rb')

		#load data
		stuff = pickle.load(input_file)

		#output data to the sreen

		for item in stuff:
			my_list.insert(END, item)

def clear_list():
	my_list.delete(0, END)
	global globalfilename
	if not globalfilename == "":
		print('fail')
		file_name = globalfilename
		if file_name:
			if file_name.endswith(".dat"):
				pass
			else:
				file_name = f'{file_name}.dat'
			#delete crossed items before saving
			count = 0
			while count < my_list.size():
				if my_list.itemcget(count, "fg") == "#dedede":
					my_list.delete(my_list.index(count))
				else:
					count += 1
			#grab all the stuff from the list
			stuff = my_list.get(0, END)


			#open file
			output_file = open(file_name, 'wb')

			#actually add the stuff to the file
			pickle.dump(stuff, output_file)
		




	else:
		pass

#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)


#ad items to menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
#add dropdowns
file_menu.add_command(label="Save List", command=save_list_button)
file_menu.add_command(label="Open List", command=open_list_button)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=clear_list)


	

		
	

#Keybinds
root.bind('<Return>', add_item)
root.bind('<BackSpace>', delete_item)
root.bind('<Shift_L>', cross_off)
root.bind('<Delete>', delete_crossed)
root.bind('<Control-o>', open_list)

root.bind('<Control-Shift-S>', save_list)




	

	



   
	


   




#add buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item_button)
add_button = Button(button_frame, text="Add Item", command=add_item_button)
cross_off_button = Button(button_frame, text="Cross Item", command=cross_off_button)
uncross_off_button = Button(button_frame, text="Uncross Item ", command=uncross_off)
delete_crossed_button = Button(button_frame, text="Delete Crossed ", command=delete_crossed_button)

delete_button.grid(row=0, column=1, padx=20)
add_button.grid(row=0, column=0, )
cross_off_button.grid(row=0, column=2)
uncross_off_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4, )





root.mainloop()