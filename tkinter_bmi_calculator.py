from tkinter import *


# code logic
def bmi_calc():
    weight = float(weight_input.get())
    height = float(height_input.get())

    raw_bmi = weight / (height ** 2)
    bmi = float("{:.2f}".format(raw_bmi))
    # print(bmi)

    if bmi < 18.5:
        bmi_result_label.config(text="Your BMI is {}, you are underweight.".format(bmi))
    elif 18.5 <= bmi < 25:
        bmi_result_label.config(text="Your BMI is {}, you have a normal weight.".format(bmi))
    elif 25 <= bmi < 30:
        bmi_result_label.config(text="Your BMI is {}, you are slightly overweight.".format(bmi))
    elif 30 <= bmi < 35:
        bmi_result_label.config(text="Your BMI is {}, you are obese.".format(bmi))
    else:
        bmi_result_label.config(
            text="Your BMI is {}, you are clinically obese. Please reach out to a doctor!".format(bmi))


# window
window = Tk()
window.title("Simple Body Mass Index (BMI) Calculator")
window.config(padx=20, pady=20)

# Entry

# Entry

weight_input = Entry(width=6)
weight_input.grid(row=0, column=1)

height_input = Entry(width=6)
height_input.grid(row=1, column=1)

# Label

weight_label = Label(text="Your height is:")
weight_label.grid(row=0, column=0)

height_label = Label(text="Your weight is:")
height_label.grid(row=1, column=0)

bmi_result_label = Label(text="0")
bmi_result_label.grid(row=3, column=1)

kg_label = Label(text="kg")
kg_label.grid(row=0, column=2)

metres_label = Label(text="meters")
metres_label.grid(row=1, column=2)

# Button

# calculate_button = Button(text="Calculate", command=tip_calc)
calculate_button = Button(text="Calculate", command=bmi_calc)
calculate_button.grid(row=2, column=1)

window.mainloop()

"""
Under 18.5 they are underweight
Equal to or over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.

sample output
"Your BMI is 18.28678, you are underweight."
"Your BMI is 22.0, you have a normal weight."
"Your BMI is 28.50752, you are slightly overweight."
"Your BMI is 32.56189, you are obese."
"Your BMI is 37.50000, you are clinically obese."
"""
