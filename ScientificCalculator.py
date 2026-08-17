import math
import History
import Settings


def square_root():
    while True:
        try:
            s_num = float(input('Enter a number : '))

            if s_num >= 0:
                result_square_root = math.sqrt(s_num)
                formatted_result = Settings.format_result(result_square_root)

                print(f'Square root of {s_num} is {formatted_result}')

                History.add_history(
                    f'Square root of {s_num} is',
                    result_square_root
                )
                break

            else:
                print('Enter a non-negative number')

        except ValueError:
            print('\nError: Please enter numbers only.')


def cube_root():
    while True:
        try:
            c_num = float(input('Enter a number : '))

            result_cube_root = math.copysign(abs(c_num) ** (1 / 3), c_num)
            formatted_result = Settings.format_result(result_cube_root)

            print(f'Cube root of {c_num} is {formatted_result}')

            History.add_history(
                f'Cube root of {c_num} is',
                result_cube_root
            )
            break

        except ValueError:
            print('\nError: Please enter numbers only.')


def sin_func():
    while True:
        try:
            degree_numbr = float(input('Enter angle in degrees : '))

            radian_number = math.radians(degree_numbr)

            sin_result = math.sin(radian_number)
            formatted_result = Settings.format_result(sin_result)

            print(f'sin({degree_numbr}°) = {formatted_result}')

            History.add_history(
                f'sin({degree_numbr}°) ',
                sin_result
            )
            break

        except ValueError:
            print('\nError: Please enter numbers only.')


def cos_func():
    while True:
        try:
            degree_numbr = float(input('Enter angle in degrees : '))

            radian_number = math.radians(degree_numbr)

            cos_result = math.cos(radian_number)
            formatted_result = Settings.format_result(cos_result)

            print(f'cos({degree_numbr}°) = {formatted_result}')

            History.add_history(
                f'cos({degree_numbr}°) ',
                cos_result
            )
            break

        except ValueError:
            print('\nError: Please enter numbers only.')


def tan_func():
    while True:
        try:
            degree_numbr = float(input('Enter angle in degrees : '))

            radian_number = math.radians(degree_numbr)

            tan_result = math.tan(radian_number)
            formatted_result = Settings.format_result(tan_result)

            print(f'tan({degree_numbr}°) = {formatted_result}')

            History.add_history(
                f'tan({degree_numbr}°) ',
                tan_result
            )
            break

        except ValueError:
            print('\nError: Please enter numbers only.')


def logarithm_func():
    while True:
        try:
            l_num = float(input('Enter a number : '))

            if l_num > 0:
                result_log10 = math.log10(l_num)
                result_log = math.log(l_num)

                formatted_log10 = Settings.format_result(result_log10)
                formatted_log = Settings.format_result(result_log)

                print(f'log10({l_num}) = {formatted_log10}')
                print(f'ln({l_num}) = {formatted_log}')

                History.add_history(
                    f'log10({l_num}) ',
                    result_log10
                )

                History.add_history(
                    f'ln({l_num}) = ',
                    result_log
                )
                break

            else:
                print('Enter a positive number')

        except ValueError:
            print('\nError: Please enter numbers only.')


def factorial_func():
    while True:
        try:
            f_num = int(input('Enter a number : '))

            if f_num >= 0:
                result_factorial = math.factorial(f_num)
                formatted_result = Settings.format_result(result_factorial)

                print(f'({f_num})! = {formatted_result}')

                History.add_history(
                    f'({f_num})! ',
                    result_factorial
                )
                break

            else:
                print('Enter a positive number')

        except ValueError:
            print('\nError: Please enter numbers only.')


def asin_func():
    while True:
        try:
            num = float(input('Enter value between -1 and 1 : '))

            if -1 <= num <= 1:
                radian_result = math.asin(num)
                degree_result = math.degrees(radian_result)
                formatted_result = Settings.format_result(degree_result)

                print(f'arcsin({num}) = {formatted_result}°')

                History.add_history(
                    f'arcsin({num}) ',
                    degree_result
                )
                break

            else:
                print('Error: Value must be between -1 and 1')

        except ValueError:
            print('\nError: Please enter numbers only.')


def acos_func():
    while True:
        try:
            num = float(input('Enter value between -1 and 1 : '))

            if -1 <= num <= 1:
                radian_result = math.acos(num)
                degree_result = math.degrees(radian_result)
                formatted_result = Settings.format_result(degree_result)

                print(f'arccos({num}) = {formatted_result}°')

                History.add_history(
                    f'arccos({num}) ',
                    degree_result
                )
                break

            else:
                print('Error: Value must be between -1 and 1')

        except ValueError:
            print('\nError: Please enter numbers only.')


def atan_func():
    while True:
        try:
            num = float(input('Enter a number : '))

            radian_result = math.atan(num)
            degree_result = math.degrees(radian_result)
            formatted_result = Settings.format_result(degree_result)

            print(f'arctan({num}) = {formatted_result}°')

            History.add_history(
                f'arctan({num}) ',
                degree_result
            )
            break

        except ValueError:
            print('\nError: Please enter numbers only.')