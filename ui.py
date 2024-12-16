import itertools
from food_and_drinks_choices import FOOD_CHOICES, FOOD_CHOICES_PRICES, DRINKS_CHOICES, \
                                     DRINKS_CHOICES_PRICES



def print_header_user_interface():
    width_before_text = 20
    width_after_text = 20
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
    print(f"  {number_symbol}  {food_text_name}   {space_food_name_price}  {price_text}     {separate_symbol}", end="")
    print(f"  {number_symbol}  {drink_text_name}  {space_drink_name_price}  {price_text}  ")


def print_user_interface():
    width = 68
    food_choices_numbers_list = [i for i in range(1,21)]
    food_choices_list = [i for i in FOOD_CHOICES]
    food_choices_price_list = [i for i in FOOD_CHOICES_PRICES]
    drinks_choices_list_numbers = [i for i in range(41,61)]
    drinks_choices_list = [i for i in DRINKS_CHOICES]
    drinks_choices_price_list = [i for i in DRINKS_CHOICES_PRICES]

    for (num_of_food, food_item, food_item_price, num_of_drink, drink_item, drink_item_price) in  \
          zip(food_choices_numbers_list, food_choices_list, \
              food_choices_price_list, drinks_choices_list_numbers, \
              drinks_choices_list, drinks_choices_price_list):
        if num_of_food == 1:
            space_before = " " * 2
            space_one = " " * 4
            space_two = " " * 11
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 14
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 2:
            space_before = " " * 2
            space_one = " " * 4
            space_two = " " * 13
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 10
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 3:
            space_before = " " * 2
            space_one = " " * 4
            space_two = " " * 11
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 3
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 4:
            space_before = " " * 2
            space_one = " " * 4
            space_two = " " * 10
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 3
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 5:
            space_before = " " * 2
            space_one = " " * 4
            space_two = " " * 5
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 2
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 6:
            space_before = " " * 2
            space_one = " " * 4
            space_two = " " * 2
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 5
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 7:
            space_before = " " * 2
            space_one = " " * 4
            space_two = " " * 12
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 4
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 8:
            space_before = " " * 2
            space_one = " " * 4
            space_two = " " * 5
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 6
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 9:
            space_before = " " * 2
            space_one = " " * 4
            space_two = " " * 7
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 3
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 10:
            space_before = " " * 2
            space_one = " " * 3
            space_two = " " * 12
            space_three = " " * 4
            space_four = " "
            space_five = " " * 3
            space_six = " " * 2
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 11:
            space_before = " " * 2
            space_one = " " * 3
            space_two = " " * 13
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 14
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 12:
            space_before = " " * 2
            space_one = " " * 3
            space_two = " " * 9
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 15
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 13:
            space_before = " " * 2
            space_one = " " * 3
            space_two = " " * 12
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 13
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 14:
            space_before = " " * 2
            space_one = " " * 3
            space_two = " " * 10
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 10
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 15:
            space_before = " " * 2
            space_one = " " * 3
            space_two = " "
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 10
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 16:
            space_before = " " * 2
            space_one = " " * 3
            space_two = " " * 9
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 10
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 17:
            space_before = " " * 2
            space_one = " " * 3
            space_two = " " * 10
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 9
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 18:
            space_before = " " * 2
            space_one = " " * 3
            space_two = " " * 6
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 11
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 19:
            space_before = " " * 2
            space_one = " " * 3
            space_two = " " * 10
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 10
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
        elif num_of_food == 20:
            space_before = " " * 2
            space_one = " " * 3
            space_two = " " * 11
            space_three = " " * 5
            space_four = " "
            space_five = " " * 3
            space_six = " " * 14
            text_output_one =  f"{space_before} {num_of_food} {space_one} {food_item} {space_two} {food_item_price} {space_three}"
            text_output_two = f"{space_four} {num_of_drink}  {space_five} {drink_item} {space_six} {drink_item_price}"
            print(text_output_one, '|', text_output_two)
            

            


            


            

        




            






        






