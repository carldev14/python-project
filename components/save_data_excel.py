from openpyxl.styles import Font, Alignment

def Save_to_excel(open_workbook, worksheet, prepath_of_excel, formatted_date, fetched_company_name, fetched_address_name, tin_number_input, fetched_description_name, TotalAmountPaid, InputVat, CPS):
    # Get the next available row
    next_row = worksheet.max_row + 1

    # Set values for the new row
    font = Font(name="Arial", size=10)
    alignment = Alignment(horizontal='center', vertical='center')

    row_data = [
        formatted_date,
        fetched_company_name,
        fetched_address_name,
        tin_number_input,
        fetched_description_name,
        TotalAmountPaid,
        InputVat,
        CPS
    ]

    worksheet.append(row_data)

    # Update font and alignment for each cell in the new row
    for cell in worksheet[next_row]:
        cell.font = font
        cell.alignment = alignment

    # Save the workbook
    open_workbook.save(prepath_of_excel)

    print("\nData has been successfully saved.")