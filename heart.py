from asyncio import log
from datetime import date
from telnetlib import LOGOUT
from tkinter import *
from tkinter import Tk, Label
from numpy import place

background = "#f0ddd5"
frame = "#fefbfb"

root = Tk()
root.title("Heart Attack Prediction System")
root.geometry("1450x730+60+80")
root.resizable(False, False)
root.config(bg=background)

def set_icon():
    image_icon = PhotoImage(file="Images/icon.png")
    root.iconphoto(False, image_icon)

# Main loop
root.after(100, set_icon)  # Wait 100 milliseconds before setting the icon



##header section 2
logo=PhotoImage(file="Images/header.png")
myimage=Label(image=logo,bg=background)
myimage.place(x=0,y=0)

##<<<<<<frame 3
Heading_entry=Frame(root,width=800,height=190,bg="#df2d4b") 
Heading_entry.place(x=600,y=20)
Label (Heading_entry, text="Registration No.", font="arial 13", bg="#df2d4b",fg=frame).place(x=30,y=0)
Label(Heading_entry, text="Date", font="arial 13", bg="#df2d4b",fg=frame).place(x=430,y=0)
Label (Heading_entry, text="Patient Name", font="arial 13", bg="#df2d4b",fg=frame).place(x=30,y=90)
Label(Heading_entry, text="Birth Year", font="arial 13", bg="#df2d4b", fg=frame).place(x=430,y=90)


Entry_image=PhotoImage(file="Images/Rounded Rectangle 1.png")
Entry_image2=PhotoImage(file="Images/Rounded Rectangle 2.png")
Label (Heading_entry,image=Entry_image,bg="#df2d4b").place(x=20,y=30)
Label(Heading_entry,image=Entry_image,bg="#df2d4b").place(x=430,y=30)

Label (Heading_entry,image=Entry_image2,bg="#df2d4b").place(x=20,y=120) 
Label(Heading_entry, image=Entry_image2,bg="#df2d4b").place(x=430,y=120)

Registration=IntVar()
reg_entry= Entry(Heading_entry,textvariable=Registration,width=30,font="arial 15",bg="#0e5363",fg="white",bd=0)
reg_entry.place(x=30,y=45)


Date=StringVar()
today=date.today()
d1=today.strftime("%d/%m/&y")
date_entry= Entry(Heading_entry, textvariable=Date,width=15,font='arial 15',bg="#0e5363",fg="white",bd=0)
date_entry.place(x=500,y=45)
Date.set(d1)

Name=StringVar()
name_entry= Entry(Heading_entry, textvariable=Name, width=20, font="arial 20",bg="#ededed",fg="#222222",bd=0)
name_entry.place(x=30,y=130)

DOB=IntVar()
dob_entry= Entry (Heading_entry, textvariable=DOB, width=20, font="arial 20", bg="#ededed",fg="#222222",bd=0)
dob_entry.place(x=450,y=130)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$BODY$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Detail_entry=Frame(root,width=490,height=260,bg="#dbe0e3")
Detail_entry.place(x=30,y=450)



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$RADIO BUTTON$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def selection():
    if gen.get()==1:
        Gender=1
        return(Gender)
        print(Gender)
    elif gen.get()==2:
        Gender=0
        return (Gender)
        print(Gender)
    else:
        print(Gender)
    
    


def selection2():
    if fbs.get()==1:
        Fbs=1
        return(Fbs)
        print(Fbs)
    elif fbs.get()==2:
        Fbs=0
        return (Fbs)
        print(Fbs)
    else:
        print(Fbs)


def selection3():
    if exang.get()==1:
        Exang=1
        return(Exang)
        print(Exang)
    elif exang.get()==2:
        Exang=0
        return (Exang)
        print(Exang)
    else:
        print(Exang)
    





# IntVar for gender selection
gen = IntVar()

# Frame for the "Sex" category
sex_frame = Frame(Detail_entry, bg=frame)
sex_frame.grid(row=0, column=0, padx=(0, 10))  # Added padx=(0, 10) for space only on the right side


# Label for the "Sex" category
Label(sex_frame, text="Sex:", font="arial 13", bg=frame, fg="black").pack(side=LEFT)

# Radio buttons for gender selection
R1 = Radiobutton(sex_frame, text='Male', variable=gen, value=1,command=selection)
R2 = Radiobutton(sex_frame, text="Female", variable=gen, value=2,command=selection)
R1.pack(side=LEFT)
R2.pack(side=LEFT, padx=5)

# IntVar for fbs selection
fbs = IntVar()
# Frame for the "fbs" category
fbs_frame = Frame(Detail_entry, bg=frame)
fbs_frame.grid(row=0, column=1, padx=(0, 10))  # Added padx=(0, 10) for space on both sides

# Label for the "fbs" category
Label(fbs_frame, text="fbs:", font="arial 13", bg=frame, fg="black").pack(side=LEFT)


# Checkbutton for fbs
Checkbutton(fbs_frame, text="fbs", variable=fbs, bg=frame).pack(side=LEFT)

# Radio buttons for fbs selection
R3 = Radiobutton(fbs_frame, text='True', variable=fbs, value=1,command=selection2)
R4 = Radiobutton(fbs_frame, text="False", variable=fbs, value=2,command=selection2)
R3.pack(side=LEFT)
R4.pack(side=LEFT, padx=5)

# IntVar for exang selection
exang = IntVar()

# Frame for the "exang" category
exang_frame = Frame(Detail_entry, bg=frame)
exang_frame.grid(row=0, column=2, padx=(10, 0))  # Added padx=(10, 0) for space only on the left side

# Label for the "exang" category
Label(exang_frame, text="exang:", font="arial 13", bg=frame, fg="black").pack(side=LEFT)




# Checkbutton for exang
Checkbutton(exang_frame, text="exang", variable=exang, bg=frame).pack(side=LEFT)

# Radio buttons for exang selection
R5 = Radiobutton(exang_frame, text='Yes', variable=exang, value=1,command=selection3)
R6 = Radiobutton(exang_frame, text="No", variable=exang, value=2,command=selection3)
R5.pack(side=LEFT)
R6.pack(side=LEFT, padx=5)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$comboboxx$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Frame for detail entry
Detail_entry = Frame(root, width=490, height=210, bg="#dbe0e3")
Detail_entry.place(x=30, y=450)


Label(Detail_entry, text="cp:", font="Arial 13", bg=frame, fg="black").place(x=10, y=30)
Label(Detail_entry, text="restecg:", font="Arial 13", bg=frame, fg="black").place(x=10, y=70)
Label(Detail_entry, text="slope:", font="Arial 13", bg=frame, fg="black").place(x=10, y=110)
Label(Detail_entry, text="ca:", font="Arial 13", bg=frame, fg="black").place(x=10, y=150)
Label(Detail_entry, text="thal:", font="Arial 13", bg=frame, fg="black").place(x=10, y=190)











Detail_entry.mainloop()
