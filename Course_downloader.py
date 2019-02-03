import wget
from urllib import request
from tkinter import *
import tkinter
import webbrowser

def ref(click):
    webbrowser.open_new(r'https://pravash21.github.io/')

    
win =Tk()
win.geometry ="800x800"
win.wm_title('Online Course Downloader')
win.config(background = '#708090', height = 800, width = 800)

def printSomething():
    
    label = Label(root, text= "Tutorial Not Found")
    label.pack() 
def PDF_Download():
    global tutorial
    tutorial=tutorial_name.get()
    try:
      PDF_url = 'https://www.tutorialspoint.com/'+tutorial+'/'+tutorial+'_tutorial.pdf'
      print(PDF_url)
      wget.download(PDF_url)
      root = Tk()
      button = Button(root, text="Tutorial Downloaded", command=printSomething) 
      button.pack()
      root.mainloop()
    except:
    	root = Tk()
    	button = Button(root, text="No such Tutorial Found", command=printSomething) 
    	button.pack()
    	root.mainloop()
    	raise Exception('No such Tutorial Found')



f= Frame(win,height=1000, width=1000)
f.grid(row=0, column=0,padx=250, pady=200)
tutorial_name = Entry(f, width=80 )
tutorial_name.grid(row=0, column=0)

Get_PDF = Button(f, text ='Get Course',command = PDF_Download)
Get_PDF.grid(row =0, column =1)
Photo = PhotoImage(file ='course.png')
Photo0 = PhotoImage(file = 'b.png')
lbl0 = Label(f,image=Photo0)
lbl = Label(f, image = Photo)
lbl.grid(row =5, column =0,padx=80,pady=20)
lbl0.grid(row=10,column=0)
lbl1 = Label(f, text="Created by Team:  Logic_Out_Of_Bound", fg='blue', cursor ="hand2")
lbl1.grid(row =6, column =0,padx=80,pady=0)

lbl1.bind("<Button-1>",  ref)

win.mainloop()


