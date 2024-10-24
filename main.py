
from prompt_toolkit import prompt
# Add the path to the components directory


# Import the function
from components.get_xlsx import Get_Xlsx
from components.input_details import InputDetails

if __name__ == "__main__":
    open_workbook, prepath_of_excel = Get_Xlsx()
    InputDetails(open_workbook, prepath_of_excel, prompt('\nEnter the date (052324 = May,24,2024): '), 0, 0)
    
    