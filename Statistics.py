import History

def mean_func():
    while True:
        try:
            numbers = input('Write the numbers and put a space between each number : ')
            list_numbers = numbers.split(' ')

            if len(list_numbers) == 0 or list_numbers == ['']:
                print("Error: Please enter at least one number")
                continue

            sum_of_numbers = 0

            for num in list_numbers:
                if num != '':
                    sum_of_numbers += float(num)

            mean = sum_of_numbers / (len(list_numbers) - list_numbers.count(''))

            History.add_history(
                f'Mean ',
                mean
            )

            print(f'\nMean = {mean}')
            break

        except ValueError:
            print("Error: Please enter numbers only")

def median_func():
    while True:
        try:
            numbers = input('Write the numbers and put a space between each number : ')
            list_numbers = numbers.split(' ')

            number_list = []
            for num in list_numbers:
                if num!= '':
                    number_list.append(float(num))

            if len(number_list) == 0:
                print("Error: Please enter at least one number")
                continue

            number_list.sort()
            n = len(number_list)

            if n % 2 == 0:
                medium_index = n // 2
                sum_number = number_list[medium_index - 1] + number_list[medium_index]
                median_value = sum_number / 2
                print(f'Median = {median_value}')
                
                History.add_history(
                                                f'Median ',
                                                median_value
                                            )
                
            else :
                medium_index = n // 2
                median_value = number_list[medium_index]
                print(f'Median = {median_value}')
                
                History.add_history(
                                                                f'Median ',
                                                                median_value
                                                            )
                
            break

        except ValueError:
            print("Error: Please enter numbers only")

def mode_func():
    while True:
        try:
            numbers = input('Write the numbers and put a space between each number : ')
            list_numbers = numbers.split(' ')

            dic_numbers ={}
            for num in list_numbers :
                if num!= '':
                    count = 0
                    test_number = float(num)
                    for number in list_numbers :
                        if number!= '' and float(number) == test_number :
                            count += 1
                    dic_numbers[test_number] = count

            if len(dic_numbers) == 0:
                print("Error: Please enter at least one number")
                continue

            max_count = 0
            for element in dic_numbers:
                if dic_numbers[element] > max_count:
                    max_count = dic_numbers[element]

            modes = []
            for element in dic_numbers:
                if dic_numbers[element] == max_count:
                    modes.append(element)

            if max_count == 1:
                print("No Mode")
            else:
                print(f'Mode = {modes}')
                History.add_history(
                                                                f'Mode ',
                                                                modes
                                                            )
            break

        except ValueError:
            print("Error: Please enter numbers only")

def range_func():
    while True:
        try:
            numbers = input('Write the numbers and put a space between each number : ')
            list_numbers = numbers.split(' ')

            number_list = []
            for num in list_numbers:
                if num!= '':
                    number_list.append(float(num))

            if len(number_list) == 0:
                print("Error: Please enter at least one number")
                continue

            max_number = number_list[0]
            min_number = number_list[0]

            for num in number_list :
                if num > max_number :
                    max_number = num
                if num < min_number :
                    min_number = num

            range_val = max_number - min_number
            print(f'Range = {range_val}')
            
            History.add_history(
                                                                            f'Range ',
                                                                            range_val
                                                                        )
            
            break

        except ValueError:
            print("Error: Please enter numbers only")

def variance():
    while True:
        try:
            numbers = input('Write the numbers and put a space between each number : ')
            list_numbers = numbers.split(' ')

            number_list = []
            for num in list_numbers:
                if num!= '':
                    number_list.append(float(num))

            if len(number_list) == 0:
                print("Error: Please enter at least one number")
                continue

            #Calculate Mean
            sum_of_numbers = 0
            for num in number_list :
                sum_of_numbers += num
            mean = sum_of_numbers / len(number_list)

            #Calculate Variance
            squared_differences = []
            for num in number_list :
                difference = num - mean
                squared_differences.append(difference * difference)

            sum_total = 0
            for sq in squared_differences:
                sum_total += sq

            variance_value = sum_total / len(squared_differences)
            print(f'Variance = {variance_value}')
            
            History.add_history(
                                                                                        f'Variance ',
                                                                                        variance_value
                                                                                    )
            
            break

        except ValueError:
            print("Error: Please enter numbers only")

def standard_deviation():
    while True:
        try:
            numbers = input('Write the numbers and put a space between each number : ')
            list_numbers = numbers.split(' ')

            number_list = []
            for num in list_numbers:
                if num!= '':
                    number_list.append(float(num))

            if len(number_list) == 0:
                print("Error: Please enter at least one number")
                continue

            #Calculate Mean
            sum_of_numbers = 0
            for num in number_list :
                sum_of_numbers += num
            mean = sum_of_numbers / len(number_list)

            #Calculate Variance
            squared_differences = []
            for num in number_list :
                difference = num - mean
                squared_differences.append(difference * difference)

            sum_total = 0
            for sq in squared_differences:
                sum_total += sq

            variance_value = sum_total / len(squared_differences)

            #Calculate standard deviation
            standard_dev = variance_value ** 0.5
            print(f'Standard Deviation = {standard_dev}')
            
            History.add_history(
                                                                                                    f'Standard Deviation ',
                                                                                                    standard_dev
                                                                                                )
            
            break

        except ValueError:
            print("Error: Please enter numbers only")