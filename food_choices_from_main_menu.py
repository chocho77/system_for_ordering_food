from food_and_drinks_choices import FOOD_CHOICES, FOOD_CHOICES_PRICES

def food_choices(user_choice:int):
    food_choices_list = [i for i in FOOD_CHOICES]
    food_choices_prices_list = [i for i in FOOD_CHOICES_PRICES]
    if user_choice == 1:

        print(f"{food_choices_list[0]}     RM {food_choices_prices_list[0]}")
  

