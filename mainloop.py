from tkinter import *
from sympy import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")

my_frame1 = Frame(root, width=10, height=10,padx=10,pady=2,highlightbackground='black',highlightthickness=2)
my_frame1.pack(fill="none")
sizeLabel = Label(my_frame1, text="Matrix Size:")
my_frame2 = Frame(root, width=500, height=10,padx=50)
my_frame2.pack(fill="none")
XLabel = Label(my_frame1, text="X")
XLabel.grid(row=0,column=2)

def SetSize():
    makeEmptyMatrix()

setSize = Button(my_frame1,text="Set Size", command = SetSize)
setSize.grid(row=0,column=4)


sizeLabel.grid(row=0, column = 0)
clickedRowButton = StringVar()
rows = OptionMenu(my_frame1, clickedRowButton, '1','2','3','4','5','6','7','8')
clickedRowButton.set("3")
rows.grid(row=0,column=1)

clickedColButton = StringVar()
cols = OptionMenu(my_frame1, clickedColButton, '1','2','3','4','5','6','7','8')
clickedColButton.set("3")
cols.grid(row=0,column=3)

Operation = StringVar()
Ops = OptionMenu(my_frame1, Operation, 'Addition','RREF','Multiplication')
Operation.set("Addition/")
cols.grid(row=0,column=2)

textBoxes = []
def makeEmptyGrid():   
    for x in range(10):
        textBoxes.append([])
        for y in range(10):
            textBoxes[x].append(Entry(my_frame2,width='5',border=3))


def makeEmptyMatrix():
    for inpField in my_frame2.winfo_children():
      inpField.grid_remove()
    makeEmptyGrid()
    for ro in range(int(clickedRowButton.get())):
       for co in range(int(clickedColButton.get())):
        textBoxes[ro][co].grid(row=ro, column=co) 

SetSize()
root.mainloop()