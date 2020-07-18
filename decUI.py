from tkinter import *
from tkinter import filedialog
import os
import decryption

def choose_File():
    filename = filedialog.askopenfilename()
    entry1.insert(0,str(filename))

def performDecryption():
    filePath = entry1.get()
    fileNameArr = filePath.split("/")
    file_name = fileNameArr[len(fileNameArr)-1]
    print(file_name)

    iterations = int(entry2.get())
    kr = int(entry3.get())
    kc = int(entry4.get())

    decryption.imgDecrypt(file_name, iterations, kr, kc)

window = Tk()

Frame1 = Frame(window)
Frame1.pack(side=TOP)
Frame2 = Frame(window)
Frame2.pack(side=TOP)
Frame3 = Frame(window)
Frame3.pack(side=TOP)
Frame4 = Frame(window)
Frame4.pack(side=TOP)

label_1 = Label(Frame1, text ="Image to be Decrypted : ",width = 100)
entry1 = Entry(Frame1,width =100)
button1 = Button(Frame1, text = "Select Image",command = choose_File)

label_2 = Label(Frame2,text = "No. Of Iterations:")
entry2 = Entry(Frame2,width = 45)

label_3 = Label(Frame3, text = "kr: ")
entry3 = Entry(Frame3,width = 10)

label_4 = Label(Frame4, text = "kc: ")
entry4 = Entry(Frame4,width = 10)

button2 = Button(window, text="Perform Decryption", command=performDecryption, width=20)


label_1.pack()
entry1.pack()
button1.pack()

label_2.pack(side=LEFT)
entry2.pack(side=LEFT)

label_3.pack(side=LEFT)
entry3.pack(side=LEFT)

label_4.pack(side=LEFT)
entry4.pack(side=LEFT)

button2.pack()

window.mainloop()
