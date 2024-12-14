import itertools
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
    food_choices_list_numbers = [i for i in range(1,21)]
    food_choices_list = [i for i in FOOD_CHOICES]
    food_choices_price_list = [i for i in FOOD_CHOICES_PRICES]
    for (a, b, c) in zip(food_choices_list_numbers, food_choices_list, food_choices_price_list):
        print(a, b, c)


    #for i, choice in enumerate(FOOD_CHOICES, start=1):
    #    if i< 10:
    #        print(f"   ({i})    {choice}")
    #    elif i >= 10:
    #        print(f"   ({i})   {choice}")





