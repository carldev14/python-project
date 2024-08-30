import sys
import os
from prompt_toolkit import prompt
# Add the path to the components directory
sys.path.append(os.path.abspath('./components'))

# Import the function
from get_xlsx import Get_Xlsx
from input_details import InputDetails

if __name__ == "__main__":
    open_workbook, prepath_of_excel = Get_Xlsx()
    InputDetails(open_workbook, prepath_of_excel, prompt('\nEnter the date (052324 = May,24,2024): '), 0, 0)
    
    