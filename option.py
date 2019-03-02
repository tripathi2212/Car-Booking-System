from Tkinter import*

root = Tk()

Options=["Hyundy", "2Vrejs", "asghs"]
var = StringVar()

DropDownMenu=apply(OptionMenu, (root, var) + tuple(Options))
DropDownMenu.place(x=10, y=10)
print DropDownMenu.value()
root.mainloop()
