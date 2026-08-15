from colorama import Fore, Style, init
init()

import os
import time
import Calculator
import QuadraticEquations  
import History
import Geometry
import ScientificCalculator

def sleep(seconds):
    time.sleep(seconds)

def clear_screen():
    os.system('clear')

# PyCalc Advanced Math Toolkit
PAMT1 = 'PyCalc'
PAMT2 = 'Advanced Math Toolkit'


while True:
    print('=' * 40)
    print(PAMT1.center(40))
    print(PAMT2.center(40))
    print('=' * 40, end='\n\n')

    print(f"{Fore.RED}1{Style.RESET_ALL}. Calculator")
    print(f"{Fore.RED}2{Style.RESET_ALL}. Quadratic Equations")
    print(f"{Fore.RED}3{Style.RESET_ALL}. Geometry")
    print(f"{Fore.RED}4{Style.RESET_ALL}. Scientific Calculator")
    print(f"{Fore.RED}5{Style.RESET_ALL}. History")
    print(f"{Fore.RED}6{Style.RESET_ALL}. Exit", end='\n\n')  

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
                calc_choice = int(input('Choose : '))  
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
                qe_choice = int(input('Choose : '))  

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

            elif qe_choice == 4:  
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Discriminant & Root Analysis-{Style.RESET_ALL}", end='\n\n')
                QuadraticEquations.discriminant_analysis() 
                input('\nPress Enter to continue...')

            elif qe_choice == 5:
                clear_screen()
                sleep(1)
                break
    elif choice == 3:
        while True:
            clear_screen()
            sleep(1)
            geo = ' Geometry '
            print(geo.center(40, '=').upper(), end='\n\n')

            print(f"{Fore.RED}1{Style.RESET_ALL}. Circle")
            print(f"{Fore.RED}2{Style.RESET_ALL}. Rectangle")
            print(f"{Fore.RED}3{Style.RESET_ALL}. Square")
            print(f"{Fore.RED}4{Style.RESET_ALL}. Triangle")
            print(f"{Fore.RED}5{Style.RESET_ALL}. Cube")
            print(f"{Fore.RED}6{Style.RESET_ALL}. Sphere")
            print(f"{Fore.RED}7{Style.RESET_ALL}. Cylinder")
            print(f"{Fore.RED}8{Style.RESET_ALL}. Back", end='\n\n')

            try:
                ge_choice = int(input('Choose : '))  

            except ValueError:
                print('\nError: Please enter a number.')
                sleep(1)
                continue

            if ge_choice == 1:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Circle-{Style.RESET_ALL}", end='\n\n')
                Geometry.circle() 
                input('\nPress Enter to continue...')

            elif ge_choice == 2:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Rectangle-{Style.RESET_ALL}", end='\n\n')
                Geometry.rectangle() 
                input('\nPress Enter to continue...')

            elif ge_choice == 3:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Square-{Style.RESET_ALL}", end='\n\n')
                Geometry.square() 
                input('\nPress Enter to continue...')

            elif ge_choice == 4:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Triangle-{Style.RESET_ALL}", end='\n\n')
                Geometry.triangle() 
                input('\nPress Enter to continue...')

            elif ge_choice == 5:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Cube-{Style.RESET_ALL}", end='\n\n')
                Geometry.cube() 
                input('\nPress Enter to continue...')

            elif ge_choice == 6:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Sphere-{Style.RESET_ALL}", end='\n\n')
                Geometry.sphere() 
                input('\nPress Enter to continue...')

            elif ge_choice == 7:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Cylinder-{Style.RESET_ALL}", end='\n\n')
                Geometry.cylinder() 
                input('\nPress Enter to continue...')

            elif ge_choice == 8:
                clear_screen()
                sleep(1)
                break
                
    elif choice == 4:
    	while True:
            clear_screen()
            sleep(1)

            scientific_calculator = ' Scientific Calculator '
            print(scientific_calculator.center(40, '=').upper(), end='\n\n')
            
            print(f"{Fore.RED}1{Style.RESET_ALL}. Square Root")
            print(f"{Fore.RED}2{Style.RESET_ALL}. Cube Root")
            print(f"{Fore.RED}3{Style.RESET_ALL}. Logarithm")
            print(f"{Fore.RED}4{Style.RESET_ALL}. Factorial")
            print(f"{Fore.RED}5{Style.RESET_ALL}. Sin")
            print(f"{Fore.RED}6{Style.RESET_ALL}. Cos")
            print(f"{Fore.RED}7{Style.RESET_ALL}. Tang")
            print(f"{Fore.RED}8{Style.RESET_ALL}. asin")
            print(f"{Fore.RED}9{Style.RESET_ALL}. acos")
            print(f"{Fore.RED}10{Style.RESET_ALL}. atang")
            print(f"{Fore.RED}11{Style.RESET_ALL}. Back", end='\n\n')
            
            try:
                Sc_choice = int(input('Choose : '))  

            except ValueError:
                print('\nError: Please enter a number.')
                sleep(1)
                continue

            if Sc_choice == 1:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Square Root-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.square_root()
                input('\nPress Enter to continue...')

            elif Sc_choice == 2:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Cube Root-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.cube_root()
                input('\nPress Enter to continue...')

            elif Sc_choice == 3:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Logarithm-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.logarithm_func()                
                input('\nPress Enter to continue...')

            elif Sc_choice == 4:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Factorial-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.factorial_func()                 
                input('\nPress Enter to continue...')

            elif Sc_choice == 5:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Sin-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.sin_func()                 
                input('\nPress Enter to continue...')

            elif Sc_choice == 6:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Cos-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.cos_func()                
                input('\nPress Enter to continue...')

            elif Sc_choice == 7:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Tang-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.tan_func()                 
                input('\nPress Enter to continue...')
                
                
            elif Sc_choice == 8:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-asin-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.asin_func()                 
                input('\nPress Enter to continue...')

            elif Sc_choice == 9:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-acos-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.acos_func()               
                input('\nPress Enter to continue...')

            elif Sc_choice == 10:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-atang-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.atan_func()              
                input('\nPress Enter to continue...')

            elif Sc_choice == 11:
                clear_screen()
                sleep(1)
                break

    elif choice == 5:
        while True:
            clear_screen()
            sleep(1)

            history = ' History '
            print(history.center(40, '=').upper(), end='\n\n')

            print(f"{Fore.RED}1{Style.RESET_ALL}. Show History ")
            print(f"{Fore.RED}2{Style.RESET_ALL}. Clear History")
            print(f"{Fore.RED}3{Style.RESET_ALL}. Back", end='\n\n')

            try:
                hi_choice = int(input('Choose : '))  

            except ValueError:
                print('\nError: Please enter a number.')
                sleep(1)
                continue

            if hi_choice == 1:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Show History-{Style.RESET_ALL}", end='\n\n')
                History.view_history()
                input('\nPress Enter to continue...')

            elif hi_choice == 2:
                clear_screen()
                sleep(1)
                print(f"{Fore.CYAN}-Clear History-{Style.RESET_ALL}", end='\n\n')

                history = History.load_history()
                History.clear_history(history)

                print("History cleared successfully.")

                input('\nPress Enter to continue...')

            elif hi_choice == 3:
                clear_screen()
                sleep(1)
                break

    elif choice == 6:
        clear_screen()
        print('Exit ...')
        sleep(1)
        break

    else:
        print('\nError: Please choose 1, 2, 3, 4, 5, or 6.')
        sleep(1)
        clear_screen()