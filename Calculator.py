import History
import Settings


def addition():
    try:
        first_number = int(input('Enter the first number : '))
        second_number = int(input('Enter the second number : '))

        result = first_number + second_number
        formatted_result = Settings.format_result(result)

        print(f'\nResult {first_number} + {second_number} = {formatted_result}')
        
        History.add_history(
            f'{first_number} + {second_number}',
            result
        )

    except ValueError:
        print('\nError: Please enter numbers only.')


def subtraction():
    try:
        first_number = int(input('Enter the first number : '))
        second_number = int(input('Enter the second number : '))

        result = first_number - second_number
        formatted_result = Settings.format_result(result)

        print(f'\nResult {first_number} - {second_number} = {formatted_result}')
                
        History.add_history(
            f'{first_number} - {second_number}',
            result
        )

    except ValueError:
        print('\nError: Please enter numbers only.')


def multiplication():
    try:
        first_number = int(input('Enter the first number : '))
        second_number = int(input('Enter the second number : '))

        result = first_number * second_number
        formatted_result = Settings.format_result(result)

        print(f'\nResult {first_number} × {second_number} = {formatted_result}')
                        
        History.add_history(
            f'{first_number} × {second_number}',
            result
        )

    except ValueError:
        print('\nError: Please enter numbers only.')


def division():
    try:
        first_number = int(input('Enter the first number : '))
        second_number = int(input('Enter the second number : '))

        result = first_number / second_number
        formatted_result = Settings.format_result(result)

        print(f'\nResult {first_number} / {second_number} = {formatted_result}')
                                
        History.add_history(
            f'{first_number} / {second_number}',
            result
        )

    except ValueError:
        print('\nError: Please enter numbers only.')

    except ZeroDivisionError:
        print('\nError: Cannot divide by zero.')


def power():
    try:
        first_number = int(input('Enter the first number : '))
        second_number = int(input('Enter the second number : '))

        result = first_number ** second_number
        formatted_result = Settings.format_result(result)

        print(f'\nResult {first_number} ^ {second_number} = {formatted_result}')
                                
        History.add_history(
            f'{first_number} ^ {second_number}',
            result
        )

    except ValueError:
        print('\nError: Please enter numbers only.')


def modulus():
    try:
        first_number = int(input('Enter the first number : '))
        second_number = int(input('Enter the second number : '))

        result = first_number % second_number
        formatted_result = Settings.format_result(result)

        print(f'\nResult {first_number} % {second_number} = {formatted_result}')
                                
        History.add_history(
            f'{first_number} % {second_number}',
            result
        )

    except ValueError:
        print('\nError: Please enter numbers only.')

    except ZeroDivisionError:
        print('\nError: Cannot use zero as the second number.')