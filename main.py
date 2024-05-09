from tkinter import *
from decimal import Decimal, getcontext

root = Tk()
root.title('Calc')

display_text = StringVar(value="0")
operator = StringVar()
memory = StringVar(value=str("0"))

getcontext().prec = 10


def is_decimal_integer(value):
    return value % Decimal('1') == 0


def write(value):
    current_value = display_text.get()
    if current_value == "0" and value not in [',', '.']:
        display_text.set(str(value))
    elif value == '.' and '.' in current_value:
        return
    else:
        display_text.set(current_value + str(value))


def format_result(value):
    if is_decimal_integer(value):
        return str(int(value))
    else:
        return str(value)


def write_result(value):
    display_text.set(format_result(value))
    memory.set(str(value))


def prepare_operator(op):
    if op == '=':
        exec_operation()
    else:
        operator.set(op)
        memory.set(display_text.get())
        display_text.set("0")


def exec_operation():
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        'x': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else "Error: Div by 0"
    }
    try:
        mem = Decimal(memory.get())
        disp = Decimal(display_text.get())
        result = operations[operator.get()](mem, disp)
        write_result(result)
    except Exception as e:
        display_text.set("Error")



display = Entry(root, justify='right', textvariable=display_text, font='Helvetica 30 bold')
display.grid(row=1, columnspan=4, sticky='ew')

button = Button(root, text='AC', command=lambda: display_text.set("0"), font='Helvetica 20 bold')
button.grid(row=2, column=0, columnspan=3, sticky='nsew', ipady=10)

def create_digit_button(val, row, col):
    Button(root, text=str(val), font='Helvetica 20 bold',
           command=lambda v=val: write(v)).grid(row=row, column=col, sticky='nsew', ipady=10)

for x in range(3):
    for y in range(3):
        create_digit_button(x*3+y+1, x+3, y)

Button(root, text='0', font='Helvetica 20 bold', command=lambda: write('0')).grid(row=6, column=0, columnspan=2, sticky='nsew', ipady=10)
Button(root, text='.', font='Helvetica 20 bold', command=lambda: write('.')).grid(row=6, column=2, sticky='nsew', ipady=10)

operations = ['+', '-', 'x', '/', '=']
for index, operation in enumerate(operations):
    Button(root, text=operation, font='Helvetica 20 bold', background='blue', foreground='black',
           command=lambda op=operation: prepare_operator(op)).grid(row=index+2, column=3, sticky='nsew', ipady=10)

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)


if __name__ == '__main__':
    root.mainloop()
