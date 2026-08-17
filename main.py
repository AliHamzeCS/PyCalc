from colorama import Fore, Style, init
init()

import os
import time
import Calculator
import QuadraticEquations  
import History
import Geometry
import ScientificCalculator
import UnitConverter
import Statistics
import Settings

def sleep():
    settings = Settings.load_settings()
    time.sleep(settings['calculation_delay'])

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
    print(f"{Fore.RED}5{Style.RESET_ALL}. Unit Converter")
    print(f"{Fore.RED}6{Style.RESET_ALL}. Statistics")
    print(f"{Fore.RED}7{Style.RESET_ALL}. Settings")
    print(f"{Fore.RED}8{Style.RESET_ALL}. History")
    print(f"{Fore.RED}9{Style.RESET_ALL}. Exit", end='\n\n')  

    try:
        choice = int(input('Choose : '))

    except ValueError:
        print('\nError: Please enter a number.')
        sleep()
        clear_screen()
        continue

    if choice == 1:
        while True:
            clear_screen()
            sleep()
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
                sleep()
                continue

            if calc_choice == 1:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Addition-{Style.RESET_ALL}", end='\n\n')
                Calculator.addition()
                input('\nPress Enter to continue...')
            elif calc_choice == 2:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Subtraction-{Style.RESET_ALL}", end='\n\n')
                Calculator.subtraction()
                input('\nPress Enter to continue...')
            elif calc_choice == 3:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Multiplication-{Style.RESET_ALL}", end='\n\n')
                Calculator.multiplication()
                input('\nPress Enter to continue...')
            elif calc_choice == 4:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Division-{Style.RESET_ALL}", end='\n\n')
                Calculator.division()
                input('\nPress Enter to continue...')
            elif calc_choice == 5:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Power-{Style.RESET_ALL}", end='\n\n')
                Calculator.power()
                input('\nPress Enter to continue...')
            elif calc_choice == 6:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Modulus-{Style.RESET_ALL}", end='\n\n')
                Calculator.modulus()
                input('\nPress Enter to continue...')
            elif calc_choice == 7:
                clear_screen()
                sleep()
                break

    elif choice == 2:
        while True:
            clear_screen()
            sleep()

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
                sleep()
                continue

            if qe_choice == 1:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-One Quadratic Equation-{Style.RESET_ALL}", end='\n\n')
                QuadraticEquations.solve_quadratic_equation()
                input('\nPress Enter to continue...')

            elif qe_choice == 2:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-System Of Two Equations-{Style.RESET_ALL}", end='\n\n')
                QuadraticEquations.solve_system_two_equations()
                input('\nPress Enter to continue...')

            elif qe_choice == 3:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-System Of Three Equations-{Style.RESET_ALL}", end='\n\n')
                QuadraticEquations.solve_system_three_equations()
                input('\nPress Enter to continue...')

            elif qe_choice == 4:  
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Discriminant & Root Analysis-{Style.RESET_ALL}", end='\n\n')
                QuadraticEquations.discriminant_analysis() 
                input('\nPress Enter to continue...')

            elif qe_choice == 5:
                clear_screen()
                sleep()
                break
    elif choice == 3:
        while True:
            clear_screen()
            sleep()
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
                sleep()
                continue

            if ge_choice == 1:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Circle-{Style.RESET_ALL}", end='\n\n')
                Geometry.circle() 
                input('\nPress Enter to continue...')

            elif ge_choice == 2:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Rectangle-{Style.RESET_ALL}", end='\n\n')
                Geometry.rectangle() 
                input('\nPress Enter to continue...')

            elif ge_choice == 3:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Square-{Style.RESET_ALL}", end='\n\n')
                Geometry.square() 
                input('\nPress Enter to continue...')

            elif ge_choice == 4:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Triangle-{Style.RESET_ALL}", end='\n\n')
                Geometry.triangle() 
                input('\nPress Enter to continue...')

            elif ge_choice == 5:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Cube-{Style.RESET_ALL}", end='\n\n')
                Geometry.cube() 
                input('\nPress Enter to continue...')

            elif ge_choice == 6:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Sphere-{Style.RESET_ALL}", end='\n\n')
                Geometry.sphere() 
                input('\nPress Enter to continue...')

            elif ge_choice == 7:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Cylinder-{Style.RESET_ALL}", end='\n\n')
                Geometry.cylinder() 
                input('\nPress Enter to continue...')

            elif ge_choice == 8:
                clear_screen()
                sleep()
                break
                
    elif choice == 4:
    	while True:
            clear_screen()
            sleep()

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
                sleep()
                continue

            if Sc_choice == 1:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Square Root-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.square_root()
                input('\nPress Enter to continue...')

            elif Sc_choice == 2:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Cube Root-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.cube_root()
                input('\nPress Enter to continue...')

            elif Sc_choice == 3:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Logarithm-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.logarithm_func()                
                input('\nPress Enter to continue...')

            elif Sc_choice == 4:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Factorial-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.factorial_func()                 
                input('\nPress Enter to continue...')

            elif Sc_choice == 5:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Sin-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.sin_func()                 
                input('\nPress Enter to continue...')

            elif Sc_choice == 6:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Cos-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.cos_func()                
                input('\nPress Enter to continue...')

            elif Sc_choice == 7:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Tang-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.tan_func()                 
                input('\nPress Enter to continue...')
                
                
            elif Sc_choice == 8:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-asin-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.asin_func()                 
                input('\nPress Enter to continue...')

            elif Sc_choice == 9:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-acos-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.acos_func()               
                input('\nPress Enter to continue...')

            elif Sc_choice == 10:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-atang-{Style.RESET_ALL}", end='\n\n')
                ScientificCalculator.atan_func()              
                input('\nPress Enter to continue...')

            elif Sc_choice == 11:
                clear_screen()
                sleep()
                break
            
    elif choice == 5:
        while True:
            clear_screen()
            sleep()
        
            Unit_Converter = ' Unit Converter '
            print(Unit_Converter.center(40, '=').upper(), end='\n\n')
            
            print(f"{Fore.RED}1{Style.RESET_ALL}. Length")
            print(f"{Fore.RED}2{Style.RESET_ALL}. Weigth")
            print(f"{Fore.RED}3{Style.RESET_ALL}. Temperature")
            print(f"{Fore.RED}4{Style.RESET_ALL}. Time")
            print(f"{Fore.RED}5{Style.RESET_ALL}. Back" , end='\n\n')
            
            try:
                uc_choice = int(input('Choose : '))  
            
            except ValueError:
                print('\nError: Please enter a number.')
                sleep()
                continue
            
            if uc_choice == 1:
                while True:
                    clear_screen()
                    sleep()
                        
                    length = ' Length '
                    print(length.center(40, '=').upper(), end='\n\n')
                            
                    print(f"{Fore.RED}1{Style.RESET_ALL}. Meter")
                    print(f"{Fore.RED}2{Style.RESET_ALL}. Kilometer")
                    print(f"{Fore.RED}3{Style.RESET_ALL}. Centimeter")
                    print(f"{Fore.RED}4{Style.RESET_ALL}. Millimeter")
                    print(f"{Fore.RED}5{Style.RESET_ALL}. Mile")
                    print(f"{Fore.RED}6{Style.RESET_ALL}. Yard")
                    print(f"{Fore.RED}7{Style.RESET_ALL}. Foot")
                    print(f"{Fore.RED}8{Style.RESET_ALL}. Inch")
                    print(f"{Fore.RED}9{Style.RESET_ALL}. Back" , end='\n\n')

                    
                    try:
                        len_choice = int(input('Choose : '))  
                                
                    except ValueError:
                        print('\nError: Please enter a number.')
                        sleep()
                        continue
                    
                    
                    if len_choice == 1:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Meter-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.meters_func()            
                        input('\nPress Enter to continue...')
                        
                    elif len_choice == 2:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Kilometer-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.kilometers_func()            
                        input('\nPress Enter to continue...')
                    elif len_choice == 3:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Centimeter-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.centimeters_func()            
                        input('\nPress Enter to continue...')
                    elif len_choice == 4:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Millimeter-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.millimeters_func()            
                        input('\nPress Enter to continue...')
                    elif len_choice == 5:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Mile-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.miles_func()            
                        input('\nPress Enter to continue...')
                    elif len_choice == 6:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Yard-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.yards_func()            
                        input('\nPress Enter to continue...')
                    elif len_choice == 7:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Foot-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.feet_func()            
                        input('\nPress Enter to continue...')
                    elif len_choice == 8:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Inch-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.inches_func()            
                        input('\nPress Enter to continue...')
                    elif len_choice == 9:
                        clear_screen()
                        sleep()
                        break
            elif uc_choice == 2:
                while True:
                    clear_screen()
                    sleep()
                                        
                    weight = ' Weight '
                    print(weight.center(40, '=').upper(), end='\n\n')
                                            
                    print(f"{Fore.RED}1{Style.RESET_ALL}. Kilogram")
                    print(f"{Fore.RED}2{Style.RESET_ALL}. Gram")
                    print(f"{Fore.RED}3{Style.RESET_ALL}. Milligram")
                    print(f"{Fore.RED}4{Style.RESET_ALL}. Pound")
                    print(f"{Fore.RED}5{Style.RESET_ALL}. Ounce")
                    print(f"{Fore.RED}6{Style.RESET_ALL}. Back" , end='\n\n')
                
                                    
                    try:
                        we_choice = int(input('Choose : '))  
                                                
                    except ValueError:
                        print('\nError: Please enter a number.')
                        sleep()
                        continue
                                    
                                    
                    if we_choice == 1:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Kilogram-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.kilogram_func()            
                        input('\nPress Enter to continue...')
                                        
                    elif we_choice == 2:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Gram-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.gram_func()
                        input('\nPress Enter to continue...')
                    elif we_choice == 3:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Milligram-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.milligram_func()            
                        input('\nPress Enter to continue...')
                    elif we_choice == 4:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Pound-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.pound_func()           
                        input('\nPress Enter to continue...')
                    elif we_choice == 5:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Ounce-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.ounce_func()            
                        input('\nPress Enter to continue...')
                    elif we_choice == 6:
                        clear_screen()
                        sleep()
                        break
            elif uc_choice == 3:
                while True:
                    clear_screen()
                    sleep()
                                                        
                    temperature = ' Temperature '
                    print(temperature.center(40, '=').upper(), end='\n\n')
                                                            
                    print(f"{Fore.RED}1{Style.RESET_ALL}. Celsius")
                    print(f"{Fore.RED}2{Style.RESET_ALL}. Fahrenheit")
                    print(f"{Fore.RED}3{Style.RESET_ALL}. Kelvin")
                    print(f"{Fore.RED}4{Style.RESET_ALL}. Back" , end='\n\n')
                                
                                                    
                    try:
                        tem_choice = int(input('Choose : '))  
                                                                
                    except ValueError:
                        print('\nError: Please enter a number.')
                        sleep()
                        continue
                                                    
                                                    
                    if tem_choice == 1:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Celsius-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.celsius_func()            
                        input('\nPress Enter to continue...')
                                                        
                    elif tem_choice == 2:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Fahrenheit-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.fahrenheit_func()
                        input('\nPress Enter to continue...')
                    elif tem_choice == 3:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Kelvin-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.kelvin_func()            
                        input('\nPress Enter to continue...')
                    elif tem_choice == 4:
                        clear_screen()
                        sleep()
                        break
            elif uc_choice == 4:
                while True:
                    clear_screen()
                    sleep()
                                                                        
                    timee = ' Time '
                    print(timee.center(40, '=').upper(), end='\n\n')
                                                                            
                    print(f"{Fore.RED}1{Style.RESET_ALL}. Second")
                    print(f"{Fore.RED}2{Style.RESET_ALL}. Minute")
                    print(f"{Fore.RED}3{Style.RESET_ALL}. Hour")
                    print(f"{Fore.RED}4{Style.RESET_ALL}. Day")
                    print(f"{Fore.RED}5{Style.RESET_ALL}. Back" , end='\n\n')
                                                
                                                                    
                    try:
                        time_choice = int(input('Choose : '))  
                                                                                
                    except ValueError:
                            print('\nError: Please enter a number.')
                            sleep()
                            continue
                                                                    
                                                                    
                    if time_choice == 1:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Second-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.seconds_func()            
                        input('\nPress Enter to continue...')
                                                                        
                    elif time_choice == 2:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Minute-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.minutes_func()
                        input('\nPress Enter to continue...')
                    elif time_choice == 3:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Hour-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.hours_func()            
                        input('\nPress Enter to continue...')
                                        
                    elif time_choice == 4:
                        clear_screen()
                        sleep()
                        print(f"{Fore.CYAN}-Day-{Style.RESET_ALL}", end='\n\n')
                        UnitConverter.days_func()            
                        input('\nPress Enter to continue...')
                    elif time_choice == 5:
                        clear_screen()
                        sleep()
                        break
            elif uc_choice == 5:
                clear_screen()
                sleep()
                break
            
    elif choice == 6:
        while True:
            clear_screen()
            sleep()
                
            statistics = ' Statistics '
            print(statistics.center(40, '=').upper(), end='\n\n')
                    
            print(f"{Fore.RED}1{Style.RESET_ALL}. Mean")
            print(f"{Fore.RED}2{Style.RESET_ALL}. Median")
            print(f"{Fore.RED}3{Style.RESET_ALL}. Mode")
            print(f"{Fore.RED}4{Style.RESET_ALL}. Range")
            print(f"{Fore.RED}5{Style.RESET_ALL}. Variance")
            print(f"{Fore.RED}6{Style.RESET_ALL}. Standard Deviation")
            print(f"{Fore.RED}7{Style.RESET_ALL}. Back" , end='\n\n')
                    
            try:
                stat_choice = int(input('Choose : '))  
                    
            except ValueError:
                print('\nError: Please enter a number.')
                sleep()
                continue
            
            if stat_choice == 1:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Mean-{Style.RESET_ALL}", end='\n\n')
                Statistics.mean_func()           
                input('\nPress Enter to continue...')
            elif stat_choice == 2:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Median-{Style.RESET_ALL}", end='\n\n')
                Statistics.median_func()           
                input('\nPress Enter to continue...')
            elif stat_choice == 3:   
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Mode-{Style.RESET_ALL}", end='\n\n')
                Statistics.mode_func()            
                input('\nPress Enter to continue...')
            elif stat_choice == 4: 
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Range-{Style.RESET_ALL}", end='\n\n')
                Statistics.range_func()            
                input('\nPress Enter to continue...')
            elif stat_choice == 5: 
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Variance-{Style.RESET_ALL}", end='\n\n')
                Statistics.variance()            
                input('\nPress Enter to continue...')
            elif stat_choice == 6: 
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Standard Deviation-{Style.RESET_ALL}", end='\n\n')
                Statistics.standard_deviation()            
                input('\nPress Enter to continue...')
            elif stat_choice == 7: 
                clear_screen()
                sleep()
                break 
            
    elif choice == 7:
        while True:
            clear_screen()
            sleep()
                        
            settings = ' Settings '
            print(settings.center(40, '=').upper(), end='\n\n')
                            
            print(f"{Fore.RED}1{Style.RESET_ALL}. Calculation Precision")
            print(f"{Fore.RED}2{Style.RESET_ALL}. Startup Delay")
            print(f"{Fore.RED}3{Style.RESET_ALL}. Reset Settings")
            print(f"{Fore.RED}4{Style.RESET_ALL}. Back" , end='\n\n')
                            
            try:
                set_choice = int(input('Choose : '))  
                            
            except ValueError:
                print('\nError: Please enter a number.')
                sleep()
                continue
            
            if set_choice == 1:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Calculation Precision-{Style.RESET_ALL}", end='\n\n')
                Settings.decimal_precision_func()           
                input('\nPress Enter to continue...')
            elif set_choice == 2:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Startup Delay-{Style.RESET_ALL}", end='\n\n')
                Settings.calculation_delay_func()           
                input('\nPress Enter to continue...')
            elif set_choice == 3:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Reset Settings-{Style.RESET_ALL}", end='\n\n')
                Settings.reset_settings()           
                input('\nPress Enter to continue...')
            elif set_choice == 4:
                clear_screen()
                sleep()
                break 
             
    elif choice == 8:
        while True:
            clear_screen()
            sleep()

            history = ' History '
            print(history.center(40, '=').upper(), end='\n\n')

            print(f"{Fore.RED}1{Style.RESET_ALL}. Show History ")
            print(f"{Fore.RED}2{Style.RESET_ALL}. Clear History")
            print(f"{Fore.RED}3{Style.RESET_ALL}. Back", end='\n\n')

            try:
                hi_choice = int(input('Choose : '))  

            except ValueError:
                print('\nError: Please enter a number.')
                sleep()
                continue

            if hi_choice == 1:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Show History-{Style.RESET_ALL}", end='\n\n')
                History.view_history()
                input('\nPress Enter to continue...')

            elif hi_choice == 2:
                clear_screen()
                sleep()
                print(f"{Fore.CYAN}-Clear History-{Style.RESET_ALL}", end='\n\n')

                history = History.load_history()
                History.clear_history(history)

                print("History cleared successfully.")

                input('\nPress Enter to continue...')

            elif hi_choice == 3:
                clear_screen()
                sleep()
                break

    elif choice == 9:
        clear_screen()
        print('Exit ...')
        sleep()
        break

    else:
        print('\nError: Please choose 1, 2, 3, 4, 5, 6, 7, 8, or 9.')
        sleep()
        clear_screen()