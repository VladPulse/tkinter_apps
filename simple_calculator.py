from tkinter import *


root = Tk()
root.resizable(False,False)
root.title('My Simple Calculator')
root.config(bg='#343434')

color_orange = '#fc7703'
color_gray = '#343434'
color_red = '#fc0303'

first_number = 0
operation = ''


# create Entry
entry = Entry(root, width=8, borderwidth=1, font=('Terminal', 30),
              fg='white',bg=color_gray)
entry.grid(column=0,row=0, columnspan=4)

# functions
def insert_number(number):
    current_text = entry.get()
    entry.delete(0,END)
    entry.insert(END, current_text + str(number))

def clear():
    global first_number, operation
    entry.delete(0, END)  # Clear the entry field
    first_number = 0  # Reset the first number
    operation = ''  # Reset the operation


def add():
    global first_number, operation
    if entry.get():
        first_number = float(entry.get())
    operation = 'add'
    entry.delete(0,END)

def subtract():
    global first_number, operation
    if entry.get():
        first_number = float(entry.get())
    operation = 'subtract'
    entry.delete(0,END)

def multiply():
    global first_number, operation
    if entry.get():
        first_number = float(entry.get())
    operation = 'multiply'
    entry.delete(0,END)

def divide():
    global first_number, operation
    if entry.get():
        first_number = float(entry.get())
    operation = 'divide'
    entry.delete(0,END)

def equal():
    global first_number,operation
    # Check if the entry field is empty, or if no operation was selected
    if not entry.get() or operation == '':
        entry.delete(0, END)
        entry.insert(END, str(first_number))  # Just show the first number if no operation
        return


    second_number = float(entry.get()) # Get the second number

    if operation == 'add':
        result = first_number + second_number
    elif operation == 'subtract':
        result = first_number - second_number
    elif operation == 'multiply':
        result = first_number * second_number
    elif operation == 'divide':
        if second_number == 0:
            entry.delete(0, END)
            entry.insert(END, "Error")
            return
        result = first_number / second_number

    entry.delete(0, END)  # Clear the entry box
    entry.insert(END, str(result))  # Insert the result into the entry box

    # Save the result as the new first number for the next calculation
    first_number = result

    # Reset the operation after calculation
    operation = ''


def insert_dot():
    current_text = entry.get()

    # Only add a dot if there isn't already one in the current number
    if '.' not in current_text:
        entry.delete(0, END)  # Clear the entry field
        entry.insert(END, current_text + '.')  # Insert the dot after the current number

# Bind keyboard input to operator functions
root.bind('+', lambda event: add())
root.bind('-', lambda event: subtract())
root.bind('*', lambda event: multiply())
root.bind('/', lambda event: divide())
root.bind('<Return>', lambda event: equal())  # Enter key as equal
root.bind('<BackSpace>', lambda event: clear())  # Backspace to clear

# number Buttons
button_7 = Button(root, text='7', padx=25, pady=10, fg='white',bg=color_gray,
                  command=lambda: insert_number(7))
button_7.grid(column=0,row=1,columnspan=1)
button_8 = Button(root, text='8', padx=25, pady=10, fg='white',bg=color_gray,
                  command=lambda: insert_number(8))
button_8.grid(column=1,row=1)
button_9 = Button(root, text='9', padx=25, pady=10, fg='white',bg=color_gray,
                  command=lambda: insert_number(9))
button_9.grid(column=2,row=1)
button_4 = Button(root, text='4', padx=25, pady=10, fg='white',bg=color_gray,
                  command=lambda: insert_number(4))
button_4.grid(column=0,row=2)
button_5 = Button(root, text='5', padx=25, pady=10, fg='white',bg=color_gray,
                  command=lambda: insert_number(5))
button_5.grid(column=1,row=2)
button_6 = Button(root, text='6', padx=25, pady=10, fg='white',bg=color_gray,
                  command=lambda: insert_number(6))
button_6.grid(column=2,row=2)
button_1 = Button(root, text='1', padx=25, pady=10, fg='white',bg=color_gray,
                  command=lambda: insert_number(1))
button_1.grid(column=0,row=3)
button_2 = Button(root, text='2', padx=25, pady=10, fg='white',bg=color_gray,
                  command=lambda: insert_number(2))
button_2.grid(column=1,row=3)
button_3 = Button(root, text='3', padx=25, pady=10, fg='white',bg=color_gray,
                  command=lambda: insert_number(3))
button_3.grid(column=2,row=3)
button_0 = Button(root, text='0', padx=25, pady=10, fg='white',bg=color_gray,
                  command=lambda: insert_number(0))
button_0.grid(column=0,row=4)

dot_button = Button(root,text=' .',padx=25, pady=10, fg='white',bg=color_gray,
                  command=insert_dot)
dot_button.grid(column=1,row=4)

# operator Buttons
button_plus = Button(root, text='+', padx=25, pady=10, fg='white',bg=color_orange,
                     command=add)
button_plus.grid(column=3,row=1)

subtract_button = Button(root,text='- ',padx=25, pady=10, fg='white',bg=color_orange,command=subtract)
subtract_button.grid(column=3,row=2)

multiply_button = Button(root,text='* ',padx=25, pady=10, fg='white',bg=color_orange,command=multiply)
multiply_button.grid(column=3,row=3)

division_button = Button(root,text='/ ',padx=25, pady=10, fg='white',bg=color_orange,command=divide)
division_button.grid(column=3,row=4)


clear_button = Button(root,text='C',padx=24, pady=10, fg='white',bg=color_red,command=clear)
clear_button.grid(column=2,row=4)

equal_button = Button(root,text='=',padx=123, pady=10, borderwidth=1, fg='white',bg=color_orange,command=equal,)
equal_button.grid(column=0,row=5, columnspan=4)

root.mainloop()