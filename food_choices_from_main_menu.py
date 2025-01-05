from food_and_drinks_choices import FOOD_CHOICES, FOOD_CHOICES_PRICES
from database import insert_data_from_db
from management import management_user_key_get, management_user_key_validation

def food_choices(user_choice:int):
    food_choices_list = [i for i in FOOD_CHOICES]
    food_choices_prices_list = [i for i in FOOD_CHOICES_PRICES]

    if user_choice == 1:
        management_user_key_validation()
        key = management_user_key_get()
        print(f"{food_choices_list[0]}     RM {food_choices_prices_list[0]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        insert_data_from_db(key, food_choices_list[0], food_choices_prices_list[0],
                             number_of_items)
        
    elif user_choice == 2:
        management_user_key_validation()
        key = management_user_key_get()
        print(f"{food_choices_list[1]}     RM {food_choices_prices_list[1]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        insert_data_from_db(key, food_choices_list[1], food_choices_prices_list[1],
                            number_of_items)

    elif user_choice == 3:
        management_user_key_validation()
        key = management_user_key_get()
        print(f"{food_choices_list[2]}     RM {food_choices_prices_list[2]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        insert_data_from_db(key, food_choices_list[2], food_choices_prices_list[2],
                            number_of_items)
        
    elif user_choice == 4:
        management_user_key_validation()
        key = management_user_key_get()
        print(f"{food_choices_list[3]}     RM {food_choices_prices_list[3]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        insert_data_from_db(key, food_choices_list[3], food_choices_prices_list[3],
                            number_of_items)
        
    elif user_choice == 5:
        print(f"{food_choices_list[4]}     RM {food_choices_prices_list[4]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        
    elif user_choice == 6:
        print(f"{food_choices_list[5]}     RM {food_choices_prices_list[5]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        
    elif user_choice == 7:
        print(f"{food_choices_list[6]}     RM {food_choices_prices_list[6]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        
    elif user_choice == 8:
        print(f"{food_choices_list[7]}     RM {food_choices_prices_list[7]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        
    elif user_choice == 9:
        print(f"{food_choices_list[8]}     RM {food_choices_prices_list[8]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        
    elif user_choice == 10:
        print(f"{food_choices_list[9]}     RM {food_choices_prices_list[9]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        
    elif user_choice == 11:
        print(f"{food_choices_list[10]}     RM {food_choices_prices_list[10]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        
    elif user_choice == 12:
        print(f"{food_choices_list[11]}     RM {food_choices_prices_list[11]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        
    elif user_choice == 13:
        print(f"{food_choices_list[12]}     RM {food_choices_prices_list[12]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        
    elif user_choice == 14:
        print(f"{food_choices_list[13]}     RM {food_choices_prices_list[13]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        
    elif user_choice == 15:
        print(f"{food_choices_list[14]}     RM {food_choices_prices_list[14]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        
    elif user_choice == 16:
        print(f"{food_choices_list[15]}     RM {food_choices_prices_list[15]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        
    elif user_choice == 17:
        print(f"{food_choices_list[16]}     RM {food_choices_prices_list[16]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        
    elif user_choice == 18:
        print(f"{food_choices_list[17]}     RM {food_choices_prices_list[17]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items) 
        
    elif user_choice == 19:
        print(f"{food_choices_list[18]}     RM {food_choices_prices_list[18]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
    
    elif user_choice == 20:
        print(f"{food_choices_list[19]}     RM {food_choices_prices_list[19]}")
        number_of_items = int(input("How Many You Want to Order?: "))
        print(number_of_items)
        





  

