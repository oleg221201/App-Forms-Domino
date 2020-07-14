import tkinter as tk
import tkinter.messagebox as tkmb
import random

domino_array = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
				[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
				[2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
				[3, 3], [3, 4], [3, 5], [3, 6],
				[4, 4], [4, 5], [4, 6],
				[5, 5], [5, 6],
				[6, 6]]

def read_file():
	with open("file.txt", "r") as file:
		array = file.readlines()
		new_arr = []
		for i in array:
			i = i.replace("\n", "")
			new_arr.append(int(i))
		return new_arr

def write_file(a):
	with open("file.txt", "a") as file:
		file.write(str(a) + '\n')

def clear_file():
	with open("file.txt", "w") as file:
		file.write('')

class MyWindow(tk.Frame):
	def __init__(self):
		self.root = tk.Tk()
		super().__init__(self.root)

		main_menu = tk.Menu(self.root)
		self.root.config(menu = main_menu)
		menu1 = tk.Menu(main_menu)
		menu2 = tk.Menu(main_menu)
		main_menu.add_cascade(label = "New domino", menu = menu1)
		menu1.add_command(label = "Create", command = self.create_new_domino)
		menu1.add_command(label = "Generate", command = self.generate_new_domino)
		main_menu.add_cascade(label = "File", menu = menu2)
		menu2.add_command(label = "View", command = self.file_view)
		menu2.add_command(label = "Clean", command = self.file_clean)
		main_menu.add_cascade(label = "Points addition", command = self.addition)
		self.canva = tk.Canvas(self.root, width = 600, height = 400)
		self.canva.pack()
		self.root.mainloop()

	def create_new_domino(self):
		create_dialog_window()

	def generate_new_domino(self):
		generate_dialog_window()

	def file_view(self):
		file_view_window()

	def file_clean(self):
		if tkmb.askyesno("Clear", "Do you want to clear file content?"):
			clear_file()

	def addition(self):
		array = read_file()
		result = 0
		for i in array:
			result += (domino_array[i][0] + domino_array[i][1])

		tkmb.showinfo("Result", result)


class create_dialog_window(tk.Toplevel):
	def __init__(self):
		super().__init__()
		self.geometry('300x170+300+250')
		self.resizable(False, False)
		self.grab_set()
		self.focus_set()
		self.label0 = tk.Label(self, text = "")
		self.label1 = tk.Label(self, text = "Enter value of points")
		self.label2 = tk.Label(self, text = "Left side: ")
		self.entry1 = tk.Entry(self, width = 20, font = 10)
		self.label3 = tk.Label(self, text = "Right side: ")
		self.entry2 = tk.Entry(self, width = 20, font = 10)
		self.button1 = tk.Button(self, text = "Save")
		self.button2 = tk.Button(self, text = "Cancel")
		self.label1.grid(columnspan = 2)
		self.label2.grid(row = 1, column = 0)
		self.entry1.grid(row = 1, column = 1)
		self.label0.grid(row = 2, column = 0)
		self.label3.grid(row = 3, column = 0)
		self.entry2.grid(row = 3, column = 1)
		self.label0.grid(row = 4, column = 0)
		self.button1.grid(columnspan = 2)
		self.button2.grid(columnspan = 2)
		self.button1.bind("<Button-1>", self.save)
		self.button2.bind("<Button-1>", self.cancel)


	def save(self, event):
		boolean_1 = True
		boolean_2 = True
		array_index = -1
		save_domino_array = read_file()

		try:
			if int(self.entry1.get()) >= 0 and int(self.entry1.get()) <= 6:
				boolean_1 = True
				value1 = int(self.entry1.get())
			else:
				boolean_1 = False
				tkmb.showinfo("Error", "Incorrect value in text_feild_1")
		except ValueError:
			boolean_1 = False
			tkmb.showinfo("Error", "Incorrect value in text_feild_1")

		try:
			if int(self.entry2.get()) >= 0 and int(self.entry2.get()) <= 6:
				boolean_2 = True
				value2 = int(self.entry2.get())
			else:
				boolean_2 = False
				tkmb.showinfo("Error", "Incorrect value in text_feild_2")
		except ValueError:
			boolean_2 = False
			tkmb.showinfo("Error", "Incorrect value in text_feild_2")

		if boolean_1 and boolean_2:
			for i in domino_array:
				if (i[0] == value1 and i[1] == value2) or (i[1] == value1 and i[0] == value2):
					array_index = domino_array.index(i)
			
			if array_index >= 0:
				if len(save_domino_array) >= 7:
					tkmb.showinfo("Error", "Maximum size!")
				else:
					if array_index in save_domino_array:
						tkmb.showinfo("Error", "Domino exists")
					else:
						write_file(array_index)
						tkmb.showinfo("Succsess", "Domino is successfully added!")

			self.entry1.delete(0, 'end')
			self.entry2.delete(0, 'end')
			
			

	def cancel(self, event):
		self.destroy()


class generate_dialog_window(tk.Toplevel):
	def __init__(self):
		super().__init__()
		self.geometry('200x170+300+250')
		self.resizable(False, False)
		self.grab_set()
		self.focus_set()
		self.label0 = tk.Label(self, text = "")
		self.label1 = tk.Label(self, text = "Here you can generate new domino")
		self.label2 = tk.Label(self, text = "Left side: ")
		self.label3 = tk.Label(self, text = "")
		self.label4 = tk.Label(self, text = "Right side: ")
		self.label5 = tk.Label(self, text = "")
		self.button1 = tk.Button(self, text = "Generate")
		self.button2 = tk.Button(self, text = "Save")
		self.button3 = tk.Button(self, text = "Cancel")
		self.label1.grid(columnspan = 2)
		self.label2.grid(row = 1, column = 0)
		self.label3.grid(row = 1, column = 1)
		self.label0.grid(row = 2, column = 0)
		self.label4.grid(row = 3, column = 0)
		self.label5.grid(row = 3, column = 1)
		self.label0.grid(row = 4, column = 0)
		self.button1.grid(columnspan = 2)
		self.button2.grid(columnspan = 2)
		self.button3.grid(columnspan = 2)
		self.button1.bind("<Button-1>", self.generate)
		self.button2.bind("<Button-1>", self.save)
		self.button3.bind("<Button-1>", self.cancel)
		self.gen_domino = -1

	def generate(self, event):
		save_domino_array = read_file()
		fit_boolean = False
		while fit_boolean == False:
			random_num = random.randint(0, 27)
			if random_num in save_domino_array:
				fit_boolean = False
			else:
				fit_boolean = True
				self.gen_domino = random_num
				self.label3['text'] = domino_array[random_num][0]
				self.label5['text'] = domino_array[random_num][1]

	def save(self, event):
		save_domino_array = read_file()
		if len(save_domino_array) >= 7:
			tkmb.showinfo("Error", "Maximum size!")
		else:
			if self.gen_domino in save_domino_array:
				tkmb.showinfo("Error", "Domino exists")
			else:
				write_file(self.gen_domino)
				tkmb.showinfo("Succsess", "Domino is successfully added!")

	def cancel(self, event):
		self.destroy()

class file_view_window(tk.Toplevel):
	def __init__(self):
		super().__init__()
		self.geometry('200x70+300+250')
		self.resizable(False, False)
		self.grab_set()
		self.focus_set()
		self.label0 = tk.Label(self, text = "File content:")
		self.label1 = tk.Label(self, text = "")
		self.label0.grid(columnspan = 1)
		self.label1.grid(row = 1, column = 0)

		array = read_file()
		text = "  "
		for i in array:
			text += str(domino_array[i][0])
			text += "/"
			text += str(domino_array[i][1])
			text += "; "

		self.label1['text'] = text

MyWindow()

