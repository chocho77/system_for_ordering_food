from food_and_drinks_choices import FOOD_CHOICES, FOOD_CHOICES_PRICES


def print_header_user_interface():
    width_before_text = 20
    width_after_text = 20
    width_text = 28
    symbols_print_before_text = width_before_text * "*"
    symbols_print_after_text = width_after_text * "*"
    main_message = "ORDER FOODS & DRINKS".center(width_text)
    number_symbol = '|No|'
    food_text_name = '|FOOD NAME|'
    drink_text_name = '|DRINK NAME|'
    price_text = '|PRICE|'
    separate_symbol = '|'
    
    print(f"{symbols_print_before_text} {main_message} {symbols_print_after_text}")
    print(f"  {number_symbol}  {food_text_name}     {price_text}    {separate_symbol}", end="")
    print(f"  {number_symbol}  {drink_text_name}      {price_text}  ")


def print_user_interface():
    #print("Called from ui.py module print_user_interface()")
    for i, choice in enumerate(FOOD_CHOICES, start=1):
        if i< 10:
            print(f"   ({i})    {choice}")
        elif i >= 10:
            print(f"   ({i})   {choice}")





