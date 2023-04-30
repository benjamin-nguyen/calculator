# Import necessary modules
from tkinter import *
import math
import tkinter.messagebox

# Create the calculator GUI
root = Tk()  # Create main window
root.wm_iconbitmap("calculator.ico")  # Set window icon
root.title("Calculator")  # Set window title
root.configure(background="white")  # Set window background color
root.resizable(width=False, height=False)  # Disable window resizing
root.geometry("311x368+0+0")  # Set window size and position

# Create calculator frame
calculator = Frame(root, bg="gainsboro")
calculator.grid()


# Define calculator class
class Calculator:
    # Initialize class variables
    def __init__(self):
        self.total = 0  # The total value
        self.current = ""  # The current value
        self.inputValue = True  # Whether the input value is a new value
        self.checkSum = False  # Whether a calculation has been made
        self.op = ""  # The current operation being performed
        self.result = False  # Whether the result has been calculated

    def enterNumber(self, num):
        """Add a digit to the display"""
        self.result = False
        firstNum = displayText.get()  # Get the current value of the entry box
        secondNum = str(num)  # Get the value of the number pad button pressed
        if self.inputValue:
            self.current = secondNum
            self.inputValue = False
        else:
            # If the entered number is a decimal: check if there is another decimal in the entry
            # If there is, return nothing, otherwise append the entered number to the current entry
            if secondNum == ".":
                if secondNum in firstNum:
                    return
            self.current = firstNum + secondNum
        self.display(self.current)

    # Method to calculate the sum of total values
    def sumOfTotal(self):
        self.result = True
        self.current = float(self.current)
        if self.checkSum:
            self.validFunction()
        else:
            self.total = float(displayText.get())

    # Method to validate and perform the current operation
    def validFunction(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multiply":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.inputValue = True
        self.checkSum = False
        self.display(self.total)

    # Method to perform an operation
    def operation(self, op):
        self.current = float(self.current)
        if self.checkSum:
            self.validFunction()
        elif not self.result:
            self.total = self.current
            self.inputValue = True
        self.checkSum = True
        self.op = op
        self.result = False

    # Method to clear the entry box
    def clearEntry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.inputValue = True

    # Method to clear all entry boxes
    def clearAllEntry(self):
        self.clearEntry  # Clear the current entry box
        self.total = 0  # Clear the total value

    def plusMinus(self):
        self.result = False
        self.current = -(float(displayText.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(displayText.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(displayText.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(displayText.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(displayText.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(displayText.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(displayText.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(displayText.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(displayText.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(displayText.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(displayText.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(displayText.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(displayText.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(displayText.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(displayText.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(displayText.get()))
        self.display(self.current)

    def display(self, value):
        # Clears previous entry text and displays entry text with number entered
        displayText.delete(0, END)
        displayText.insert(0, value)


addedValue = Calculator()

# Display
displayText = Entry(
    calculator,
    font=("Arial", 15, "bold"),
    bd=0,
    width=27,
    justify=RIGHT,
    bg="light gray",
    relief=RIDGE,
)
displayText.grid(row=0, column=0, columnspan=4, pady=0)
displayText.insert(0, "0")

# Standard Calculator Buttons
numPad = "789456123"
button = []
i = 0

for j in range(2, 5):
    for k in range(3):
        button.append(
            Button(
                calculator,
                width=6,
                height=2,
                font=("Arial", 15, "bold"),
                bd=0,
                bg="SlateGray3",
                text=numPad[i],
            )
        )
        button[i].grid(row=j, column=k, pady=0)
        button[i]["command"] = lambda x=numPad[i]: addedValue.enterNumber(x)
        i += 1

# Buttons

clearEntryButton = Button(
    calculator,
    text=chr(67) + chr(69),
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.clearEntry,
).grid(row=1, column=0, pady=0)

clearAllButton = Button(
    calculator,
    text=chr(67),
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.clearAllEntry,
).grid(row=1, column=1, pady=0)

sqrtButton = Button(
    calculator,
    text=chr(8730),
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.squared,
).grid(row=1, column=2, pady=0)

divideButton = Button(
    calculator,
    text=chr(247),
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=lambda: addedValue.operation("divide"),
).grid(row=1, column=3, pady=0)

multiplyButton = Button(
    calculator,
    text=chr(215),
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=lambda: addedValue.operation("multiply"),
).grid(row=2, column=3, pady=0)

minusButton = Button(
    calculator,
    text=chr(45),
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=lambda: addedValue.operation("sub"),
).grid(row=3, column=3, pady=0)

plusButton = Button(
    calculator,
    text=chr(43),
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=lambda: addedValue.operation("add"),
).grid(row=4, column=3, pady=0)

pmButton = Button(
    calculator,
    text=chr(177),
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.plusMinus,
).grid(row=5, column=0, pady=0)

zeroButton = Button(
    calculator,
    text=chr(48),
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray3",
    command=lambda: addedValue.enterNumber(0),
).grid(row=5, column=1, pady=0)

dotButton = Button(
    calculator,
    text=chr(46),
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=lambda: addedValue.enterNumber("."),
).grid(row=5, column=2, pady=0)

equalsButton = Button(
    calculator,
    text=chr(61),
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="orange",
    command=addedValue.sumOfTotal,
).grid(row=5, column=3, pady=0)

# Scientific Calculator Buttons

piButton = Button(
    calculator,
    text=chr(960),
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.pi,
).grid(row=1, column=5, pady=0)

sinButton = Button(
    calculator,
    text="sin",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.sin,
).grid(row=1, column=6, pady=0)

cosButton = Button(
    calculator,
    text="cos",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.cos,
).grid(row=1, column=7, pady=0)

tanButton = Button(
    calculator,
    text="tan",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.tan,
).grid(row=1, column=8, pady=0)


twoPiButton = Button(
    calculator,
    text="2" + chr(960),
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.pi,
).grid(row=2, column=5, pady=0)

sinhButton = Button(
    calculator,
    text="sinh",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray3",
    command=addedValue.sinh,
).grid(row=2, column=6, pady=0)

coshButton = Button(
    calculator,
    text="cosh",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray3",
    command=addedValue.cosh,
).grid(row=2, column=7, pady=0)

tanhButton = Button(
    calculator,
    text="tanh",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray3",
    command=addedValue.tanh,
).grid(row=2, column=8, pady=0)


logButton = Button(
    calculator,
    text="log",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.log,
).grid(row=3, column=5, pady=0)

expButton = Button(
    calculator,
    text="exp",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray3",
    command=addedValue.exp,
).grid(row=3, column=6, pady=0)

modButton = Button(
    calculator,
    text="mod",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray3",
    command=lambda: addedValue.operation("mod"),
).grid(row=3, column=7, pady=0)

eButton = Button(
    calculator,
    text="e",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray3",
    command=addedValue.e,
).grid(row=3, column=8, pady=0)


log2Button = Button(
    calculator,
    text="log2",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.log2,
).grid(row=4, column=5, pady=0)

degButton = Button(
    calculator,
    text="deg",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray3",
    command=addedValue.degrees,
).grid(row=4, column=6, pady=0)

acoshButton = Button(
    calculator,
    text="acosh",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray3",
    command=addedValue.acosh,
).grid(row=4, column=7, pady=0)

asinhButton = Button(
    calculator,
    text="asinh",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray3",
    command=addedValue.asinh,
).grid(row=4, column=8, pady=0)


log10Button = Button(
    calculator,
    text="log10",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.log10,
).grid(row=5, column=5, pady=0)

log1pButton = Button(
    calculator,
    text="log1p",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.log1p,
).grid(row=5, column=6, pady=0)

expm1Button = Button(
    calculator,
    text="expm1",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.expm1,
).grid(row=5, column=7, pady=0)

lgammaButton = Button(
    calculator,
    text="lgamma",
    width=6,
    height=2,
    font=("Arial", 15, "bold"),
    bd=0,
    bg="SlateGray4",
    command=addedValue.lgamma,
).grid(row=5, column=8, pady=0)


scientificDisplayTitle = Label(
    calculator,
    text="Scientific Calculator",
    font=("Helvetica", 20, "bold", "italic"),
    bg="gray",
    padx=26,
    justify=CENTER,
)
scientificDisplayTitle.grid(row=0, column=5, columnspan=4)


# Menu & Functions
def exit():
    exit = tkinter.messagebox.askyesno("Calculator", "Are you sure you want to exit?")
    if exit > 0:
        root.destroy()
        return


def standardCalc():
    root.resizable(width=False, height=False)
    root.geometry("311x348+0+0")


def scientificCalc():
    root.resizable(width=False, height=False)

    root.geometry("624x348+0+0")


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
