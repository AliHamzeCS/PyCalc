from colorama import Fore, Style, init
init()
import History
import math

def circle():
    try :
        r = float(input('redius : '))
        
        result_area = math.pi * r * r
        result_circumference = 2 * math.pi * r
        result_diameter = 2 * r
        
        print(f"{Fore.MAGENTA}Area = {Style.RESET_ALL}. {result_area}")
        print(f"{Fore.MAGENTA}Circumference = {Style.RESET_ALL}. {result_circumference}")
        print(f"{Fore.MAGENTA}Diameter = {Style.RESET_ALL}. {result_diameter}")
        
        History.add_history(f'Area = ' , result_area)
        History.add_history(f'Circumference = ' , result_circumference)
        History.add_history(f'Diameter = ' , result_diameter)
        
    except ValueError:
            print('\nError: Please enter numbers only.')

def rectangle():
    try :
        l = float(input('length : '))
        w = float(input('width : '))
        
        result_area = l * w
        result_perimeter = 2 * (l + w)
        result_diagonal = math.sqrt(l**2 + w**2)
        
        print(f"{Fore.MAGENTA}Area = {Style.RESET_ALL}. {result_area}")
        print(f"{Fore.MAGENTA}Perimeter = {Style.RESET_ALL}. {result_perimeter}")
        print(f"{Fore.MAGENTA}Diagonal = {Style.RESET_ALL}. {result_diagonal}")
        
        History.add_history(f'Area = ' , result_area)
        History.add_history(f'Perimeter = ' , result_perimeter)
        History.add_history(f'Diagonal = ' , result_diagonal)
        
    except ValueError:
                print('\nError: Please enter numbers only.')
                
def square():
    try :
        s = float(input('side : '))
        
        
        result_area = s * s
        result_perimeter = 4 * s
        result_diagonal = (math.sqrt(2)) * s
        
        print(f"{Fore.MAGENTA}Area = {Style.RESET_ALL}. {result_area}")
        print(f"{Fore.MAGENTA}Perimeter = {Style.RESET_ALL}. {result_perimeter}")
        print(f"{Fore.MAGENTA}Diagonal = {Style.RESET_ALL}. {result_diagonal}")
        
        History.add_history(f'Area = ' , result_area)
        History.add_history(f'Perimeter = ' , result_perimeter)
        History.add_history(f'Diagonal = ' , result_diagonal)
        
    except ValueError:
                print('\nError: Please enter numbers only.')
                
def triangle():
    try :
        b = float(input('base : '))
        h = float(input('height : '))
        
        side_1 = float(input('side 1 : '))
        side_2 = float(input('side 2 : '))
        side_3 = float(input('side 3 : '))
        
        result_area = (b * h) / 2
        result_perimeter = side_1 + side_2 + side_3
                
        print(f"{Fore.MAGENTA}Area = {Style.RESET_ALL}. {result_area}")
        print(f"{Fore.MAGENTA}Perimeter = {Style.RESET_ALL}. {result_perimeter}")
                
        History.add_history(f'Area = ' , result_area)
        History.add_history(f'Perimeter = ' , result_perimeter)
        
    except ValueError:
                    print('\nError: Please enter numbers only.')
                    
def cube():
    try :
        s = float(input('side : '))
        
        result_volume = s * s * s
        result_total_surface_area = 6 * s * s
        result_diagonal = (math.sqrt(3)) * s
                
        print(f"{Fore.MAGENTA}Volume = {Style.RESET_ALL}. {result_volume}")
        print(f"{Fore.MAGENTA}Total Surface Area = {Style.RESET_ALL}. {result_total_surface_area}")
        print(f"{Fore.MAGENTA}Diagonal = {Style.RESET_ALL}. {result_diagonal}")
                
        History.add_history(f'Volume = ' , result_volume)
        History.add_history('Total Surface Area = ', result_total_surface_area)
        History.add_history(f'Diagonal = ' , result_diagonal)
        
    except ValueError:
                    print('\nError: Please enter numbers only.')
                    
def sphere():
    try :
        r = float(input('radius : '))
        
        result_volume = (4/3) * math.pi * r**3
        result_surface_area = 4 * math.pi * r**2
        result_diameter = 2 * r
                
        print(f"{Fore.MAGENTA}Volume = {Style.RESET_ALL}. {result_volume}")
        print(f"{Fore.MAGENTA}Surface Area = {Style.RESET_ALL}. {result_surface_area}")
        print(f"{Fore.MAGENTA}Diameter = {Style.RESET_ALL}. {result_diameter}")
                
        History.add_history(f'Volume = ' , result_volume)
        History.add_history('Surface Area = ', result_surface_area)
        History.add_history(f'Diameter = ' , result_diameter)
        
    except ValueError:
                    print('\nError: Please enter numbers only.')
                    
def cylinder():
    try :
        r = float(input('radius : '))
        h = float(input('height : '))
        
        result_volume = math.pi * r**2 *h
        result_total_surface_area =(math.pi * r * h) + (2 * math.pi * r**2)
        result_Lateral_Surface_Area = 2 * math.pi * r * h
                
        print(f"{Fore.MAGENTA}Volume = {Style.RESET_ALL}. {result_volume}")
        print(f"{Fore.MAGENTA}Total Surface Area = {Style.RESET_ALL}. {result_total_surface_area}")
        print(f"{Fore.MAGENTA}Lateral Surface Area = {Style.RESET_ALL}. {result_Lateral_Surface_Area}")
                
        History.add_history(f'Volume = ' , result_volume)
        History.add_history('Total Surface Area = ', result_total_surface_area)
        History.add_history('Lateral Surface Area = ', result_Lateral_Surface_Area)
        
    except ValueError:
                    print('\nError: Please enter numbers only.')