from typing import List
from database import empty_list_user_item_orders


key = ""
user_keys = []

def is_input_key_different() -> bool:
    global user_keys
    _user_keys = []
    _user_keys = user_keys.copy()
   
    for i in _user_keys:
        if i is not management_user_key_get():
            return True
    return False 

def management_user_key_set(user_key:str):
    _user_key = user_key
    global key
    key = _user_key

def management_user_key_get()-> str:
    global key
    _user_key = key
    return _user_key

def management_user_key_record(user_key:str):
    global user_keys
    user_keys.append(user_key)

def management_user_keys_records_get_all() -> List:
    global user_keys
    _user_keys = []
    _user_keys = user_keys
    return _user_keys


def management_input_user_key_different()-> None:
    if is_input_key_different():
        empty_list_user_item_orders()
