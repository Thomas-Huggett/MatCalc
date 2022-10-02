from tkinter import *
from sympy import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")


my_frame1 = Frame(root, width=10, height=10,padx=10,pady=2,highlightbackground='black',highlightthickness=2)
my_frame1.grid(row=0,column=0)
sizeLabel = Label(my_frame1, text="Matrix Size:")
my_frame3 = Frame(root,width=10,height=10,highlightthickness=1)
my_frame3.grid(row=1,column=0)
my_frame2 = Frame(my_frame3, width=500, height=10,padx=5)
my_frame2.grid(row=0,column=0)
plusLabel = Label(my_frame3,text='+',font=("Arial", 40))

my_frame4=Frame(my_frame3,height=0,width=0)
my_frame4.grid(row=0,column=2,pady=10)

my_frame6=Frame(root)
my_frame6.grid(row=3,column=0)
my_frame5=Frame(my_frame6,pady=5,highlightthickness=1,highlightbackground='black')
my_frame5.grid(row=0,column=1)
solLabel=Label(my_frame6,text='Solution:')
solLabel.grid(row=0,column=0)

XLabel = Label(my_frame1, text="X")
XLabel.grid(row=0,column=2)

def SetSize():
    makeEmptyMatrix(my_frame2)
    if(operation.get != 'RREF'):
        makeEmptyMatrix2(my_frame4)
def Solve():
    if(Operation.get()=='RREF'):
        unsolvedList = []
        for x in range(int(clickedRowButton.get())):
            unsolvedList.append([])
            for y in range(int(clickedColButton.get())):
                try:
                    n = float(textBoxes[x][y].get())
                except:
                    return
                unsolvedList[x].append(textBoxes[x][y].get())
        
        unsolvedMatrix = Matrix(unsolvedList)
        solvedMatrix = unsolvedMatrix.rref()

        for widg in my_frame5.winfo_children():
            widg.grid_remove()
        solvedList = solvedMatrix[0].tolist()
        yPos=0
        for num in solvedList:
            xPos=0
            yPos+= 1
            for ans in num:
                k = Label(my_frame5, text=ans)
                k.grid(row=yPos,column=xPos)
                xPos+=1 
    if(Operation.get()=='Addition'):
        unsolvedList = []
        for x in range(int(clickedRowButton.get())):
            unsolvedList.append([])
            for y in range(int(clickedColButton.get())):
                s1 = int(textBoxes[x][y].get())
                s2 = int(textBoxes2[x][y].get())
                s2 += s1
                k = Label(my_frame5,text = s2)
                k.grid(row=x,column=y)


def setOP():
    if(Operation.get() == 'Addition'):
        plusLabel.grid(row=0,column=1)
        makeEmptyMatrix2(my_frame4)
    else:
        plusLabel.grid_remove()
        for w in my_frame4.winfo_children():
            w.grid_remove()

setSize = Button(my_frame1,text="Set Size", command = SetSize)
setSize.grid(row=0,column=4)
solveButton = Button(my_frame1,text="Solve", command = Solve)
solveButton.grid(row=0,column=11)
setOPButton = Button(my_frame1,text="Set Operation", command = setOP)
setOPButton.grid(row=0,column=10)


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
Ops = OptionMenu(my_frame1, Operation, 'RREF','Addition','Multiplication')
Operation.set("RREF")
Ops.grid(row=0,column=6)

textBoxes = []
def makeEmptyGrid(frames):   
    for x in range(10):
        textBoxes.append([])
        for y in range(10):
            textBoxes[x].append(Entry(frames,width='5',border=1))


def makeEmptyMatrix(frames):
    for inpField in frames.winfo_children():
      inpField.grid_remove()
    makeEmptyGrid(frames)
    for ro in range(int(clickedRowButton.get())):
       for co in range(int(clickedColButton.get())):
        textBoxes[ro][co].grid(row=ro, column=co) 

textBoxes2 = []
def makeEmptyGrid2(frames):   
    for x in range(10):
        textBoxes2.append([])
        for y in range(10):
            textBoxes2[x].append(Entry(frames,width='5',border=1))


def makeEmptyMatrix2(frames):
    for inpField in frames.winfo_children():
      inpField.grid_remove()
    makeEmptyGrid2(frames)
    for ro in range(int(clickedRowButton.get())):
       for co in range(int(clickedColButton.get())):
        textBoxes2[ro][co].grid(row=ro, column=co) 

makeEmptyMatrix(my_frame2)
root.mainloop()