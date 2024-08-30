import os
from prompt_toolkit import prompt
from openpyxl import load_workbook

print("\nWelcome to Excel Automated.")

# Function to get the xlsx file
def Get_Xlsx():
    while True:
        nameFile = prompt('\nEnter the name of the xlsx file: ')
        # Adjust the relative path to be correct based on the directory structure
        prepath_of_excel = os.path.join(os.path.dirname(__file__), '../xlsx_folder', f"{nameFile}.xlsx")
        
        if not os.path.isfile(prepath_of_excel):
            print('\nFile not found')
        else:
            open_workbook = load_workbook(prepath_of_excel)
            break
    
    return open_workbook, prepath_of_excel


    

