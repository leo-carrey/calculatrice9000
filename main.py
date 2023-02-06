from tkinter import *

window = Tk()
window.title("Calculatrice 9000")
window.geometry("300x300")

txt_input=''
result = StringVar()


def func(num):
    global txt_input
    txt_input += str(num)
    result.set(txt_input)


def sup_character():
    global txt_input
    txt_input = ""
    input.delete(len(input.get())-1, END)
    txt_input = input.get()

def sup_all():
    global txt_input
    txt_input = ""
    result.set("")

def plus_moin():
    global txt_input
    if txt_input.isalnum():
        txt_input = "(-" + txt_input + ")"
        result.set(txt_input)
    else:
        txt_input = txt_input[2:len(txt_input)-1]
        result.set(txt_input)
        
    
def equal(): 
    try: 
        global txt_input
        resultat = str(eval(txt_input))
        result.set(resultat)
        txt_input = resultat
    except: 
        result.set("error")
        txt_input = ""


input = Entry(window,text=result, relief=SOLID, width=30)
input.grid(row=1, columnspan=3, pady=10)


button7 = Button(window, text='7', fg='black', height=2, width=9, command=lambda: func(7))
button7.grid(row=4, column=0)

button8 = Button(window, text='8', fg='black', height=2, width=9, command=lambda: func(8))
button8.grid(row=4, column=1)

button9 = Button(window, text='9', fg='black', height=2, width=9, command=lambda: func(9))
button9.grid(row=4, column=2)

button4 = Button(window, text='4', fg='black', height=2, width=9, command=lambda: func(4))
button4.grid(row=5, column=0)

button5 = Button(window, text='5', fg='black', height=2, width=9, command=lambda: func(5))
button5.grid(row=5, column=1)

button6 = Button(window, text='6', fg='black', height=2, width=9, command=lambda: func(6))
button6.grid(row=5, column=2)

button1 = Button(window, text='1', fg='black', height=2, width=9, command=lambda: func(1))
button1.grid(row=6, column=0)

button2 = Button(window, text='2', fg='black', height=2, width=9, command=lambda: func(2))
button2.grid(row=6, column=1)

button3 = Button(window, text='3', fg='black', height=2, width=9, command=lambda: func(3))
button3.grid(row=6, column=2)

button0 = Button(window, text='0', fg='black', height=2, width=9, command=lambda: func(0))
button0.grid(row=7, column=1)

buttonC = Button(window, text='C', fg='black', height=2, width=9, command=lambda: sup_all())
buttonC.grid(row=3, column=2)

buttonDel = Button(window, text='⌫', fg='black', height=2, width=9, command=lambda: sup_character())
buttonDel.grid(row=1, column=3)

buttonModulo = Button(window, text='%', fg='black', height=2, width=9, command=lambda: func("%"))
buttonModulo.grid(row=3, column=1)

buttonSubtraction = Button(window, text='-', fg='black', height=2, width=9, command=lambda: func("-"))
buttonSubtraction.grid(row=5, column=3)

buttonAddition = Button(window, text='+', fg='black', height=2, width=9, command=lambda: func("+"))
buttonAddition.grid(row=6, column=3)

buttonX = Button(window, text='*', fg='black', height=2, width=9, command=lambda: func("*"))
buttonX.grid(row=4, column=3)

buttonEqual = Button(window, text='=', fg='black', height=2, width=9, command=lambda: equal())
buttonEqual.grid(row=7, column=3)

buttonDivides = Button(window, text='/', fg='black', height=2, width=9, command=lambda: func("/"))
buttonDivides.grid(row=3, column=3)

buttonComma = Button(window, text=',', fg='black', height=2, width=9, command=lambda: func("."))
buttonComma.grid(row=7, column=2)

buttonPositive = Button(window, text='+/-', fg='black', height=2, width=9, command=lambda: plus_moin())
buttonPositive.grid(row=7, column=0)

buttonPi = Button(window, text='π', fg='black', height=2, width=9, command=lambda: func("3.1415926535"))
buttonPi.grid(row=3, column=0)


window.mainloop()