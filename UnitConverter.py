from pint import UnitRegistry
ureg = UnitRegistry()
import History


# ========== LENGTH ==========

def meters_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: meter')
            to = input('To unit: ').lower()

            val = num * ureg.meter
            result = val.to(ureg(to))

            print(f'{num} meter = {result}')

            History.add_history(
                f'{num} meter',
                str(result)
            )

    except:
        print('Error. Try again')


def kilometers_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: kilometer')
            to = input('To unit: ').lower()

            val = num * ureg.kilometer
            result = val.to(ureg(to))

            print(f'{num} kilometer = {result}')

            History.add_history(
                f'{num} kilometer',
                str(result)
            )

    except:
        print('Error. Try again')


def centimeters_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: centimeter')
            to = input('To unit: ').lower()

            val = num * ureg.centimeter
            result = val.to(ureg(to))

            print(f'{num} centimeter = {result}')

            History.add_history(
                f'{num} centimeter',
                str(result)
            )

    except:
        print('Error. Try again')


def millimeters_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: millimeter')
            to = input('To unit: ').lower()

            val = num * ureg.millimeter
            result = val.to(ureg(to))

            print(f'{num} millimeter = {result}')

            History.add_history(
                f'{num} millimeter',
                str(result)
            )

    except:
        print('Error. Try again')


def miles_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: mile')
            to = input('To unit: ').lower()

            val = num * ureg.mile
            result = val.to(ureg(to))

            print(f'{num} mile = {result}')

            History.add_history(
                f'{num} mile',
                str(result)
            )

    except:
        print('Error. Try again')


def yards_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: yard')
            to = input('To unit: ').lower()

            val = num * ureg.yard
            result = val.to(ureg(to))

            print(f'{num} yard = {result}')

            History.add_history(
                f'{num} yard',
                str(result)
            )

    except:
        print('Error. Try again')


def feet_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: foot')
            to = input('To unit: ').lower()

            val = num * ureg.foot
            result = val.to(ureg(to))

            print(f'{num} foot = {result}')

            History.add_history(
                f'{num} foot',
                str(result)
            )

    except:
        print('Error. Try again')


def inches_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: inch')
            to = input('To unit: ').lower()

            val = num * ureg.inch
            result = val.to(ureg(to))

            print(f'{num} inch = {result}')

            History.add_history(
                f'{num} inch',
                str(result)
            )

    except:
        print('Error. Try again')


# ========== WEIGHT ==========

def kilogram_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: kilogram')
            to = input('To unit: ').lower()

            val = num * ureg.kilogram
            result = val.to(ureg(to))

            print(f'{num} kilogram = {result}')

            History.add_history(
                f'{num} kilogram',
                str(result)
            )

    except:
        print('Error. Try again')


def gram_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: gram')
            to = input('To unit: ').lower()

            val = num * ureg.gram
            result = val.to(ureg(to))

            print(f'{num} gram = {result}')

            History.add_history(
                f'{num} gram',
                str(result)
            )

    except:
        print('Error. Try again')


def milligram_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: milligram')
            to = input('To unit: ').lower()

            val = num * ureg.milligram
            result = val.to(ureg(to))

            print(f'{num} milligram = {result}')

            History.add_history(
                f'{num} milligram',
                str(result)
            )

    except:
        print('Error. Try again')


def pound_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: pound')
            to = input('To unit: ').lower()

            val = num * ureg.pound
            result = val.to(ureg(to))

            print(f'{num} pound = {result}')

            History.add_history(
                f'{num} pound',
                str(result)
            )

    except:
        print('Error. Try again')


def ounce_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: ounce')
            to = input('To unit: ').lower()

            val = num * ureg.ounce
            result = val.to(ureg(to))

            print(f'{num} ounce = {result}')

            History.add_history(
                f'{num} ounce',
                str(result)
            )

    except:
        print('Error. Try again')


# ========== TEMPERATURE ==========

def celsius_func():
    try:
        num = float(input('Enter value: '))

        print('From unit: celsius')
        to = input('To unit: ').lower()

        val = num * ureg.degC
        result = val.to(ureg(to))

        print(f'{num} celsius = {result}')

        History.add_history(
            f'{num} celsius',
            str(result)
        )

    except:
        print('Error. Try again')


def fahrenheit_func():
    try:
        num = float(input('Enter value: '))

        print('From unit: fahrenheit')
        to = input('To unit: ').lower()

        val = num * ureg.degF
        result = val.to(ureg(to))

        print(f'{num} fahrenheit = {result}')

        History.add_history(
            f'{num} fahrenheit',
            str(result)
        )

    except:
        print('Error. Try again')


def kelvin_func():
    try:
        num = float(input('Enter value: '))

        print('From unit: kelvin')
        to = input('To unit: ').lower()

        val = num * ureg.kelvin
        result = val.to(ureg(to))

        print(f'{num} kelvin = {result}')

        History.add_history(
            f'{num} kelvin',
            str(result)
        )

    except:
        print('Error. Try again')


# ========== TIME ==========

def seconds_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: second')
            to = input('To unit: ').lower()

            val = num * ureg.second
            result = val.to(ureg(to))

            print(f'{num} second = {result}')

            History.add_history(
                f'{num} second',
                str(result)
            )

    except:
        print('Error. Try again')


def minutes_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: minute')
            to = input('To unit: ').lower()

            val = num * ureg.minute
            result = val.to(ureg(to))

            print(f'{num} minute = {result}')

            History.add_history(
                f'{num} minute',
                str(result)
            )

    except:
        print('Error. Try again')


def hours_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: hour')
            to = input('To unit: ').lower()

            val = num * ureg.hour
            result = val.to(ureg(to))

            print(f'{num} hour = {result}')

            History.add_history(
                f'{num} hour',
                str(result)
            )

    except:
        print('Error. Try again')


def days_func():
    try:
        num = float(input('Enter value: '))
        if num >= 0:
            print('From unit: day')
            to = input('To unit: ').lower()

            val = num * ureg.day
            result = val.to(ureg(to))

            print(f'{num} day = {result}')

            History.add_history(
                f'{num} day',
                str(result)
            )

    except:
        print('Error. Try again')
        