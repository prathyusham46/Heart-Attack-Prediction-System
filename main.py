import sys
from re import I
from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter.ttk import Combobox
import datetime
from datetime import date
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib
import selection
matplotlib.use("TKAgg")
import os
from sklearn.linear_model import LogisticRegression
from backend import *
from mysql import *
from sklearn.preprocessing import StandardScaler


import backend
from PIL import Image, ImageTk

import my_module
result = my_module

# Create a connection to the MySQL database
import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection to the MySQL database"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost', 
            user='root',  
            password='varma123',
            database='heart_data'  
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Create a connection to the MySQL database
connection = create_connection()

# Flag to check if login was successful
login_successful = False

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Validate username and password 
    if username == "user" and password == "pass123":
        # If credentials are correct, close login window and open main application window
        login_window.destroy()
        open_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_main_window():
    
    pass

# Create login window
login_window = Tk()
login_window.title("HEART ATTACK PREDICTION SYSTEM LOGIN")
login_window.geometry("1450x730+60+80")


# Load the background image
background_image = Image.open("Images/inside.png")
background_image = background_image.resize((1450, 730), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas
canvas = tk.Canvas(login_window, width=1450, height=730)
canvas.pack(fill="both", expand=True)

# Set the background image on the canvas
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Username Label and Entry
Label(login_window, text="Username:", bg="white").place(relx=0.5, rely=0.4, anchor=CENTER)
username_entry = Entry(login_window)
username_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

# Password Label and Entry
Label(login_window, text="Password:", bg="white").place(relx=0.5, rely=0.5, anchor=CENTER)
password_entry = Entry(login_window, show="*")
password_entry.place(relx=0.6, rely=0.5, anchor=CENTER)
# Login Button
login_button = Button(login_window, text="Login", command=login)
login_button.place(relx=0.5, rely=0.6, anchor=CENTER)

login_window.mainloop()

# Increase max_iter
model = LogisticRegression(max_iter=1000)
# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the model using Logistic Regression with increased max_iter and a different solver
model = LogisticRegression(max_iter=1000, solver='sag')
model.fit(X_scaled, Y)

background = "#f0ddd5"
frame = "#fefbfb"

root = Tk()
root.title("Heart Attack Prediction System")
root.geometry("1450x730+60+80")
root.resizable(False, False)
root.config(bg=background)

##################################################Analysis##################################################
def analysis():
    global prediction
    try:
        print("Starting analysis...")

        # Retrieve user inputs
        name = Name.get()
        D1 = Date.get()
        today = date.today()
        birth_year = DOB.get()

        if birth_year == 0:
            messagebox.showerror("Invalid input", "Please enter a valid birth year!")
            return

        A = today.year - birth_year

        # Retrieve radio button selections
        B = sex_var.get()
        if B == '':
            messagebox.showerror("missing", "Please select gender!")
            return

        F = fbs_var.get()
        if F == '':
            messagebox.showerror("missing", "Please select fbs!")
            return

        I = exang_var.get()
        if I == '':
            messagebox.showerror("missing", "Please select exang!")
            return

        # Retrieve combobox selections
        C = cp_combobox.get()
        if C == '':
            messagebox.showerror("missing", "Please select cp!")
            return

        G = restecg_combobox.get()
        if G == '':
            messagebox.showerror("missing", "Please select restecg!")
            return

        K = slope_combobox.get()
        if K == '':
            messagebox.showerror("missing", "Please select slope!")
            return

        L = ca_combobox.get()
        if L == '':
            messagebox.showerror("missing", "Please select ca!")
            return

        M = thal_combobox.get()
        if M == '':
            messagebox.showerror("missing", "Please select thal!")
            return

        # Retrieve numeric entries
        try:
            D = int(trestbps_entry.get())
            E = int(chol_entry.get())
            H = int(thalach_entry.get())
            J = float(oldpeak_entry.get())
        except ValueError:
            messagebox.showerror("missing data", "Few missing data entry!")
            return

        print("Retrieved values:")
        print("A is age:", A)
        print("B is gender:", B)
        print("C is cp:", C)
        print("D is trestbps:", D)
        print("E is chol:", E)
        print("F is fbs:", F)
        print("G is restecg:", G)
        print("H is thalach:", H)
        print("I is exang:", I)
        print("J is oldpeak:", J)
        print("K is slope:", K)
        print("L is ca:", L)
        print("M is thal:", M)

        # Call selection2() and selection3() functions
        P2 = selection2()
        Q2 = selection3()

        print("P2 (ca):", P2)
        print("Q2 (thal):", Q2)

    except Exception as e:
        # Catch any exceptions and print error message
        print("Error occurred during analysis:", e)
                                                                                                                                                    
        ############first graph###############
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot(["sex", "fbs", "exang"], [B, F, I])
        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.place(width=250, height=250, x=600, y=240)

        ############second graph###############
        f2 = Figure(figsize=(5, 5), dpi=100)
        a2 = f2.add_subplot(111)
        a2.plot(["age", "trestbps", "chol", "thalach"], [A, D, E, H])
        canvas2 = FigureCanvasTkAgg(f2, master=root)
        canvas2.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tk.BOTH, expand=True)
        canvas2._tkcanvas.place(width=250, height=250, x=860, y=240)

        ############third graph###############
        f3 = Figure(figsize=(5, 5), dpi=100)
        a3 = f3.add_subplot(111)
        a3.plot(["oldpeak", "restecg", "cp"], [J, G, C])
        canvas3 = FigureCanvasTkAgg(f3, master=root)
        canvas3.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tk.BOTH, expand=True)
        canvas3._tkcanvas.place(width=250, height=250, x=600, y=470)

        ############fourth graph###############
        f4 = Figure(figsize=(5, 5), dpi=100)
        a4 = f4.add_subplot(111)
        a4.plot(["slope", "ca", "thal"], [K, L, M])
        canvas4 = FigureCanvasTkAgg(f4, master=root)
        canvas4.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tk.BOTH, expand=True)
        canvas4._tkcanvas.place(width=250, height=250, x=860, y=470)
        
        # Convert categorical variables to numeric
        sex_mapping = {"Male": 1, "Female": 0}
        fbs_mapping = {"True": 1, "False": 0}
        exang_mapping = {"Yes": 1, "No": 0}
        cp_mapping = {"1. Typical Angina": 1, "2. Atypical Angina": 2, "3. Non-Anginal Pain": 3, "4. Asymptomatic": 4}
        restecg_mapping = {"0": 0, "1": 1, "2": 2}
        slope_mapping = {"1. Upsloping": 1, "2. Flat": 2, "3. Downsloping": 3}
        ca_mapping = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4}
        thal_mapping = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4}

        B = sex_mapping.get(B)
        F = fbs_mapping.get(F)
        I = exang_mapping.get(I)
        C = cp_mapping.get(C)
        G = restecg_mapping.get(G)
        K = slope_mapping.get(K)
        L = ca_mapping.get(L)
        M = thal_mapping.get(M)
                
        #input data
        input_data=(A,B,C,D,E,F,G,H,I,J,K,L,M)
        input_data_as_numpy_array=np.asanyarray(input_data)
        
        #reshape the numpy array as we are predicting for only on instances
        input_data_reshape=input_data_as_numpy_array.reshape(1,-1)
        
        prediction=model.predict(input_data_reshape)
        print(prediction[0])
        
        if(prediction[0]==0):
            print('The person does not have a Heart disease')
            report.config(text=f"Report:{0}",fg="#8dc63f")
            report1.config(text=f"{name}, you do not have a heart disease")
            
        else:
            print('The person has Heart disease')
            report.config(text=f"Report:{1}",fg="#ed1c24")
            report1.config(text=f"{name}, you  have a heart disease")

        # Assuming selection() function performs the analysis
        try:
            B = selection()  # Call your analysis function
            print(f"Selection result: {B}")
        except Exception as e:
            print("An error occurred during selection:", e)
            messagebox.showerror("NEW USER", " NEW USER ADDED")
            return

        print("Analysis completed successfully.")

    except Exception as e:
        print("An error occurred during analysis:", e)
        messagebox.showerror("Error", "An error occurred during analysis.")

##info window  (operated by info button)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Info():
    Icon_window = Toplevel(root)
    Icon_window.title("Info")
    Icon_window.geometry("700x600+100+100")

    # icon_image
    icon_image = PhotoImage(file="Images/info.png")
    Icon_window.iconphoto(False, icon_image)

    # Heading
    Label(Icon_window, text="Information Related to dataset", font="robot 19 bold").pack(padx=20, pady=20)

    # info
    Label(Icon_window, text="age - age in years", font="arial 11").place(x=20, y=100)
    Label(Icon_window, text="sex - sex (1 = male; 0 = female)", font="arial 11").place(x=20, y=130)
    Label(Icon_window, text="cp - chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3 = asymptomatic)",
        font="arial 11").place(x=20, y=160)
    Label(Icon_window, text="trestbps - resting blood pressure (in mm Hg on admission to the hospital)",
        font="arial 11").place(x=20, y=190)
    Label(Icon_window, text="chol - serum cholesterol in mg/dl", font="arial 11").place(x=20, y=220)
    Label(Icon_window, text="fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)", font="arial 11").place(
        x=20, y=250)
    Label(Icon_window, text="restecg - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)",
        font="arial 11").place(x=20, y=280)
    Label(Icon_window, text="thalach - maximum heart rate achieved", font="arial 11").place(x=20, y=310)
    Label(Icon_window, text="exang - exercise induced angina (1 = yes; 0 = no)", font="arial 11").place(x=20, y=340)
    Label(Icon_window, text="oldpeak - ST depression induced by exercise relative to rest", font="arial 11").place(
        x=20, y=370)
    Label(Icon_window, text="slope - the slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping)",
        font="arial 11").place(x=20, y=400)
    Label(Icon_window, text="ca - number of major vessels (0-3) colored by flourosopy", font="arial 11").place(x=20, y=430)
    Label(Icon_window, text="thal - 0 = normal; 1 = fixed defect; 2 = reversible defect", font="arial 11").place(x=20, y=460)

    Icon_window.mainloop()

######################### it is use for closing window ##############################

def logout():
    root.destroy()
    
######clear ( with the help of clear we can clear more entry field in once)

oldpeak = 0.0  # Replace 0.0 with the appropriate value
thalach = 0
chol = 0  # Replace 0 with the appropriate value
trestbps = 0  # Replace 0 with the appropriate value

def clear():
    Name.get('')
    DOB.get('')
    trestbps.get('')
    chol.get('')
    thalach.set('')
    
    #####save
    def save():
        B2=Name.get()
        C2=Date.get()
        D2=DOB.get()
        
        today=datetime.date.today()
        E2=today.year-DOB.get()
        def selection():
            pass
        
        try:
            F2=selection()
        except:
            messagebox.showerror("Missing Data","Please select gender!")
            
            def selection2():
                pass
            
        try:
            J2=selection2()
        except:
            messagebox.showerror("Missing Data","Please select fbs!")
            
            def selection3():
                pass
            
        try:
            M2=selection3()
        except:
            messagebox.showerror("Missing Data","Please select exang!")
            
            def selection4():
                pass
            
        try:
            G2=selection4()
        except:
            messagebox.showerror("Missing Data","Please select CP!")  
            
        try:
            K2=restecg_combobox.get()
        except:
            messagebox.showerror("Missing Data","Please select restecg!")  
            
            def selection5():
                pass
            
        try:
            O2=selection5()
        except:
            messagebox.showerror("Missing Data","Please select slope!")    
            
        try:
            P2=ca_combobox.get()
        except:
            messagebox.showerror("Missing Data","Please select ca!")
            
        try:
            Q2=thal_combobox.get()
        except:
            messagebox.showerror("Missing Data","Please select thal!")
            
        H2=trestbps.get()
        I2=chol.get()
        L2=thalach.get()
        N2=float(oldpeak.get())
        
        print(B2)
        print(C2)
        print(D2)
        print(E2)
        print(F2)
        print(G2)
        print(H2)
        print(I2)
        print(J2)
        print(K2)
        print(L2)
        print(M2)
        print(N2)
        print(O2)
        print(P2)
        print(Q2)

def set_icon():
    image_icon = PhotoImage(file="Images/icon.png")
    root.iconphoto(False, image_icon)


root.after(100, set_icon)

# Header section
logo = PhotoImage(file="Images/header.png")
myimage = Label(image=logo, bg=background)
myimage.place(x=0, y=0)

# Frame
Heading_entry = Frame(root, width=800, height=190, bg="#df2d4b")
Heading_entry.place(x=600, y=20)
Label(Heading_entry, text="Registration No.", font="arial 13", bg="#df2d4b", fg=frame).place(x=30, y=0)
Label(Heading_entry, text="Date", font="arial 13", bg="#df2d4b", fg=frame).place(x=430, y=0)
Label(Heading_entry, text="Patient Name", font="arial 13", bg="#df2d4b", fg=frame).place(x=30, y=90)
Label(Heading_entry, text="Birth Year", font="arial 13", bg="#df2d4b", fg=frame).place(x=430, y=90)

Entry_image = PhotoImage(file="Images/Rounded Rectangle 1.png")
Entry_image2 = PhotoImage(file="Images/Rounded Rectangle 2.png")
Label(Heading_entry, image=Entry_image, bg="#df2d4b").place(x=20, y=30)
Label(Heading_entry, image=Entry_image, bg="#df2d4b").place(x=430, y=30)

Label(Heading_entry, image=Entry_image2, bg="#df2d4b").place(x=20, y=120)
Label(Heading_entry, image=Entry_image2, bg="#df2d4b").place(x=430, y=120)

Registration = tk.IntVar()
reg_entry = tk.Entry(Heading_entry, textvariable=Registration, width=30, font="arial 15", bg="#0e5363", fg="white", bd=0)
reg_entry.place(x=30, y=45)

Date = StringVar()
today = date.today()
d1 = today.strftime("%d/%m/%y")
date_entry = Entry(Heading_entry, textvariable=Date, width=15, font='arial 15', bg="#0e5363", fg="white", bd=0)
date_entry.place(x=500, y=45)
Date.set(d1)

Name = StringVar()
name_entry = Entry(Heading_entry, textvariable=Name, width=20, font="arial 20", bg="#ededed", fg="#222222", bd=0)
name_entry.place(x=30, y=130)

# Define Date of Birth variable and Entry widget
DOB = IntVar()  
# Define Date of Birth variable and Entry widget
DOB = IntVar()  
dob_entry = Entry(Heading_entry, textvariable=DOB, width=20, font="arial 20", bg="#ededed", fg="#222222", bd=0)
dob_entry.place(x=500, y=130) 

# Function to calculate age and display it
def calculate_age():
    birth_year = DOB.get()
    if birth_year != 0:  # Ensure birth year is provided
        current_year = today.year
        age = current_year - birth_year
        Label(Heading_entry, text=f"Age: {age}", font="arial 13", bg="#df2d4b", fg=frame).place(x=30, y=160)
    else:
        # Display error message if birth year is not provided
        Label(Heading_entry, text="Please enter Birth Year", font="arial 13", bg="#df2d4b", fg="red").place(x=30, y=160)

# Button to trigger age calculation
calculate_button = Button(Heading_entry, text="Calculate Age", command=calculate_age)
calculate_button.place(x=640, y=130)  

# Frame for radio buttons
Radio_frame = Frame(root, width=550, height=100, bg="#dbe0e3")
Radio_frame.place(x=10, y=400)

# Sex radio buttons
sex_var = StringVar()
sex_var.set(None) 

# Adjusted positions and sizes for the sex, fbs, and exang buttons
Label(Radio_frame, text="Sex:", font="arial 10", bg="blue", fg="black").place(x=10, y=10)
Radiobutton(Radio_frame, text="Male", variable=sex_var, value="Male", bg="#dbe0e3").place(x=60, y=10)
Radiobutton(Radio_frame, text="Female", variable=sex_var, value="Female", bg="#dbe0e3").place(x=130, y=10)

# FBS radio buttons
fbs_var = StringVar()
fbs_var.set(None) 

Label(Radio_frame, text="FBS:", font="arial 10", bg="blue", fg="black").place(x=200, y=10)
Radiobutton(Radio_frame, text="True", variable=fbs_var, value="True", bg="#dbe0e3").place(x=240, y=10)
Radiobutton(Radio_frame, text="False", variable=fbs_var, value="False", bg="#dbe0e3").place(x=310, y=10)

# Exang radio buttons
exang_var = StringVar()
exang_var.set(None)  

Label(Radio_frame, text="Exang:", font="arial 10", bg="blue", fg="black", padx=0).place(x=370, y=10)
Radiobutton(Radio_frame, text="Yes", variable=exang_var, value="Yes", bg="#dbe0e3").place(x=410, y=10)
Radiobutton(Radio_frame, text="No", variable=exang_var, value="No", bg="#dbe0e3").place(x=470, y=10)

# Detail entry frame
Detail_entry = Frame(root, width=550, height=200, bg="#dbe0e3")
Detail_entry.place(x=10, y=500)

# Labels and comboboxes for "cp", "restecg", "slope", "ca", and "thal"
Label(Detail_entry, text="cp:", font="arial 13", bg="#dbe0e3", fg="black").place(x=10, y=10)
cp_combobox = Combobox(Detail_entry, values=['1. Typical Angina', '2. Atypical Angina', '3. Non-Anginal Pain', '4. Asymptomatic'], font="Arial 13", state="readonly", width=15)
cp_combobox.place(x=120, y=10)

Label(Detail_entry, text="restecg:", font="arial 13", bg="#dbe0e3", fg="black").place(x=10, y=50)
restecg_combobox = Combobox(Detail_entry, values=['0', '1', '2'], font="Arial 13", state="readonly", width=15)
restecg_combobox.place(x=120, y=50)

Label(Detail_entry, text="slope:", font="arial 13", bg="#dbe0e3", fg="black").place(x=10, y=90)
slope_combobox = Combobox(Detail_entry, values=['1. Upsloping', '2. Flat', '3. Downsloping'], font="Arial 13", state="readonly", width=15)
slope_combobox.place(x=120, y=90)

Label(Detail_entry, text="ca:", font="arial 13", bg="#dbe0e3", fg="black").place(x=10, y=130)
ca_combobox = Combobox(Detail_entry, values=['0', '1', '2', '3', '4'], font="Arial 13", state="readonly", width=15)
ca_combobox.place(x=120, y=130)

Label(Detail_entry, text="thal:", font="arial 13", bg="#dbe0e3", fg="black").place(x=10, y=170)
thal_combobox = Combobox(Detail_entry, values=['0', '1', '2', '3', '4'], font="Arial 13", state="readonly", width=15)
thal_combobox.place(x=120, y=170)

# Labels for smoking, trestbps, chol, thalach, and oldpeak
Label(Detail_entry, text="Smoking:", font="arial 13", bg="#dbe0e3", fg="black").place(x=280, y=10)
smoking_entry = Entry(Detail_entry, font="Arial 13", bg="#dbe0e3", fg="black", width=15)
smoking_entry.place(x=400, y=10)

Label(Detail_entry, text="trestbps:", font="arial 13", bg="#dbe0e3", fg="black").place(x=280, y=50)
trestbps_entry = Entry(Detail_entry, font="Arial 13", bg="#dbe0e3", fg="black", width=15)
trestbps_entry.place(x=400, y=50)

Label(Detail_entry, text="chol:", font="arial 13", bg="#dbe0e3", fg="black").place(x=280, y=90)
chol_entry = Entry(Detail_entry, font="Arial 13", bg="#dbe0e3", fg="black", width=15)
chol_entry.place(x=400, y=90)

Label(Detail_entry, text="thalach:", font="arial 13", bg="#dbe0e3", fg="black").place(x=280, y=130)
thalach_entry = Entry(Detail_entry, font= "Arial 13", bg="#dbe0e3", fg="black", width=15)
thalach_entry.place(x=400, y=130)
Label(Detail_entry, text="oldpeak:", font="arial 13", bg="#dbe0e3", fg="black").place(x=280, y=170)
oldpeak_entry = Entry(Detail_entry, font="Arial 13", bg="#dbe0e3", fg="black", width=15)
oldpeak_entry.place(x=400, y=170)

square_report_image = PhotoImage(file="Images/Report.png")
report_background = Label(image=square_report_image, bg=background)
report_background.place(x=1120, y=400)

report = Label(root, font="arial 25 bold", bg="white", fg="#8dc63f")
report.place(x=1170, y=550)

report1 = Label(root, font="arial 10 bold", bg="white")
report1.place(x=1130, y=610)

##########################################Graph###################################################

# Load the image and scale it
graph_image = PhotoImage(file="Images/graph.png").zoom(1)

# Create labels and place them
labels = []
positions = [(600, 270), (860, 270), (600, 500), (860, 500)]

for x, y in positions:
    label = tk.Label(root, image=graph_image)
    label.place(x=x, y=y)
    labels.append(label) 

#######################################################Button###############################################
analysis_button = PhotoImage(file="Images/Analysis.png")
Button(root, image=analysis_button, bd=0, bg=background, cursor='hand2', command=analysis).place(x=1130, y=240)

###########################################info button######################################################

info_button = PhotoImage(file="Images/info.png")
Button(root, image=info_button, bd=0, bg=background, cursor='hand2', command=Info).place(x=10, y=240)

# Define the save function
def save(file_path, data):
    with open(file_path, 'w') as f:
        for item in data:
            f.write("%s\n" % item)

# Call the save function with 'file' and 'arr' arguments
save("example.txt", [1, 2, 3])

# Define a function to handle button click event
def on_save_button_click():
    # Get the file path from the user
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        # Assuming data is a list of strings
        data = [
            "G is restecg: 0",
            "H is thalach: 34",
            "I is exang: Yes",
            "J is oldpeak: 54.0",
            "K is slope: 1. Upsloping",
            "L is ca: 4",
            "M is thal: 2"
        ]
        
#############################################save button ###################################################

save_button = PhotoImage(file="Images/save.png")
Button(root, image=save_button, bd=0, bg=background, cursor='hand2',command=np.save).place(x=1370, y=250)

###########################################smoking and non smoking button####################################

button_mode = True
choice = "smoking"

def changemode():
    global button_mode
    global choice

    if button_mode:
        choice = "non_smoking"
        mode.config(image=non_smoking_icon, activebackground="white")
        button_mode = False
    else:
        choice = "smoking"
        mode.config(image=smoking_icon, activebackground="white")
        button_mode = True
        print(choice)

smoking_icon = PhotoImage(file="Images/smoker.png")
non_smoking_icon = PhotoImage(file="Images/non-smoker.png")
mode = Button(root, image=smoking_icon, bg="#dbe0e3", bd=0, cursor="hand2", command=changemode)
mode.place(x=430, y=505)

##############################################logout button###################################################

logout_icon = PhotoImage(file="Images/logout.png")
logout_button = Button(root, image=logout_icon, bg="#df2d4b", cursor="hand2", bd=0, command=logout)
logout_button.place(x=1130, y=660)
print
root.mainloop()
