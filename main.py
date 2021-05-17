from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


def clear():
    en_BMI.config(state="normal")
    en_BMI.delete(0, END)
    en_BMI.config(state="readonly")

    en_I_BMI.config(state="normal")
    en_I_BMI.delete(0, END)
    en_I_BMI.config(state="readonly")

    en_Age.delete(0, END)

    en_Weight.delete(0, END)

    en_Height.delete(0, END)

    lbl_Status["text"] = ""


def ex():
    exit()


def cal():
    try:
        if cmb_Gender.get() == "Female":
            global WeightStatus
            weight = float(en_Weight.get())
            height = float(en_Height.get())
            age = int(en_Age.get())

            bmi = weight / ((height / 100) * (height / 100))

            i_bmi = 0.5 * weight / ((height/100)*(height/100)) + 0.03 * age + 11

            en_BMI.config(state="normal")
            en_BMI.delete(0, END)
            en_BMI.insert(0, bmi)
            en_BMI.config(state="readonly")

            en_I_BMI.config(state="normal")
            en_I_BMI.delete(0, END)
            en_I_BMI.insert(0, i_bmi)
            en_I_BMI.config(state="readonly")

            if bmi < 18:
                lbl_Status["text"] = "Underweight"
            elif (bmi >= 18) or (bmi < 25):
                lbl_Status["text"] = "Normal"
            elif (bmi >= 25) or (bmi < 30):
                lbl_Status["text"] = "Overweight"
            elif bmi >= 30:
                lbl_Status["text"] = "Obese"
        elif cmb_Gender.get() == "Male":
            weight = float(en_Weight.get())
            height = float(en_Height.get())

            bmi = weight / ((height / 100) * (height / 100))

            i_bmi = 0.5 * weight / ((height/100)*(height/100)) + 11.5

            en_BMI.config(state="normal")
            en_BMI.delete(0, END)
            en_BMI.insert(0, bmi)
            en_BMI.config(state="readonly")

            en_I_BMI.config(state="normal")
            en_I_BMI.delete(0, END)
            en_I_BMI.insert(0, i_bmi)
            en_I_BMI.config(state="readonly")

            if bmi < 18:
                lbl_Status["text"] = "Underweight"
            elif (bmi >= 18) or (bmi < 25):
                lbl_Status["text"] = "Normal"
            elif (bmi >= 25) or (bmi < 30):
                lbl_Status["text"] = "Overweight"
            elif bmi >= 30:
                lbl_Status["text"] = "Obese"
        else:
            messagebox.showerror("Error", "Gender not Defined")
    except ValueError as error:
        messagebox.showerror("Error", error)


BMI = Tk()
BMI.title("Ideal Body Mass Index")
BMI.geometry("900x800")

# code start

# heading start
lbl_head1 = Label(BMI, text="Ideal Body Mass Index")
lbl_head1["font"] = "Times", 40
lbl_head1.place(x=350, y=50)

lbl_head2 = Label(BMI, text="Calculator")
lbl_head2["font"] = "Times", 40
lbl_head2.place(x=500, y=100)
# heading end

# Subheading start
lbl_Sub = Label(BMI, text="Enter your Weight, Height and Gender")
lbl_Sub["font"] = "Times", 25
lbl_Sub.place(x=150, y=175)
# Subheading end

# Frame start
fm_Input = LabelFrame(BMI, borderwidth=10)
fm_Input.place(x=50, y=225, height=250, width=800)
# Frame end

# Inside Frame start
# Weight start
lbl_Weight = Label(fm_Input, text="Weight:")
lbl_Weight["font"] = "Ariel", 20
lbl_Weight.place(x=40, y=40)

en_Weight = Entry(fm_Input)
en_Weight["font"] = "Ariel", 20
en_Weight.place(x=150, y=35, width=200, height=50)

lbl_Kilograms = Label(fm_Input, text="Kilograms")
lbl_Kilograms["font"] = "Ariel", 20
lbl_Kilograms.place(x=370, y=40)
# Weight end

# Height start
lbl_Height = Label(fm_Input, text="Height:")
lbl_Height["font"] = "Ariel", 20
lbl_Height.place(x=40, y=95)

en_Height = Entry(fm_Input)
en_Height["font"] = "Ariel", 20
en_Height.place(x=150, y=90, width=200, height=50)

lbl_Cm = Label(fm_Input, text="cm")
lbl_Cm["font"] = "Ariel", 20
lbl_Cm.place(x=370, y=95)
# Height end

# Gender start
lbl_Gender = Label(fm_Input, text="Gender:")
lbl_Gender["font"] = "Ariel", 20
lbl_Gender.place(x=40, y=150)

cmb_Gender = Combobox(fm_Input)
cmb_Gender['values'] = ('Male', 'Female')
cmb_Gender["font"] = "Ariel", 20
cmb_Gender.config(state="readonly")
cmb_Gender.place(x=150, y=150, height=40, width=200)
# Gender end

# Age start
lbl_Age = Label(fm_Input, text="Age:")
lbl_Age["font"] = "Ariel", 20
lbl_Age.place(x=370, y=150)

en_Age = Entry(fm_Input)
en_Age["font"] = "Ariel", 20
en_Age.place(x=450, y=140, width=200, height=50)
# Age end
# Inside Frame end

# Cal-Button start
btn_Cal = Button(BMI, text="Calculate Your Ideal Body Mass Index", borderwidth=10, command=cal)
btn_Cal["font"] = "Ariel", 20
btn_Cal.place(x=50, y=500, width=800)
# Cal-Button end

# BMI bottom start
# BMI start
lbl_BMI = Label(BMI, text="BMI:")
lbl_BMI["font"] = "Ariel", 20
lbl_BMI.place(x=50, y=600)

en_BMI = Entry(BMI)
en_BMI["font"] = "Ariel", 20
en_BMI.config(state="readonly")
en_BMI.place(x=120, y=595, width=200, height=50)
# BMI end

# I-BMI start
lbl_I_BMI = Label(BMI, text="Ideal BMI:")
lbl_I_BMI["font"] = "Ariel", 20
lbl_I_BMI.place(x=350, y=600)

en_I_BMI = Entry(BMI)
en_I_BMI["font"] = "Ariel", 20
en_I_BMI.config(state="readonly")
en_I_BMI.place(x=500, y=595, width=200, height=50)
# I-BMI end
# BMI bottom end

# Bottom Buttons start
btn_Clear = Button(BMI, text="Clear", borderwidth=10, command=clear)
btn_Clear["font"] = "Ariel", 20
btn_Clear.place(x=50, y=700, width=200, height=70)

lbl_Status = Label(BMI)
lbl_Status["font"] = "Ariel", 20
lbl_Status.place(x=300, y=700)

btn_Exit = Button(BMI, text="Exit", borderwidth=10, command=ex)
btn_Exit["font"] = "Ariel", 20
btn_Exit.place(x=650, y=700, width=200, height=70)
# Bottom Buttons end

# code end

BMI.mainloop()
