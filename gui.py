import tkinter as T
import add as A
	
E = []
'''
	Maintains a list of entry fields in GUI 
	Let the size of E be n
	E[n-2] is entry for search field
	E[n-1] is Search output field
	All others are Data Entry Columns
'''


# Function to add entry in the file
def add_entry_click(path):
	temp = []
	for i in range(len(E)-2):
		temp.append(E[i].get())
		E[i].delete(0, len(temp[len(temp)-1])) # deletes the entry once add entry is clicked

	print(temp) # prints on terminal
	A.add(temp, path) # Adds the entry in file


# Function to search entry in file
def search_click(path, returnall):

	E[len(E)-1].delete(0, T.END)  # Last Index belongs to list box. So, clear the list box
	person_id = E[len(E)-2].get() # 2nd Last Index belongs to search field

	out = A.search(person_id, path, returnall)

	cur = 1

	# add each line of output enter it into search field
	for item in out:
		E[len(E)-1].insert(cur, item)
		cur += 1


# The Main GUI
def make_gui(column_names, path, returnall):

	box = T.Tk()
	box.title("Our GUI")


	T.Label(box, text='ID_Num').grid(row=0) # id_num is always a field
	E.append(T.Entry(box))
	E[0].grid(row=0, column=1)
	cur_row = 1

	# adding other fields
	for col in column_names:

		T.Label(box, text=col).grid(row=cur_row)
		E.append(T.Entry(box))
		E[len(E)-1].grid(row=cur_row, column=1)
		cur_row += 1

	# Button for Add Entry
	btn = T.Button(box, text="Add Entry", command=lambda: add_entry_click(path))
	btn.grid(column=2, row=1) 	

	# Add field for searching using ID
	T.Label(box, text='Search using ID_Num').grid(row=cur_row) 
	E.append(T.Entry(box))
	E[len(E)-1].grid(row=cur_row,column=1)

	# Button for Add Entry
	btn2 = T.Button(box, text="Search", command=lambda: search_click(path, returnall))
	btn2.grid(column=2, row=cur_row) 

	# Add field for Displaying Search Results
	T.Label(box, text="Search Results")
	E.append(T.Listbox(box))
	E[len(E)-1].grid(row=cur_row+1, column=1)
	box.mainloop()
