def main():

    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while True:
        val1 = int(input('Enter Value 1: '))
        val2 = int(input('Enter Value 2: '))
        val3 = int(input('Enter Value 3: '))
        val4 = int(input('Enter Value 4: '))
        val5 = int(input('Enter Value 5: '))
        numbers = [val1, val2, val3, val4, val5]
        if val1 > val2 and val1 > val3 and val1 > val3 and val1 > val4 and val1 > val5:
            maxval = val1
        else:
            if val2 > val1 and val2 > val3 and val2 > val4 and val2 > val5:
                maxval = val2
            else:
                if val3 > val1 and val3 > val2 and val3 > val4 and val3 > val5:
                    maxval = val3
                else:
                    if val4 > val1 and val4 > val2 and val4 > val3 and val4 > val5:
                        maxval = val4
                    else:
                        maxval = val5
        if val1 < val2 and val1 < val3 and val1 < val4 and val1 < val5:
            minval = val1
        else: 
            if val2 < val1 and val2 < val3 and val2 < val4 and val2 < val5:
                minval = val2
            else: 
                if val3 < val1 and val3 < val2 and val3 < val4 and val3 < val5:
                    minval = val3
                else:
                    if val4 < val1 and val4 < val2 and val4 < val3 and val4 < val5:
                        minval = val4
                    else:
                        minval = val5
    

        print(*numbers)
        print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
        return numbers, maxval, minval


if __name__ == '__main__':
    main()
