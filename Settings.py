import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_FILE = os.path.join(BASE_DIR, 'settings.json')


def load_settings():
    try:
        with open(SETTINGS_FILE, 'r') as file:
            settings = json.load(file)

        return settings

    except FileNotFoundError:
        return {
            "decimal_precision": 2,
            "calculation_delay": 1
        }


def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as file:
        json.dump(settings, file, indent=4)
        
def add_settings(setting_name, value):
    settings = load_settings()

    settings[setting_name] = value

    save_settings(settings)
    
    
def decimal_precision_func():
    while True:
        try:
            precision = int(input('Enter number of decimal places: '))

            if precision >= 0 and precision <= 10:
                add_settings('decimal_precision', precision)
                print(f'Decimal precision set to {precision}')
                break

            else:
                print('Error: Please enter a number between 0 and 10.')

        except ValueError:
            print('Error: Please enter a whole number.')
    
def calculation_delay_func():
    while True:
        try:
            delay = float(input('Enter calculation delay in seconds: '))

            if delay >= 0:
                add_settings('calculation_delay', delay)
                print(f'Calculation delay set to {delay} seconds')
                break

            else:
                print('Error: Delay cannot be negative.')

        except ValueError:
            print('Error: Please enter a valid number.')
            
def reset_settings():
    settings = {
        "decimal_precision": 2,
        "calculation_delay": 1
    }

    save_settings(settings)

    print("Settings have been reset to default.")
    
def format_result(result):
    settings = load_settings()
    precision = settings['decimal_precision']

    return f'{result:.{precision}f}'