from tkinter import *
from tkinter import filedialog
import os
import encryption
import database
from datetime import date

todayDate = str(date.today())

def choose_File():
    filename = filedialog.askopenfilename()
    entry1.insert(0,str(filename))

def performEncryption():
    filePath = entry1.get()
    fileNameArr = filePath.split("/")
    file_name = fileNameArr[len(fileNameArr)-1]
    print(file_name)

    iterations_str = entry2.get()
    iterations = int(iterations_str)
    email = entry3.get()

    encryption.inputImg(file_name, iterations, email)
    database.insert(email, todayDate)


def view_history():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def delete_command():
    database.delete()


window = Tk()

Frame1 = Frame(window)
Frame1.pack(side=TOP)
Frame2 = Frame(window)
Frame2.pack(side=TOP)
Frame3 = Frame(window)
Frame3.pack(side=TOP)
Frame4 = Frame(window)
Frame4.pack(side=TOP)

label_1 = Label(Frame1, text ="Image to be Encrypted : ",width = 100)
entry1 = Entry(Frame1,width =100)
button1 = Button(Frame1, text = "Select Image",command = choose_File)

label_2 = Label(Frame2,text = "     No. Of Iterations:")
entry2 = Entry(Frame2, width = 45)

label_3 = Label(Frame3,text = "Enter Email address:")
email_text = StringVar()
entry3 = Entry(Frame3, textvariable=email_text, width = 45)

button2 = Button(window, text="Perform Encryption", command=performEncryption, width=20)

button3 = Button(window, text="History", command=view_history)

button4 = Button(window, text="Delete History", command=delete_command)

list1=Listbox(window, height=8,width=100)


label_1.pack()
entry1.pack()
button1.pack()

label_2.pack(side=LEFT)
entry2.pack(side=LEFT)

label_3.pack(side=LEFT)
entry3.pack(side=LEFT)


button2.pack()

button3.pack()

list1.pack()
button4.pack()

window.mainloop()
