from prompt_toolkit import prompt
from autocomplete_suggestions import Company, Address, Description
from choice_sheet import ChoiceSheet, parse_date
from tin_input import TIN
from float_input import FloatInput

from save_data_excel import Save_to_excel


def InputDetails(open_workbook, prepath_of_excel,  input_str, TotalAmountPaid, InputVat):
    
    try:
        formatted_date, input_str, month = parse_date(input_str)
    except ValueError:
        print("\nInvalid date format. Please enter the date in the format MMDDYY.")
        return
    
    fetched_company_name = Company()
    fetched_address_name = Address()
    fetched_description_name = Description()
    tin_number_input = TIN()
    TotalAmountPaid, InputVat = FloatInput()
    
    # Calculate CPS
    CPS = round(TotalAmountPaid - InputVat, 2)
    
    worksheet = ChoiceSheet(str(month).zfill(2), open_workbook)
    
    # Confirm Details
    print('\nConfirm Details:\n')
    print(f'Date: {formatted_date}')
    print(f'Company: {fetched_company_name}')
    print(f'Address: {fetched_address_name}')
    print(f'TIN: {tin_number_input}')
    print(f'Description: {fetched_description_name}')
    print(f'Total Amount Paid: {TotalAmountPaid}')
    print(f'Input Vat: {InputVat}')
    print(f'Cost of Product and Services: {CPS}')

    while True:
        y_or_n = input('\nAre the details correct? (y/n): ')
        if y_or_n.lower() == 'y':
            Save_to_excel(open_workbook, worksheet, prepath_of_excel, formatted_date, fetched_company_name, fetched_address_name, tin_number_input, fetched_description_name, TotalAmountPaid, InputVat, CPS)
            from Encode_again import Encode_Again
            Encode_Again(open_workbook, prepath_of_excel)
        elif y_or_n.lower() == 'n':
            InputDetails(prompt('\nEnter the date (052324 = May,24,2024): '), 0, 0)
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

