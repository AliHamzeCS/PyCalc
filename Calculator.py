def addition():
    try:
        first_number = int(input('Enter the first number : '))
        second_number = int(input('Enter the second number : '))

        print(f'\nResult {first_number} + {second_number} = {first_number + second_number}')

    except ValueError:
        print('\nError: Please enter numbers only.')


def subtraction():
    try:
        first_number = int(input('Enter the first number : '))
        second_number = int(input('Enter the second number : '))

        print(f'\nResult {first_number} - {second_number} = {first_number - second_number}')

    except ValueError:
        print('\nError: Please enter numbers only.')


def multiplication():
    try:
        first_number = int(input('Enter the first number : '))
        second_number = int(input('Enter the second number : '))

        print(f'\nResult {first_number} × {second_number} = {first_number * second_number}')

    except ValueError:
        print('\nError: Please enter numbers only.')


def division():
    try:
        first_number = int(input('Enter the first number : '))
        second_number = int(input('Enter the second number : '))

        print(f'\nResult {first_number} / {second_number} = {first_number / second_number}')

    except ValueError:
        print('\nError: Please enter numbers only.')

    except ZeroDivisionError:
        print('\nError: Cannot divide by zero.')


def power():
    try:
        first_number = int(input('Enter the first number : '))
        second_number = int(input('Enter the second number : '))

        print(f'\nResult {first_number} ^ {second_number} = {first_number ** second_number}')

    except ValueError:
        print('\nError: Please enter numbers only.')


def modulus():
    try:
        first_number = int(input('Enter the first number : '))
        second_number = int(input('Enter the second number : '))

        print(f'\nResult {first_number} % {second_number} = {first_number % second_number}')

    except ValueError:
        print('\nError: Please enter numbers only.')

    except ZeroDivisionError:
        print('\nError: Cannot use zero as the second number.')