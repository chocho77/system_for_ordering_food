from food_and_drinks_choices import FOOD_CHOICES, FOOD_CHOICES_PRICES, DRINKS_CHOICES, \
                                     DRINKS_CHOICES_PRICES, SEPARATOR_LIST, TEXT_RM_LIST
from user_input import take_user_input
from validation import is_main_menu_input_valid, map_user_input, valid_success
import sys
from database import read_data_from_db

d = {}


def space_numbers_between_texts(number: int) -> str:
    return " " * number


def print_columns(*args, spacings):
    # Ensure spacings is a list with enough values for the columns
    if len(spacings) != len(args):
        print("Error: Number of spacings does not match the number of columns.")
        return

    # Initialize the base format string
    format_string = "   "

    # Add each argument's format with spacing
    for i in range(len(args) - 1):
        format_string += "{:<" + str(spacings[i]) + "}"

    # Add the last column without extra spacing
    format_string += "{}"

    # Print the formatted text for each row
    for row in zip(*args):
        print(format_string.format(*row))



def print_header_user_interface():
    width_before_text = 35
    width_after_text = 35
    width_text = 28
    symbols_print_before_text = width_before_text * "*"
    symbols_print_after_text = width_after_text * "*"
    space_drink_name_price = " " * 4
    space_food_name_price = " " * 5
    main_message = "ORDER FOODS & DRINKS".center(width_text)
    number_symbol = '|No|'
    food_text_name = '|FOOD NAME|'
    drink_text_name = '|DRINK NAME|'
    price_text = '|PRICE|'
    separate_symbol = '|'
    
    print(f"{symbols_print_before_text} {main_message} {symbols_print_after_text}")
    print(f"  {number_symbol}  {food_text_name}   {space_numbers_between_texts(5)} {price_text} {space_numbers_between_texts(12)} {separate_symbol}", end="")
    print(f"  {space_numbers_between_texts(6)}{number_symbol} {space_numbers_between_texts(3)} {drink_text_name}   {space_numbers_between_texts(7)}   {price_text}  ")

def print_footer_interface():
    print() # print empty row
    print(f" (M) MAIN MENU {space_numbers_between_texts(6)} (S) SELECT ORDER ", end="")
    print(f" {space_numbers_between_texts(4)} (L) LIST OF ORDERS", end = "")
    print(f" {space_numbers_between_texts(5)}(P) PAYMENT {space_numbers_between_texts(5)}(E) EXIT")
    print(103 * "_")

def print_choice_msg():
    while True:
        user_choice = take_user_input()
        is_valid_input = is_main_menu_input_valid(user_choice)
        if is_valid_input:
            if user_choice == "M":
                print_main_ui()
            elif user_choice == "S":
                print("SELECT ORDER")
            elif user_choice == "L":
                #key = input("Enter order: ")
                print("LIST OF ORDERS")           
            elif user_choice == "P":
                print("PAYMENT")
                #d = read_data_from_db(key)
                #print(d)
            elif user_choice == "E":
                print("Exit Program Bye!")
                print("Have a Nice Day!")
                sys.exit(0)
            elif not (user_choice == "M" and user_choice == "P" and user_choice == "S" and user_choice == "L" and user_choice == "E"):
                user_correct_input = valid_success(user_choice)
                map_user_input(user_correct_input)
        else:
            print("The input is invalid.")

def print_user_interface():
    # column 1
    food_choices_numbers_list = [i for i in range(1,21)]
    # column 2
    food_choices_list = [i for i in FOOD_CHOICES]
    # column 3
    rm_text_list = [i for i in TEXT_RM_LIST]
    # column 4
    food_choices_price_list = [i for i in FOOD_CHOICES_PRICES]
    # column 5
    separator_list = [i for i in SEPARATOR_LIST]
    # column 6
    drinks_choices_list_numbers = [i for i in range(41,61)]
    # column 7
    drinks_choices_list = [i for i in DRINKS_CHOICES]
    # column 8    
    drinks_choices_price_list = [i for i in DRINKS_CHOICES_PRICES]

    spacings = [6, 20, 3, 17, 10, 10, 24, 3, 15]  # Varying spaces between columns
    print_columns(food_choices_numbers_list, food_choices_list, rm_text_list,
                  food_choices_price_list,separator_list,drinks_choices_list_numbers,  
                  drinks_choices_list, rm_text_list ,drinks_choices_price_list, spacings=spacings)
    

def print_main_ui():
      print_header_user_interface()
      print_user_interface()
      print_footer_interface()
      print_choice_msg()

 
