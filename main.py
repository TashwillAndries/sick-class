# Tashwill Andries
# importing everything from tkinter
from tkinter import *
from tkinter import messagebox


sick = Tk()
sick.title("Sick Class")
sick.config(bg="orange")
sick.geometry("700x600")

# the layout
code_label = Label(sick, text="SicknessCode:", bg="orange")
code_label.place(x=50, y=51)
code_entry = Entry(sick)
code_entry.place(x=250, y=51)
duration_label = Label(sick, text="DurationOfTreatment:", bg="orange")
duration_label.place(x=50, y=100)
duration_entry = Entry(sick, width=15)
duration_entry.place(x=250, y=100)
weeks_label = Label(sick, text="Week/Months", bg="orange")
weeks_label.place(x=420, y=100)
practice_label = Label(sick, text="DoctorsPracticeNumber:", bg="orange")
practice_label.place(x=50, y=160)
practice_entry = Entry(sick)
practice_entry.place(x=250, y=160)
fee_label = Label(sick, text="Scan/Consultation fee:", bg="orange")
fee_label.place(x=50, y=230)
fee_entry = Entry(sick)
fee_entry.place(x=250, y=230)

var = StringVar()

# radio buttons
cancer_button = Radiobutton(sick, text="Cancer", variable=var, value="Cancer", bg="orange")
cancer_button.place(x=50, y=280)
influenza_button = Radiobutton(sick, text="Influenza", variable=var, value="Influenza", bg="orange")
influenza_button.place(x=50, y=330)

# amount paid
amount_label = Label(sick, text="AmountPaidForTreatment:", bg="orange")
amount_label.place(x=50, y=400)
answer_label = Label(sick, bg="orange")
answer_label.place(x=420, y=400)


# functions
class Sick:
    def patient(self):
        self.code = code_entry
        self.duration = duration_entry
        self.practice = practice_entry
        self.cancer = 450
        self.influenza = 350.50


def sickness():
    if var.get() == "Cancer":
        if int(fee_entry.get()) >= 600:

            messagebox.showinfo("Message", "Sorry we cannot treat you")
        elif int(fee_entry.get()) < 600:
            cancer_amount = int(fee_entry.get()) + 400

            answer_label.config(text=str(cancer_amount))
# influenza function
    if var.get() == "Influenza":
        if int(fee_entry.get()) < 600:
            influenza_answer = 350.50 + int(fee_entry.get())
            answer_label.config(text=str(influenza_answer))
        elif int(fee_entry.get()) >= 600:
            influenza_answer = 350.50 + int(fee_entry.get())
            discount = (influenza_answer * (2/100)) + influenza_answer
            messagebox.showinfo("Message", "2% discount")
            answer_label.config(text=str(discount))


# function to clear everything
def clear():
    code_entry.delete(0, END)
    duration_entry.delete(0, END)
    practice_entry.delete(0, END)
    fee_entry.delete(0, END)
    answer_label.config(text="")


calculate = Button(sick, text="Calculate", command=sickness)
calculate.place(x=50, y=490)
clear_button = Button(sick, text="Clear", command=clear)
clear_button.place(x=250, y=490)

sick.mainloop()

