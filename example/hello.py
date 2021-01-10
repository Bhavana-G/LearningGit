import tkinter
from tkinter import messagebox
from tkinter import END
from random import randint

#GUESSING GAME:
low = 0
high = 20
rand = randint(low, high)
print(rand)

def check(guess):
    if guess < rand:
        tkinter.Label(tk, text=f"{guess} is too low").pack()
    elif guess > rand:
        tkinter.Label(tk, text=f"{guess} is too high").pack()
    else:
        tkinter.messagebox.showinfo("You WIN!", f"{guess} is correct")
        #                           title and   content of alert box

tk = tkinter.Tk()
tk.title("Hello World")

#label telling user what to do
label = tkinter.Label(tk, text=f"Guess a number {low} to {high} (inclusive)")
label.pack()

#text box to enter input
entry = tkinter.Entry(tk)
entry.pack()

#Button to submit the guess
button = tkinter.Button(tk, text="Guess", command=lambda: check(int(entry.get()))) #how to pass arguments to command for buttons in tkinter
button.pack()

tk.mainloop() #pauses all execution and following code will be executed after we exit that window
print("Done") #prints in terminal

#LISTBOX:
tk = tkinter.Tk()
tk.title("Listbox")

listbox = tkinter.Listbox(tk)
listbox.insert(0, "hello", "hi", "yo")
listbox.insert(2, "hola")
listbox.pack()

#even if inserted after listbox.pack it works fine as it works dynamically
listbox = tkinter.Listbox(tk)
listbox.pack()
listbox.insert(END, "hello", "hi", "yo")
listbox.insert(END, "hola") #inserts at the end of list
listbox.delete(0)

tk.mainloop()

#UPDATE LISTBOX FROM USER INPUT:
def add_to_list():
    listbox2.insert(END, entry2.get())
    entry2.delete(0, END) #clears entered data in text box

def remove_from_list():
    listbox2.delete(listbox2.curselection())

tk2 = tkinter.Tk()
tk2.title("List Box")

listbox2 = tkinter.Listbox(tk2)
listbox2.pack()

entry2 = tkinter.Entry(tk2)
entry2.pack()

button2 = tkinter.Button(tk2, text="Add Value", command=add_to_list) #no need of lambda - since we are not passing any arguments
button2.pack()

button2 = tkinter.Button(tk2, text="Remove Selected Value", command=remove_from_list)
button2.pack()

tk2.mainloop()
