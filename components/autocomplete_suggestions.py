import json
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# Load JSON data from the file
def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return an empty dict if the file does not exist or is corrupted

# Save JSON data back to the file
def save_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to prompt the user with autocomplete suggestions and save new entries
def Autocomplete_suggestions(prompt_message, collection_key, file_path):
    data = load_data(file_path)
    # Get the current options from the specific collection
    current_options = data.get(collection_key, [])
    
    # Create a WordCompleter with the current options
    completer = WordCompleter(current_options, ignore_case=True)
    
    # Prompt the user for input with autocomplete
    main_input_3 = prompt(f"\nEnter the {prompt_message}: ", completer=completer)
    
    # Check if the input exists in the collection
    if main_input_3 in current_options:
        print(f"You selected: {main_input_3}")
    else:
        print(f"'{main_input_3}' not found. Adding it to the collection.")
        current_options.append(main_input_3)
        data[collection_key] = current_options
        save_data(data, file_path)
        print(f"New entry '{main_input_3}' added to {collection_key}.")
    
    return main_input_3

# Define the path to the JSON file
file_path = 'database.json'

# Prompt for different inputs and save the selected or new entries
def Company():
    return Autocomplete_suggestions("Company name", 'company_list', file_path)

def Address():
    return Autocomplete_suggestions("Address name", 'address_list', file_path)

def Description():
    return Autocomplete_suggestions("Description name", 'description_list', file_path)







