from prompt_toolkit import prompt


def Encode_Again(open_workbook, prepath_of_excel):
    
    while True:
        result = prompt("\nDo you want to create more? (y/n) ") 
        if result.lower() == "y":
            from .input_details import InputDetails
            InputDetails(open_workbook, prepath_of_excel, prompt('\nEnter the date (052324 = May,24,2024): '), 0, 0)
        elif result.lower() == "n":
            print("\nGood bye!")
            exit()
        else:
            print("\nEnter valid answer (y/n)")