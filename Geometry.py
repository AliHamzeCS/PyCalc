from colorama import Fore, Style, init
init()
import History
import Settings
import math


def circle():
    try:
        r = float(input('redius : '))

        result_area = math.pi * r * r
        result_circumference = 2 * math.pi * r
        result_diameter = 2 * r

        formatted_area = Settings.format_result(result_area)
        formatted_circumference = Settings.format_result(result_circumference)
        formatted_diameter = Settings.format_result(result_diameter)

        print(f"{Fore.MAGENTA}Area = {Style.RESET_ALL}. {formatted_area}")
        print(f"{Fore.MAGENTA}Circumference = {Style.RESET_ALL}. {formatted_circumference}")
        print(f"{Fore.MAGENTA}Diameter = {Style.RESET_ALL}. {formatted_diameter}")

        History.add_history(f'Area = ', result_area)
        History.add_history(f'Circumference = ', result_circumference)
        History.add_history(f'Diameter = ', result_diameter)

    except ValueError:
        print('\nError: Please enter numbers only.')


def rectangle():
    try:
        l = float(input('length : '))
        w = float(input('width : '))

        result_area = l * w
        result_perimeter = 2 * (l + w)
        result_diagonal = math.sqrt(l**2 + w**2)

        formatted_area = Settings.format_result(result_area)
        formatted_perimeter = Settings.format_result(result_perimeter)
        formatted_diagonal = Settings.format_result(result_diagonal)

        print(f"{Fore.MAGENTA}Area = {Style.RESET_ALL}. {formatted_area}")
        print(f"{Fore.MAGENTA}Perimeter = {Style.RESET_ALL}. {formatted_perimeter}")
        print(f"{Fore.MAGENTA}Diagonal = {Style.RESET_ALL}. {formatted_diagonal}")

        History.add_history(f'Area = ', result_area)
        History.add_history(f'Perimeter = ', result_perimeter)
        History.add_history(f'Diagonal = ', result_diagonal)

    except ValueError:
        print('\nError: Please enter numbers only.')


def square():
    try:
        s = float(input('side : '))

        result_area = s * s
        result_perimeter = 4 * s
        result_diagonal = (math.sqrt(2)) * s

        formatted_area = Settings.format_result(result_area)
        formatted_perimeter = Settings.format_result(result_perimeter)
        formatted_diagonal = Settings.format_result(result_diagonal)

        print(f"{Fore.MAGENTA}Area = {Style.RESET_ALL}. {formatted_area}")
        print(f"{Fore.MAGENTA}Perimeter = {Style.RESET_ALL}. {formatted_perimeter}")
        print(f"{Fore.MAGENTA}Diagonal = {Style.RESET_ALL}. {formatted_diagonal}")

        History.add_history(f'Area = ', result_area)
        History.add_history(f'Perimeter = ', result_perimeter)
        History.add_history(f'Diagonal = ', result_diagonal)

    except ValueError:
        print('\nError: Please enter numbers only.')


def triangle():
    try:
        b = float(input('base : '))
        h = float(input('height : '))

        side_1 = float(input('side 1 : '))
        side_2 = float(input('side 2 : '))
        side_3 = float(input('side 3 : '))

        result_area = (b * h) / 2
        result_perimeter = side_1 + side_2 + side_3

        formatted_area = Settings.format_result(result_area)
        formatted_perimeter = Settings.format_result(result_perimeter)

        print(f"{Fore.MAGENTA}Area = {Style.RESET_ALL}. {formatted_area}")
        print(f"{Fore.MAGENTA}Perimeter = {Style.RESET_ALL}. {formatted_perimeter}")

        History.add_history(f'Area = ', result_area)
        History.add_history(f'Perimeter = ', result_perimeter)

    except ValueError:
        print('\nError: Please enter numbers only.')


def cube():
    try:
        s = float(input('side : '))

        result_volume = s * s * s
        result_total_surface_area = 6 * s * s
        result_diagonal = (math.sqrt(3)) * s

        formatted_volume = Settings.format_result(result_volume)
        formatted_total_surface_area = Settings.format_result(result_total_surface_area)
        formatted_diagonal = Settings.format_result(result_diagonal)

        print(f"{Fore.MAGENTA}Volume = {Style.RESET_ALL}. {formatted_volume}")
        print(f"{Fore.MAGENTA}Total Surface Area = {Style.RESET_ALL}. {formatted_total_surface_area}")
        print(f"{Fore.MAGENTA}Diagonal = {Style.RESET_ALL}. {formatted_diagonal}")

        History.add_history(f'Volume = ', result_volume)
        History.add_history('Total Surface Area = ', result_total_surface_area)
        History.add_history(f'Diagonal = ', result_diagonal)

    except ValueError:
        print('\nError: Please enter numbers only.')


def sphere():
    try:
        r = float(input('radius : '))

        result_volume = (4 / 3) * math.pi * r**3
        result_surface_area = 4 * math.pi * r**2
        result_diameter = 2 * r

        formatted_volume = Settings.format_result(result_volume)
        formatted_surface_area = Settings.format_result(result_surface_area)
        formatted_diameter = Settings.format_result(result_diameter)

        print(f"{Fore.MAGENTA}Volume = {Style.RESET_ALL}. {formatted_volume}")
        print(f"{Fore.MAGENTA}Surface Area = {Style.RESET_ALL}. {formatted_surface_area}")
        print(f"{Fore.MAGENTA}Diameter = {Style.RESET_ALL}. {formatted_diameter}")

        History.add_history(f'Volume = ', result_volume)
        History.add_history('Surface Area = ', result_surface_area)
        History.add_history(f'Diameter = ', result_diameter)

    except ValueError:
        print('\nError: Please enter numbers only.')


def cylinder():
    try:
        r = float(input('radius : '))
        h = float(input('height : '))

        result_volume = math.pi * r**2 * h
        result_total_surface_area = (math.pi * r * h) + (2 * math.pi * r**2)
        result_Lateral_Surface_Area = 2 * math.pi * r * h

        formatted_volume = Settings.format_result(result_volume)
        formatted_total_surface_area = Settings.format_result(result_total_surface_area)
        formatted_Lateral_Surface_Area = Settings.format_result(result_Lateral_Surface_Area)

        print(f"{Fore.MAGENTA}Volume = {Style.RESET_ALL}. {formatted_volume}")
        print(f"{Fore.MAGENTA}Total Surface Area = {Style.RESET_ALL}. {formatted_total_surface_area}")
        print(f"{Fore.MAGENTA}Lateral Surface Area = {Style.RESET_ALL}. {formatted_Lateral_Surface_Area}")

        History.add_history(f'Volume = ', result_volume)
        History.add_history('Total Surface Area = ', result_total_surface_area)
        History.add_history('Lateral Surface Area = ', result_Lateral_Surface_Area)

    except ValueError:
        print('\nError: Please enter numbers only.')