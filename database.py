from typing import List, Dict

d = {}
list_user_item_orders = []

def insert_data_from_db(key:str,user_item_choice:str, 
                user_item_choice_price:float, 
                number_of_item:int) -> None:
    user_item_order = (user_item_choice, user_item_choice_price, number_of_item)
    global d, list_user_item_orders
    list_user_item_orders.append(user_item_order)
    d[key] = list_user_item_orders


def read_data_from_db(key: str) -> List:
    return d[key]

def extract_list_user_item_orders() -> List:
    global list_user_item_orders
    _list_user_item_orders = list_user_item_orders
    return _list_user_item_orders

def empty_list_user_item_orders() -> None:
    global list_user_item_orders
    list_user_item_orders.clear()

def read_db() -> Dict:
    global d
    return d



