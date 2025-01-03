from typing import List

d = {}
list_user_item_orders = []

def insert_data_from_db(key:str,user_item_choice:str, 
                user_item_choice_price:float, 
                number_of_item:int) -> None:
    user_item_order = (user_item_choice, user_item_choice_price, number_of_item)
    list_user_item_orders.append(user_item_order)
    d[key] = list_user_item_orders


def read_data_from_db(key: str) -> List:
    return d[key]


