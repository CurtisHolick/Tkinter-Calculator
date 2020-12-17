import tkinter as tk

root = tk.Tk()
root.title("Calculator")


#display
fullEquationDisp = tk.Label(root,text = "input your equation",height = 2,font = "TkDefaultFont 8",borderwidth=2,relief="groove")
fullEquationDisp.grid(row=0,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)

currentInputDisp = tk.Label(root,text = "input numbers",height = 3,font = "TkDefaultFont 12",relief="groove")
currentInputDisp.grid(row=1,columnspan=4,sticky=tk.W+tk.E+tk.N+tk.S)

currentInput = []
finalEquation = []

def solve():
    global currentInput,finalEquation
    finalEquation.append(lstToString(currentInput))
    fullEquationDisp.config(text = lstToString(finalEquation))
    currentInput = []
    solution = round(eval(lstToString(finalEquation)),6)
    currentInputDisp.config(text = solution)
    finalEquation = [solution]
    #fullEquationDisp.config(text = lstToString(finalEquation))

def lstToString(lst):
    #converts a list passed to a string
    return "".join(str(e) for e in lst)

   
def inputNumber(num):
    #inputs the passed number to the active input line
    global currentInput
    currentInput.append(num)
    currentInputDisp.config(text = lstToString(currentInput))

def makeNumButtons(root):
    #make the buttons
    button9 = tk.Button(root, text = "9",command = lambda: inputNumber(9),
                        width = 8, height = 3,relief="groove",borderwidth=1).grid(row=4,column=2)
    button8 = tk.Button(root, text = "8",command = lambda: inputNumber(8),
                        width = 8, height = 3,relief="groove",borderwidth=1).grid(row=4,column=1)
    button7 = tk.Button(root, text = "7",command = lambda: inputNumber(7),
                        width = 8, height = 3,relief="groove",borderwidth=1).grid(row=4,column=0)
    button6 = tk.Button(root, text = "6",command = lambda: inputNumber(6),
                        width = 8, height = 3,relief="groove",borderwidth=1).grid(row=5,column=2)
    button5 = tk.Button(root, text = "5",command = lambda: inputNumber(5),
                        width = 8, height = 3,relief="groove",borderwidth=1).grid(row=5,column=1)
    button4 = tk.Button(root, text = "4",command = lambda: inputNumber(4),
                        width = 8, height = 3,relief="groove",borderwidth=1).grid(row=5,column=0)
    button3 = tk.Button(root, text = "3",command = lambda: inputNumber(3),
                        width = 8, height = 3,relief="groove",borderwidth=1).grid(row=6,column=2)
    button2 = tk.Button(root, text = "2",command = lambda: inputNumber(2),
                        width = 8, height = 3,relief="groove",borderwidth=1).grid(row=6,column=1)
    button1 = tk.Button(root, text = "1",command = lambda: inputNumber(1),
                        width = 8, height = 3,relief="groove",borderwidth=1).grid(row=6,column=0)
    button1 = tk.Button(root, text = "0",command = lambda: inputNumber(0),
                        width = 8, height = 3,relief="groove",borderwidth=1).grid(row=7,column=1)
    button1 = tk.Button(root, text = ".",command = lambda: inputNumber("."),
                        width = 8, height = 3,relief="groove",borderwidth=1).grid(row=7,column=2)
makeNumButtons(root)


def operator(func):
    global currentInput,finalEquation
    finalEquation.extend([lstToString(currentInput),func])
    fullEquationDisp.config(text = lstToString(finalEquation))
    currentInput = []
    #currentInputDisp.config(text = "")

def clear(power):
    global currentInput,finalEquation
    if power == "all":
        finalEquation = []
        fullEquationDisp.config(text = "")
        currentInput = []
        currentInputDisp.config(text = "0")        
    elif power == "input":
        currentInput = []
        currentInputDisp.config(text = "")
    elif power == "backspace":
        currentInput.pop()
        currentInputDisp.config(text = lstToString(currentInput))

def standardFunctionButtons(root):
    #makes the buttons that do stuff besides input numbers or decimals
    buttonDiv = tk.Button(root, text = "÷",command = lambda: operator("/"),
                        width = 8, height = 3,relief = "groove",borderwidth=1).grid(row=3,column=3)
    buttonMultiply = tk.Button(root, text = "x",command = lambda: operator("*"),
                        width = 8, height = 3,relief = "groove",borderwidth=1).grid(row=4,column=3)
    buttonSub = tk.Button(root, text = "-",command = lambda: operator("-"),
                        width = 8, height = 3,relief = "groove",borderwidth=1).grid(row=5,column=3)
    buttonAdd = tk.Button(root, text = "+",command = lambda: operator("+"),
                        width = 8, height = 3,relief = "groove",borderwidth=1).grid(row=6,column=3)
    buttonEquals = tk.Button(root, text = "=",command = lambda: solve(),
                        width = 8, height = 3,relief = "groove",borderwidth=1).grid(row=7,column=3)
    buttonClearAll = tk.Button(root, text = "Clear All",command = lambda: clear("all"),
                        width = 8, height = 3,relief = "groove",borderwidth=1).grid(row=3,column=0)
    buttonClearAll = tk.Button(root, text = "Clear Input",command = lambda: clear("input"),
                        width = 8, height = 3,relief = "groove",borderwidth=1).grid(row=3,column=1)
    buttonBackspace = tk.Button(root, text = "⌫",command = lambda: clear("backspace"),
                        width = 8, height = 3,relief = "groove",borderwidth=1).grid(row=3,column=2)
    buttonMore = tk.Button(root, text = "More",command = lambda: moreButtons(),
                        width = 8, height = 3,relief = "groove",borderwidth=1).grid(row=7,column=0)


standardFunctionButtons(root)

def moreButtons():
    buttonOpenPar = tk.Button(root, text = "(",command = lambda: inputNumber("("),
                        width = 8, height = 3,relief = "groove",borderwidth=1).grid(row=7,column=4)
    buttonClosePar = tk.Button(root, text = ")",command = lambda: inputNumber(")"),
                        width = 8, height = 3,relief = "groove",borderwidth=1).grid(row=7,column=5)


##fullEquationDisp.config( sticky=N)

root.mainloop()
##def lstToInt(lst):
##    s = map(str, lst)
##    s = ''.join(s)
##    s = int(s)
##    return s























