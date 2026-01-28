from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text =="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    elif text == "⌫":  # Backspace button (you can use text "Back" also)
        current_value = scvalue.get()
        scvalue.set(current_value[:-1])  # remove last character
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


root=Tk()#will create an empty window
root.geometry("428x850")#setting size of window
root.configure(bg="orange")
root.title("Calculator by Tanya Gupta ;) ")
root.iconbitmap("cal.ico")   # file should exist in same folder

scvalue=StringVar()
scvalue.set("")
screen=Entry(root, textvar=scvalue,font="lucida 35 bold")
#Entry is a Tkinter widget used for single-line text input.
#Here, we are creating an Entry widget and storing its reference in the variable screen.
#The first argument root means this Entry widget will be placed inside the main window (root = Tk()).
#textvar connects the Entry widget with a Tkinter variable.
#Whatever is typed or displayed in the Entry box is stored in scvalue.
#font style, size, and weight
screen.pack(fill=X, ipadx=8,pady=10,padx=10)
#.pack() is a geometry manager in Tkinter.
#It tells Tkinter: “place this widget in the window.”


#frames with 3 buttons

f =Frame(root, bg="orange")

b=Button(f, text="9",padx=25,pady=18, font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f, text="8",padx=25,pady=18, font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f, text="7",padx=25,pady=18, font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

f =Frame(root, bg="orange")

b=Button(f, text="6",padx=25,pady=18, font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f, text="5",padx=25,pady=18, font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f, text="4",padx=25,pady=18, font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

f =Frame(root, bg="orange")

b=Button(f, text="3",padx=25,pady=18, font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f, text="2",padx=25,pady=18, font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f, text="1",padx=25,pady=18, font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

f =Frame(root, bg="orange")

b=Button(f, text="0",padx=25,pady=18, font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f, text="-",padx=26,pady=18, font="lucida 33 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f, text="*",padx=26,pady=18, font="lucida 32 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

f =Frame(root, bg="orange")

b=Button(f, text="/",padx=23,pady=13, font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f, text="%",padx=23,pady=18, font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f, text="=",padx=23,pady=18, font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()
f = Frame(root, bg="orange")

b = Button(f, text="C", padx=25, pady=18, font="lucida 30 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=25, pady=18, font="lucida 30 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="⌫", padx=25, pady=18, font="lucida 30 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()#it keeps the window open and responsive until the user closes it manually
