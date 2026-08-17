from colorama import Fore, Style, init
init()

import math
import History
import Settings


# Get a valid number from the user
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(f"{Fore.YELLOW}Error: Please enter a valid number.{Style.RESET_ALL}")


# Quadratic Equation
def solve_quadratic_equation():

    print("Quadratic equation: ax² + bx + c = 0")

    while True:
        a = get_number("a: ")

        if a != 0:
            break

        print("Error: 'a' cannot be 0 in a quadratic equation.")

    b = get_number("b: ")
    c = get_number("c: ")

    D = b * b - 4 * a * c
    formatted_D = Settings.format_result(D)

    print(f"\nEquation: {a}x² + {b}x + {c} = 0")
    print(f"Discriminant (D) = {formatted_D}")

    if D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)

        formatted_x1 = Settings.format_result(x1)
        formatted_x2 = Settings.format_result(x2)

        print(f"Two real roots: x1 = {formatted_x1}, x2 = {formatted_x2}")

        History.add_history(
            f"{a}x² + {b}x + {c} = 0",
            f"x1 = {x1}, x2 = {x2}"
        )

    elif D == 0:
        x1 = -b / (2 * a)

        formatted_x1 = Settings.format_result(x1)

        print(f"One real root: x1 = {formatted_x1}")

        History.add_history(
            f"{a}x² + {b}x + {c} = 0",
            f"x1 = {x1}"
        )

    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-D) / (2 * a)

        formatted_real_part = Settings.format_result(real_part)
        formatted_imag_part = Settings.format_result(imag_part)

        print(
            f"Two complex roots: "
            f"{formatted_real_part} + {formatted_imag_part}i , "
            f"{formatted_real_part} - {formatted_imag_part}i"
        )

        History.add_history(
            f"{a}x² + {b}x + {c} = 0",
            f"{real_part} + {imag_part}i , "
            f"{real_part} - {imag_part}i"
        )


# System Of Two Equations
def solve_system_two_equations():

    print("a1*x + b1*y = c1")
    print("a2*x + b2*y = c2")

    a1 = get_number("a1: ")
    b1 = get_number("b1: ")
    c1 = get_number("c1: ")

    a2 = get_number("a2: ")
    b2 = get_number("b2: ")
    c2 = get_number("c2: ")

    print(f"\n{a1}x + {b1}y = {c1}")
    print(f"{a2}x + {b2}y = {c2}")

    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1

    if D != 0:
        x = Dx / D
        y = Dy / D

        formatted_x = Settings.format_result(x)
        formatted_y = Settings.format_result(y)

        print(f"Unique solution: x = {formatted_x}, y = {formatted_y}")

        History.add_history(
            f"{a1}x + {b1}y = {c1} | "
            f"{a2}x + {b2}y = {c2}",
            f"x = {x}, y = {y}"
        )

    else:
        if Dx == 0 and Dy == 0:
            print("Infinite solutions")

            History.add_history(
                f"{a1}x + {b1}y = {c1} | "
                f"{a2}x + {b2}y = {c2}",
                "Infinite solutions"
            )

        else:
            print("No solution")

            History.add_history(
                f"{a1}x + {b1}y = {c1} | "
                f"{a2}x + {b2}y = {c2}",
                "No solution"
            )


# System Of Three Equations
def solve_system_three_equations():

    print("a1*x + b1*y + c1*z = d1")
    print("a2*x + b2*y + c2*z = d2")
    print("a3*x + b3*y + c3*z = d3")

    a1 = get_number("a1: ")
    b1 = get_number("b1: ")
    c1 = get_number("c1: ")
    d1 = get_number("d1: ")

    a2 = get_number("a2: ")
    b2 = get_number("b2: ")
    c2 = get_number("c2: ")
    d2 = get_number("d2: ")

    a3 = get_number("a3: ")
    b3 = get_number("b3: ")
    c3 = get_number("c3: ")
    d3 = get_number("d3: ")

    print(f"\n{a1}x + {b1}y + {c1}z = {d1}")
    print(f"{a2}x + {b2}y + {c2}z = {d2}")
    print(f"{a3}x + {b3}y + {c3}z = {d3}")

    D = (
        a1 * (b2 * c3 - b3 * c2)
        - b1 * (a2 * c3 - a3 * c2)
        + c1 * (a2 * b3 - a3 * b2)
    )

    Dx = (
        d1 * (b2 * c3 - b3 * c2)
        - b1 * (d2 * c3 - d3 * c2)
        + c1 * (d2 * b3 - d3 * b2)
    )

    Dy = (
        a1 * (d2 * c3 - d3 * c2)
        - d1 * (a2 * c3 - a3 * c2)
        + c1 * (a2 * d3 - a3 * d2)
    )

    Dz = (
        a1 * (b2 * d3 - b3 * d2)
        - b1 * (a2 * d3 - a3 * d2)
        + d1 * (a2 * b3 - a3 * b2)
    )

    if D != 0:
        x = Dx / D
        y = Dy / D
        z = Dz / D

        formatted_x = Settings.format_result(x)
        formatted_y = Settings.format_result(y)
        formatted_z = Settings.format_result(z)

        print(
            f"Unique solution: "
            f"x = {formatted_x}, "
            f"y = {formatted_y}, "
            f"z = {formatted_z}"
        )

        History.add_history(
            f"{a1}x + {b1}y + {c1}z = {d1} | "
            f"{a2}x + {b2}y + {c2}z = {d2} | "
            f"{a3}x + {b3}y + {c3}z = {d3}",
            f"x = {x}, y = {y}, z = {z}"
        )

    else:
        if Dx == 0 and Dy == 0 and Dz == 0:
            print("Infinite solutions")

            History.add_history(
                f"{a1}x + {b1}y + {c1}z = {d1} | "
                f"{a2}x + {b2}y + {c2}z = {d2} | "
                f"{a3}x + {b3}y + {c3}z = {d3}",
                "Infinite solutions"
            )

        else:
            print("No solution")

            History.add_history(
                f"{a1}x + {b1}y + {c1}z = {d1} | "
                f"{a2}x + {b2}y + {c2}z = {d2} | "
                f"{a3}x + {b3}y + {c3}z = {d3}",
                "No solution"
            )


# Discriminant & Root Analysis
def discriminant_analysis():

    print("Quadratic equation: ax² + bx + c = 0")

    while True:
        a = get_number("a: ")

        if a != 0:
            break

        print("Error: 'a' cannot be 0 in a quadratic equation.")

    b = get_number("b: ")
    c = get_number("c: ")

    D = b * b - 4 * a * c
    formatted_D = Settings.format_result(D)

    print(f"\nDiscriminant (D) = {formatted_D}")

    if D > 0:
        print("The equation has two distinct real roots.")

        History.add_history(
            f"{a}x² + {b}x + {c} = 0",
            "Two distinct real roots"
        )

    elif D == 0:
        print("The equation has one repeated real root.")

        History.add_history(
            f"{a}x² + {b}x + {c} = 0",
            "One repeated real root"
        )

    else:
        print("The equation has two complex roots.")

        History.add_history(
            f"{a}x² + {b}x + {c} = 0",
            "Two complex roots"
        )