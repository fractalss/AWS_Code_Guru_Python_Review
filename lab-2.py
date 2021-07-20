
import config


def main():
    ask_again = True
    while(ask_again):
        a = input("Enter the numerator: ")
        b = input("Enter the denominator: ")
        result = perform_division(a,b)
        print(result)
        ask_again = input("Do you want to perform another operation? Enter yes or no: ")
        if(ask_again == 'yes'):
            ask_again = True
        else:
            ask_again = False
            strings = ['You performed ', str(config.operations_count), ' operations, bye!']
            print(str.join())


def perform_division(a,b):
    config.operations_count
    config.operations_count += 1
    try:
        return int(a)/int(b)
    except ZeroDivisionError as e:
        logger.exception('ZeroDivisionError:')
        pass


main()