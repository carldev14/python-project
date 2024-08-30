from prompt_toolkit import prompt

def TIN():
    while True:
        tin_number = prompt('\nEnter the TIN number: ')
        if tin_number == "":
            print('\nFill the blank\n')
        else:
            return tin_number