from prompt_toolkit import prompt

def FloatInput():
    while True:
        try:
            TotalAmountPaid = float(prompt('\nEnter the Total Amount Paid: '))
            InputVat = float(prompt('\nEnter the Input Vat: '))
            return TotalAmountPaid, InputVat
        except ValueError:
            print("\nError: Please enter a valid number.")