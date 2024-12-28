from food_and_drinks_choices import FOOD_CHOICES, FOOD_CHOICES_PRICES, DRINKS_CHOICES, \
                                     DRINKS_CHOICES_PRICES, SEPARATOR_LIST

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
   
def print_user_interface():
    # column 1
    food_choices_numbers_list = [i for i in range(1,21)]
    # column 2
    food_choices_list = [i for i in FOOD_CHOICES]
    # column 3
    food_choices_price_list = [i for i in FOOD_CHOICES_PRICES]
    # column 4
    separator_list = [i for i in SEPARATOR_LIST]
    # column 5
    drinks_choices_list_numbers = [i for i in range(41,61)]
    # column 6
    drinks_choices_list = [i for i in DRINKS_CHOICES]
    # column 7    
    drinks_choices_price_list = [i for i in DRINKS_CHOICES_PRICES]

    spacings = [6, 20, 20, 10, 10, 25, 10]  # Varying spaces between columns
    print_columns(food_choices_numbers_list, food_choices_list, \
                  food_choices_price_list,separator_list,drinks_choices_list_numbers,  
                  drinks_choices_list, drinks_choices_price_list, spacings=spacings)
    
  


        






