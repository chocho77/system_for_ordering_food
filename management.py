key = ""

def management_user_key_set(user_key:str):
    _user_key = user_key
    global key
    key = _user_key

def management_user_key_get()-> str:
    global key
    _user_key = key
    return _user_key



