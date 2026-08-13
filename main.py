from colorama import Fore, Style, init
init()

import os
import time
import Calculator
import QuadraticEquations  # <== ملاحظة 1: لازم تستوردو

def sleep(seconds):
    time.sleep(seconds)

def clear_screen():
    os.system('clear')

# PyCalc Advanced Math Toolkit
PAMT1 = 'PyCalc'
PAMT2 = 'Advanced Math Toolkit'

print('=' * 40)
print(PAMT1.center(40))
print(PAMT2.center(40))
print('=' * 40, end='\n\n')

while True:

    print(f"{Fore.RED}1{Style.RESET_ALL}. Calculator")
    print(f"{Fore.RED}2{Style.RESET_ALL}. Quadratic Equations")
    print(f"{Fore.RED}3{Style.RESET_ALL}. History")
    print(f"{Fore.RED}4{Style.RESET_ALL}. Exit", end='\n\n')  # <== ملاحظة 2: كان 3 مكرر

    try:
        choice = int(input('Choose : '))

    except ValueError:
        print('\nError: Please enter a number.')
        sleep(1)
        clear_screen()
        continue

    if choice == 1:
        while True:
            clear_screen()
            sleep(1)
            calc = ' calculator '
            print(calc.center(40, '=').upper(), end='\n\n')

            print(f"{Fore.RED}1{Style.RESET_ALL}. Addition")
            print(f"{Fore.RED}2{Style.RESET_ALL}. Subtraction")
            print(f"{Fore.RED}3{Style.RESET_ALL}. Multiplication")
            print(f"{Fore.RED}4{Style.RESET_ALL}. Division")
            print(f"{Fore.RED}5{Style.RESET_ALL}. Power")
            print(f"{Fore.RED}6{Style.RESET_ALL}. Modulus")
            print(f"{Fore.RED}7{Style.RESET_ALL}. Back", end='\n\n')

            try:
                calc_choice = int(input('Choose : '))  # <== ملاحظة 3: غيرت الاسم
            except ValueError:
                print('\nError: Please enter a number.')
                sleep(1)
                continue

            if calc_choice == 1:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Addition-{Style.RESET_ALL}", end='\n\n')
                Calculator.addition()
                input('\nPress Enter to continue...')
            elif calc_choice == 2:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Subtraction-{Style.RESET_ALL}", end='\n\n')
                Calculator.subtraction()
                input('\nPress Enter to continue...')
            elif calc_choice == 3:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Multiplication-{Style.RESET_ALL}", end='\n\n')
                Calculator.multiplication()
                input('\nPress Enter to continue...')
            elif calc_choice == 4:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Division-{Style.RESET_ALL}", end='\n\n')
                Calculator.division()
                input('\nPress Enter to continue...')
            elif calc_choice == 5:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Power-{Style.RESET_ALL}", end='\n\n')
                Calculator.power()
                input('\nPress Enter to continue...')
            elif calc_choice == 6:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Modulus-{Style.RESET_ALL}", end='\n\n')
                Calculator.modulus()
                input('\nPress Enter to continue...')
            elif calc_choice == 7:
                clear_screen()
                sleep(1)
                break
    
    elif choice == 2:
        while True:
            clear_screen()
            sleep(1)
            
            QE = ' Quadratic Equations'
            print(QE.center(40, '=').upper(), end='\n\n')
            
            print(f"{Fore.RED}1{Style.RESET_ALL}. One Quadratic Equation")
            print(f"{Fore.RED}2{Style.RESET_ALL}. System Of Two Equations")
            print(f"{Fore.RED}3{Style.RESET_ALL}. System Of Three Equations")
            print(f"{Fore.RED}4{Style.RESET_ALL}. Discriminant & Root Analysis")
            print(f"{Fore.RED}5{Style.RESET_ALL}. Back" , end='\n\n')
            
            try:
                qe_choice = int(input('Choose : '))  # <== ملاحظة 3: غيرت الاسم

            except ValueError:
                print('\nError: Please enter a number.')
                sleep(1)
                continue
                
            if qe_choice == 1:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-One Quadratic Equation-{Style.RESET_ALL}", end='\n\n')
                QuadraticEquations.solve_quadratic_equation()
                input('\nPress Enter to continue...')
                
            elif qe_choice == 2:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-System Of Two Equations-{Style.RESET_ALL}", end='\n\n')
                QuadraticEquations.solve_system_two_equations()
                input('\nPress Enter to continue...')
            
            elif qe_choice == 3:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-System Of Three Equations-{Style.RESET_ALL}", end='\n\n')
                QuadraticEquations.solve_system_three_equations()
                input('\nPress Enter to continue...')
                
            elif qe_choice == 4:  # <== كان if واسم غلط
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Discriminant & Root Analysis-{Style.RESET_ALL}", end='\n\n')
                QuadraticEquations.discriminant_analysis() # لازم تضيف هالفنكشن
                input('\nPress Enter to continue...')
            
            elif qe_choice == 5:
                clear_screen()
                sleep(1)
                break

    elif choice == 3:
        clear_screen()
        sleep(1)
        print("History coming soon...") # <== فاضي
        input('\nPress Enter to continue...')

    elif choice == 4:
        clear_screen()
        print('Exit ...')
        sleep(1)
        break

    else:
        print('\nError: Please choose 1, 2, 3, or 4.') # <== صلحت الرسالة
        sleep(1)
        clear_screen()