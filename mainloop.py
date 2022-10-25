from operator import matmul
from tkinter import *
from turtle import color
from sympy import *
from tkinter import ttk

#initalizes main tkinter Frame
root = Tk()
root.geometry("500x500")


#sets up Frames for input, solution, and seleections
pad = (10,80)
headerLabel = Label(root,text="Linear Algebra Calculator",font=("Times", 24),fg='Grey')
headerLabel.grid(row=0,column=0,pady=(10,30))
my_frame1 = Frame(root, width=10, height=10,padx=10,pady=2,highlightbackground='black',highlightthickness=2)
my_frame1.grid(row=1,column=0)
sizeLabel = Label(my_frame1, text="Matrix Size:")
my_frame3 = Frame(root,width=10,height=10,highlightthickness=1)
my_frame3.grid(row=2,column=0)
my_frame2 = Frame(my_frame3, width=500, height=10,padx=5)
my_frame2.grid(row=0,column=0)
plusLabel = Label(my_frame3,text='+',font=("Arial", 40))
timesLabel = Label(my_frame3,text='x',font=("Arial", 40))

my_frame4=Frame(my_frame3,height=0,width=0)
my_frame4.grid(row=0,column=2,pady=10)

my_frame6=Frame(root)
my_frame6.grid(row=4,column=0)
my_frame5=Frame(my_frame6,pady=5,highlightthickness=1,highlightbackground='black')
my_frame5.grid(row=0,column=1)
solLabel=Label(my_frame6,text='Solution:')
solLabel.grid(row=0,column=0)

XLabel = Label(my_frame1, text="X")
XLabel.grid(row=0,column=2)

#function called when user clicks "Set Size" button
def SetSize():
    makeEmptyMatrix(my_frame2)
    if(Operation.get() == 'Addition'):
        plusLabel.grid(row=0,column=1)
        makeEmptyMatrix2(my_frame4)
        
    if(Operation.get() == 'Multiplication'):
        timesLabel.grid(row=0,column=1)
        
        makeEmptyMatrix2(my_frame4)


#Function called when user clicks "Solve Button"
def Solve():

    #When Operation = RREF
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
    
    #When operation = Addition
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

    #When operation = Multiplication
    if(Operation.get()=='Multiplication'):
        unsolvedList = []
        for x in range(int(clickedRowButton.get())):
            unsolvedList.append([])
            for y in range(int(clickedColButton.get())):
                
                try:
                    n = float(textBoxes[x][y].get())
                except:
                    
                    return
                unsolvedList[x].append(textBoxes[x][y].get())
        unsolvedList2 = []
        for x in range(int(clickedColButton.get())):
            
            unsolvedList2.append([])
            for y in range(int(clickedRowButton.get())):
                
                try:
                    n = float(textBoxes2[x][y].get())
                except:
                    
                    return
                unsolvedList2[x].append(textBoxes2[x][y].get())
        unsolvedMatrix = Matrix(unsolvedList)
        unsolvedMatrix2 = Matrix(unsolvedList2)

        #clear Solution Frame
        for widg in my_frame5.winfo_children():
            widg.grid_remove()

        #Solve and place solution onto solution frame
        solvedMatrix = matmul(unsolvedMatrix,unsolvedMatrix2)
        print(solvedMatrix)
        solvedList = solvedMatrix.tolist()
        print(solvedList)
        for i in range(len(solvedList)):
            for j in range(len(solvedList[i])):
                a = Label(my_frame5,text=solvedList[i][j])
                a.grid(row=i,column=j)
        
        

        
        
#function called when user clicks "Set Operation" button
def setOP():
    if(Operation.get() == 'Addition'):
        plusLabel.grid(row=0,column=1)
        timesLabel.grid_remove()
        makeEmptyMatrix2(my_frame4)
        makeEmptyMatrix(my_frame2)
    elif(Operation.get() == 'Multiplication'):
        timesLabel.grid(row=0,column=1)
        makeEmptyMatrix2(my_frame4)
        makeEmptyMatrix(my_frame2)
    else:
        plusLabel.grid_remove()
        timesLabel.grid_remove()
        for w in my_frame4.winfo_children():
            w.grid_remove()

#Initalizes buttons
setSize = Button(my_frame1,text="Set Size", command = SetSize)
setSize.grid(row=0,column=4)
solveButton = Button(my_frame1,text="Solve", command = Solve)
solveButton.grid(row=0,column=11)
setOPButton = Button(my_frame1,text="Set Operation", command = setOP)
setOPButton.grid(row=0,column=10)

#initializes row drop down list
sizeLabel.grid(row=0, column = 0)
clickedRowButton = StringVar()
rows = OptionMenu(my_frame1, clickedRowButton, '1','2','3','4','5','6','7','8')
clickedRowButton.set("3")
rows.grid(row=0,column=1)

#initializes column drop down list
clickedColButton = StringVar()
cols = OptionMenu(my_frame1, clickedColButton, '1','2','3','4','5','6','7','8')
clickedColButton.set("3")
cols.grid(row=0,column=3)

#initializes operations drop down list    
Operation = StringVar()
Ops = OptionMenu(my_frame1, Operation, 'RREF','Addition','Multiplication')
Operation.set("RREF")
Ops.grid(row=0,column=6)

textBoxes = []
#creates 10x10 empty grid of input boxes
def makeEmptyGrid(frames):   
    
    for x in range(10):
        textBoxes.append([])
        for y in range(10):
            textBoxes[x].append(Entry(frames,width='5',border=1))

#clear input frame and then adds correct # of boxes to frame
def makeEmptyMatrix(frames):
    for inpField in frames.winfo_children():
      inpField.grid_remove()
    #makeEmptyGrid(frames)
    for ro in range(int(clickedRowButton.get())):
       for co in range(int(clickedColButton.get())):
        textBoxes[ro][co].grid(row=ro, column=co) 

#clears input second input frame and adds correct # of boxes to frame
textBoxes2 = []
def makeEmptyGrid2(frames): 
    
    for x in range(10):
        textBoxes2.append([])
        for y in range(10):
            textBoxes2[x].append(Entry(frames,width='5',border=1))

#clears second input frame and then adds correct # of boxes to frame
def makeEmptyMatrix2(frames):
    for inpField in frames.winfo_children():
      inpField.grid_remove()
    #makeEmptyGrid2(frames)
    if(Operation.get()=='Addition'):
        for ro in range(int(clickedRowButton.get())):
            for co in range(int(clickedColButton.get())):
                textBoxes2[ro][co].grid(row=ro, column=co) 
    else:
        for ro in range(int(clickedColButton.get())):
            for co in range(int(clickedRowButton.get())):
                textBoxes2[ro][co].grid(row=ro, column=co) 

#initalizes grid for both inputs as well as solution
makeEmptyGrid(my_frame2)
makeEmptyGrid2(my_frame4)
makeEmptyMatrix(my_frame2)

#Extra information Labels:
RREFLabel = Label(root,text='For more info on RREF: \n https://www.youtube.com/watch?v=_viQnk7qrwI')
RREFLabel.grid(row=6,column=0)
AdditionLabel = Label(root,text='For more info on Matrix addition: \n https://www.youtube.com/watch?v=xhK-pzSJwJQ')
AdditionLabel.grid(row=7,column=0)
MultiplicationLabel = Label(root,text='For more info on Matrix Multiplication: \n https://www.youtube.com/watch?v=xhK-pzSJwJQ')
MultiplicationLabel.grid(row=8,column=0)
root.mainloop()
