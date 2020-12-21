from tkinter import*
import math
import parser
import tkinter.messagebox

# Calculator GUI
root = Tk()
root.wm_iconbitmap('CalculatorIcon.ico')
root.title("Calculator")
root.configure(background="SlateGray1")
root.resizable(width=False, height=False)
root.geometry("480x620+0+0")

calculator = Frame(root) 
calculator.grid()

# Display
display = Entry(calculator, font=('Arial', 15, 'bold'), bd=30, width=28, justify=RIGHT)
display.grid(row=0, column=0, columnspan=4, pady=1)
display.insert(0, "0")

# Standard Calculator Buttons
numPad = "789456123"
button = []
i=0

for j in range(2,5):
  for k in range(3):
    button.append(Button(calculator, width=6, height=2, font=('Arial', 15, 'bold'), bd=4,  bg="SlateGray1", text=numPad[i]))
    button[i].grid(row=j, column=k, pady=1)
    i+=1
    
clearEntryButton = Button(calculator, text=chr(67)+chr(69), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=1, column=0, pady=1)

clearAllButton = Button(calculator, text=chr(67), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=1, column=1, pady=1)

sqrtButton = Button(calculator, text=chr(8730), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=1, column=2, pady=1)

divideButton = Button(calculator, text=chr(247), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=1, column=3, pady=1)

multiplyButton = Button(calculator, text=chr(215), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=2, column=3, pady=1)

minusButton = Button(calculator, text=chr(45), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=3, column=3, pady=1)

plusButton = Button(calculator, text=chr(43), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=4, column=3, pady=1)

pmButton = Button(calculator, text=chr(177), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=5, column=0, pady=1)

zeroButton = Button(calculator, text=chr(48), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray1").grid(row=5, column=1, pady=1)

dotButton = Button(calculator, text=chr(46), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=5, column=2, pady=1)

equalsButton = Button(calculator, text=chr(61), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="orange").grid(row=5, column=3, pady=1)

# Scientific Calculator Buttons
numPad = "789456123"
button = []
i=0

for j in range(2,5):
  for k in range(3):
    button.append(Button(calculator, width=6, height=2, font=('Arial', 15, 'bold'), bd=4,  bg="SlateGray1", text=numPad[i]))
    button[i].grid(row=j, column=k, pady=1)
    i+=1
    
clearEntryButton = Button(calculator, text=chr(67)+chr(69), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=1, column=0, pady=1)

clearAllButton = Button(calculator, text=chr(67), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=1, column=1, pady=1)

sqrtButton = Button(calculator, text=chr(8730), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=1, column=2, pady=1)

divideButton = Button(calculator, text=chr(247), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=1, column=3, pady=1)

multiplyButton = Button(calculator, text=chr(215), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=2, column=3, pady=1)

minusButton = Button(calculator, text=chr(45), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=3, column=3, pady=1)

plusButton = Button(calculator, text=chr(43), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=4, column=3, pady=1)

pmButton = Button(calculator, text=chr(177), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=5, column=0, pady=1)

zeroButton = Button(calculator, text=chr(48), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray1").grid(row=5, column=1, pady=1)

dotButton = Button(calculator, text=chr(46), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="SlateGray3").grid(row=5, column=2, pady=1)

equalsButton = Button(calculator, text=chr(61), width=6, height=2, font=('Arial', 15, 'bold'), bd=4, bg="orange").grid(row=5, column=3, pady=1)


# Menu & Functions
def exit():
  exit = tkinter.messagebox.askyesno("Calculator", "Are you sure you want to exit?")
  if exit > 0:
    root.destroy()
    return

def standardCalc():
  root.resizable(width=False, height=False)
  root.geometry("944x568+0+0")

def scientificCalc():
  root.resizable(width=False, height=False)
  root.geometry("480x620+0+0")

menuBar = Menu(calculator)

# Menu: File
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Standard", command=standardCalc)
fileMenu.add_command(label="Scientific", command=scientificCalc)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit)

# Menu: Edit
editMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_separator()
editMenu.add_command(label="Paste")

# Menu: Help
helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="View Help")

root.config(menu=menuBar)
root.mainloop()