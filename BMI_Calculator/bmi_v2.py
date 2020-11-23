"""
Created on 23.11.2020

@author: dafr
"""
import tkinter

root = tkinter.Tk()
#root.geometry("300x100")
root.title("BMI Calculator")

# Functions

def calculate_bmi():
    kg = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round(kg / (height ** 2), 2)
    label_result["text"] = f"BMI: {bmi}"

def advice():
    if bmi>30 or bmi<18.5:
        label_advice["text"] = "Your health is in danger.\n You should consult a doctor!"

    else:
        label_advice["text"] = "Your BMI is normal"


# Create GUI
label_kg = tkinter.Label(root, text= "KG: ")
label_kg.grid(column=0, row=0)

entry_kg = tkinter.Entry(root)
entry_kg.grid(column=1, row=0)

label_height = tkinter.Label(root, text= "Height: ")
label_height.grid(column=0, row=1)

entry_height = tkinter.Entry(root)
entry_height.grid(column=1, row=1)

button_calculate = tkinter.Button(root, text="Calculate", command=(calculate_bmi, advice))
button_calculate.grid(column=0, row=2)

label_result = tkinter.Label(root, text= "BMI: ")
label_result.grid(column=1, row=2)

label_comment = tkinter.Label(root, text= "Comment: ")
label_comment.grid(column=0, row=3)

label_advice = tkinter.Label(root, text="")
label_advice.grid(column=1, row=3)




root.mainloop()
