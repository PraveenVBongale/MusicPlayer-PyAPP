from tkinter import *
class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.configure(background="green")

        Label1(window, font="Ariel 12 bold", bg="green", text="Annual Interest Rate").grid(row=1, column=1, sticky=W)
        Label2(window, font="Ariel 12 bold", bg="green", text="Number of Years").grid(row=2, column=1, sticky=W)
        Label3(window, font="Ariel 12 bold", bg="green", text="Loan Amount").grid(row=3, column=1, sticky=W)
        Label4(window, font="Ariel 12 bold", bg="green", text="Monthly Payment").grid(row=4, column=1, sticky=W)
        Label5(window, font="Ariel 12 bold", bg="green", text="Total Amount").grid(row=5, column=1, sticky=W)

        self.annualInterestRateVar=StringVar()
        Entry(window, textvariable=self.annualInterestRateVar),
        justify=RIGHT.grid(row=1, column=2)
        self.numberofYearsVar=StringVar()
        Entry(window, textvariable=self.numberofYearsVar),
        justify=RIGHT.grid(row=2, column=2)
        self.loanAmountVar=StringVar()
        Entry(window, textvariable=self.loanAmountVar),
        justify=RIGHT.grid(row=3, column=2)
        self.monthlyPaymentVar=StringVar()
        lblMonthlyPayment = Label(window, font="Calibri 12 bold", bg="green", textVariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)

        self.totalPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, font="Calibri 12 bold", bg="green", textVariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)

        btComputePayment = Button(window, text="Compute Payment", bg="red", fg="white", font="Calibri 14 bold", command=self.ComputePayment).grid(row=6, column=2, sticky=E)
        btClear = Button(window, text="Clear", bg="blue", fg = "white", font = "Calibri 14 bold", command = self.delete_all).grid(row=6, column=8, padx=20, pady=20, sticky=E)

        window.mainloop()

    def ComputePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) /1200,
            int(self.numberofYearsVar.get()))

        self.monthlyPaymentVar.set(format (monthlyPayment, "10,20" ))
        totalPayment = float(self.monthlyPaymentVar.get())*12\
                   *int(self.numberofYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, "10,20"))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberofYears):
        monthlyPayment = loanAmount * monthlyInterestRate /(1-1/(1+monthlyInterestRate)**(numberofYears*12))
        return monthlyPayment

    def delete_all(self):
        self.monthlyPaymentVar.set(" ")
        self.loanAmountVar.set(" ")
        self.annualInterestRateVar.set(" ")
        self.numberofYearsVar.set(" ")
        self.totalPaymentVar.set(" ")

LoanCalculator()