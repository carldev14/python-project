import datetime

def parse_date(input_str: str) -> tuple:
    # Remove any dots in the input string
    input_str = input_str.replace('.', '')
    
    # Extract month, day, and year components from the input string
    month = int(input_str[:2])
    day = int(input_str[2:4])
    year = int(input_str[4:])
    
    # Determine the correct century for the year component
    if year >= 0 and year <= 21:
        year += 2000
    else:
        year += 1900
    
    # Calculate the last two digits of the year
    year %= 100
    
    # Get the abbreviated month name
    month_abbr = datetime.date(year, month, day).strftime("%b")
    
    # Format the date string
    formatted_date = f"{day}-{month_abbr}-{year}"
    
    return formatted_date, input_str, month

def ChoiceSheet(month, open_workbook):
    month_names = {
        '01': 'January', '02': 'February', '03': 'March', '04': 'April',
        '05': 'May', '06': 'June', '07': 'July', '08': 'August',
        '09': 'September', '10': 'October', '11': 'November', '12': 'December'
    }
    sheet_name = month_names.get(month)
    if sheet_name:
        worksheet = open_workbook[sheet_name]
        return worksheet
    else:
        print('Sheet not found')
        return None