from tkinter import *

counter = 0

def write(x):
    global counter
    inpbox.insert(counter, x)
    counter += 1

def clear(y):
    var1 = len(inpbox.get())
    if(y <= var1):
        inpbox.delete(0, var1)
    else:
        inpbox.delete(0, y)    

def result():
    eq = inpbox.get()
    answer = eval(eq)
    clear(counter)
    inpbox.insert(0, answer)

main = Tk()

main.resizable(0, 0)
main.title("Calculator")

frameE = Frame(main, bg = "white", bd = 0)
frameE.pack(fill = BOTH)
frameN = Frame(main)
frameN.pack(side = BOTTOM)

inpbox = Entry(frameE, bd = 0, relief = FLAT)

button1 = Button(frameN, text = "1", command = lambda:write(1), padx = 25, pady = 20, bg = "white", bd = 0.5, relief = RIDGE)
button2 = Button(frameN, text = "2", command = lambda:write(2), padx = 20, pady = 20, bg = "white", bd = 0.5, relief = RIDGE)
button3 = Button(frameN, text = "3", command = lambda:write(3), padx = 20, pady = 20, bg = "white", bd = 0.5, relief = RIDGE)
button4 = Button(frameN, text = "4", command = lambda:write(4), padx = 25, pady = 20, bg = "white", bd = 0.5, relief = RIDGE)
button5 = Button(frameN, text = "5", command = lambda:write(5), padx = 20, pady = 20, bg = "white", bd = 0.5, relief = RIDGE)
button6 = Button(frameN, text = "6", command = lambda:write(6), padx = 20, pady = 20, bg = "white", bd = 0.5, relief = RIDGE)
button7 = Button(frameN, text = "7", command = lambda:write(7), padx = 25, pady = 20, bg = "white", bd = 0.5, relief = RIDGE)
button8 = Button(frameN, text = "8", command = lambda:write(8), padx = 20, pady = 20, bg = "white", bd = 0.5, relief = RIDGE)
button9 = Button(frameN, text = "9", command = lambda:write(9), padx = 20, pady = 20, bg = "white", bd = 0.5, relief = RIDGE)
button0 = Button(frameN, text = "0", command = lambda:write(0), padx = 77.5, pady = 20, bg = "white", bd = 0.5, relief = RIDGE)
buttonadd = Button(frameN, text = "+", command = lambda:write("+"), padx = 18.499999999999999, pady = 20, bg = "light grey", bd = 0.5, relief = RIDGE)
buttonsub = Button(frameN, text = "-", command = lambda:write("-"), padx = 20, pady = 20, bg = "light grey", bd = 0.5, relief = RIDGE)
buttonmul = Button(frameN, text = "*", command = lambda:write("*"), padx = 20, pady = 20, bg = "light grey", bd = 0.5, relief = RIDGE)
buttondiv = Button(frameN, text = "/", command = lambda:write("/"), padx = 20, pady = 20, bg = "light grey", bd = 0.5, relief = RIDGE)
buttonclr = Button(frameN, text = "C", command = lambda:clear(counter), padx = 76.5, pady = 20, bg = "light grey", bd = 0.5, relief = RIDGE)
buttonpnt = Button(frameN, text = ".", command = lambda:write("."), padx = 20.5, pady = 20, bg = "light grey", bd = 0.5, relief = RIDGE)
buttonans = Button(frameN, text = "=", command = lambda:result(), padx = 103, pady = 20, bg = "light grey", bd = 0.5, relief = RIDGE)

inpbox.pack(ipadx = 50, ipady = 10)
button1.grid(row = 1, column = 0, sticky = "W")
button2.grid(row = 1, column = 1, sticky = "W")
button3.grid(row = 1, column = 2, sticky = "W")
button4.grid(row = 2, column = 0, sticky = "W")
button5.grid(row = 2, column = 1, sticky = "W")
button6.grid(row = 2, column = 2, sticky = "W")
button7.grid(row = 3, column = 0, sticky = "W")
button8.grid(row = 3, column = 1, sticky = "W")
button9.grid(row = 3, column = 2, sticky = "W")
button0.grid(row = 4, column = 0, columnspan = 3, sticky = "W")
buttonclr.grid(row = 0, columnspan = 3)
buttonadd.grid(row = 0, column = 3, sticky = "W")
buttondiv.grid(row = 1, column = 3, sticky = "W")
buttonmul.grid(row = 2, column = 3, sticky = "W")
buttonpnt.grid(row = 3, column = 3, sticky = "W")
buttonsub.grid(row = 4, column = 3, sticky = "W")
buttonans.grid(row = 5, column = 0, columnspan = 4, sticky = "W")

main.mainloop()
