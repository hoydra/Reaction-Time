
from tkinter import *
import time
import random


random_int = random.randint(1,3)
start = 0
click_amt = 0
early = False

# Tkinter Start
root = Tk()
root.wm_title("Reaction Time")
root.iconbitmap("eye.ico")
root.resizable(False, False)



def quit():

    root.quit()

def not_ready():

    global early
    early = True
    warning = Label(root,text="Too Early",font="Fixedsys")
    warning.grid(row=0,column=1,padx=2,pady=2)
    root.after(2500, warning.grid_forget)



def ready(rand,button):

    time.sleep(rand)
    button.grid_forget()
    button = Button(root, text="YES READY", padx=50, pady=50, bg="green2", command=click)
    button.grid(row=0,column=0)
    global start
    start = time.time()


def click():

    global click_amt

    if click_amt == 0:
        end = time.time() - start
        ms = Label(root,text=str(end)[:4],font="Fixedsys")
        ms.grid(row=0,column=1,padx=2,pady=2)
        click_amt += 1
    else:
        #ms.grid_forget()
        quit_button = Button(root,text="Quit",command=quit)
        quit_button.grid(row=0,column=1,padx=2,pady=2)




# Declare buttons
early_button = Button(root,text="NOT READY", padx=50,pady=50,bg="red",command=not_ready)
start_button = Button(root,text="Start",padx=30,pady=20,command=lambda: ready(random_int,early_button))

# Display buttons
early_button.grid(row=0,column=0)
start_button.grid(row=1,column=0)



root.mainloop()

