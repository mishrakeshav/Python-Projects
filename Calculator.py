from tkinter import *   
#from tkinter import messagebox
from tkinter import Button
#from tkinter import LEFT

expression = ""


def press(num):

    global expression
    expression += str(num)

    equation.set(expression)


def equalpress():

    try:
        global expression
        # eval evaluates the expression to find the ans
        total = str(eval(expression))
        equation.set(total)

        expression = ""
    except:
        equation.set("Error")
        expression = ""

# this functions clears the text in Entry


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == '__main__':

    # making a object of tkinter class
    root = Tk()
    root.configure(background="sky blue")
    root.title("Calculator-by Keshav Mishra")
    root.geometry("360x390+300+300")
    root.resizable(False, False)

    equation = StringVar()  # StrigVar() is a class

    expression_field = Entry(root,  textvariable=equation,
                             bd=3, width=25, font=("arial", 10, "bold"))
    expression_field.grid(columnspan=4, ipadx=70)

    equation.set("Enter your expression ")

    button1 = Button(root, text=' 1 ', fg='black', bg='wheat2',
                     command=lambda: press(1), height=5, width=10, font=("arial", 10, "bold"))
    button1.grid(row=2, column=0)

    button2 = Button(root, text=' 2 ', fg='black', bg='wheat2',
                     command=lambda: press(2), height=5, width=10, font=("arial", 10, "bold"))
    button2.grid(row=2, column=1)

    button3 = Button(root, text=' 3 ', fg='black', bg='wheat2',
                     command=lambda: press(3), height=5, width=10, font=("arial", 10, "bold"))
    button3.grid(row=2, column=2)

    button4 = Button(root, text=' 4 ', fg='black', bg='wheat2',
                     command=lambda: press(4), height=5, width=10, font=("arial", 10, "bold"))
    button4.grid(row=3, column=0)

    button5 = Button(root, text=' 5 ', fg='black', bg='wheat2',
                     command=lambda: press(5), height=5, width=10, font=("arial", 10, "bold"))
    button5.grid(row=3, column=1)

    button6 = Button(root, text=' 6 ', fg='black', bg='wheat2',
                     command=lambda: press(6), height=5, width=10, font=("arial", 10, "bold"))
    button6.grid(row=3, column=2)

    button7 = Button(root, text=' 7 ', fg='black', bg='wheat2',
                     command=lambda: press(7), height=5, width=10, font=("arial", 10, "bold"))
    button7.grid(row=4, column=0)

    button8 = Button(root, text=' 8 ', fg='black', bg='wheat2',
                     command=lambda: press(8), height=5, width=10, font=("arial", 10, "bold"))
    button8.grid(row=4, column=1)

    button9 = Button(root, text=' 9 ', fg='black', bg='wheat2',
                     command=lambda: press(9), height=5, width=10, font=("arial", 10, "bold"))
    button9.grid(row=4, column=2)

    button0 = Button(root, text=' 0 ', fg='black', bg='wheat2',
                     command=lambda: press(0), height=5, width=10, font=("arial", 10, "bold"))
    button0.grid(row=5, column=0)
    plus = Button(root, text=' + ', fg='black', bg='wheat2',
                  command=lambda: press("+"), height=5, width=10, font=("arial", 10, "bold"))
    plus.grid(row=2, column=3)

    minus = Button(root, text=' - ', fg='black', bg='wheat2',
                   command=lambda: press("-"), height=5, width=10, font=("arial", 10, "bold"))
    minus.grid(row=3, column=3)

    multiply = Button(root, text=' * ', fg='black', bg='wheat2',
                      command=lambda: press("*"), height=5, width=10, font=("arial", 10, "bold"))
    multiply.grid(row=4, column=3)

    divide = Button(root, text=' / ', fg='black', bg='wheat2',
                    command=lambda: press("/"), height=5, width=10, font=("arial", 10, "bold"))
    divide.grid(row=5, column=3)

    equal = Button(root, text=' = ', fg='black', bg='wheat2',
                   command=equalpress, height=5, width=10, font=("arial", 10, "bold"))
    equal.grid(row=5, column=2)

    clear = Button(root, text='Clear', fg='black', bg='wheat2',
                   command=clear, height=5, width=10, font=("arial", 10, "bold"))
    clear.grid(row=5, column='1')

    root.mainloop()
