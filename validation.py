from food_choices_from_main_menu import food_choices
from drink_choices_from_main_menu import drink_choices


def is_main_menu_input_valid(user_input: str) -> bool:
    is_digit =user_input.isdigit()
    is_letter_M = (user_input == "M")
    is_letter_S = (user_input == "S")
    is_letter_L = (user_input == "L")
    is_letter_P = (user_input == "P")
    is_letter_E = (user_input == "E")
    if is_letter_M:
         return True
    elif is_letter_S:
         return True
    elif is_letter_L:
         return True
    elif is_letter_P:
         return True
    elif is_letter_E:
         return True
    if not user_input.isdigit():
        return False
    return True

def valid_success(user_input: str) -> int:
     return int(user_input)

def map_user_input(user_input_num: int):
        print()
        print(103 * "_")
        if user_input_num >= 1 and user_input_num <= 20: # filter food choices
            food_choices(user_input_num)
        elif user_input_num >= 41 and user_input_num <= 60: # filter drink choices
            drink_choices(user_input_num)
    
