import re


# checking for empty fields
def checK_empty_field(*args):
    for data in args:
        if data == "":
            return True


# checking correct data type
def check_types(product_name, description, quantity, price):
    if not isinstance(product_name, str):
        return True
    if not isinstance(description, str):
        return True
    if not isinstance(quantity, int):
        return True
    if not isinstance(price, int):
        return True


# checking for white spaces
def check_remove_white_spaces(*args):
    for data in args:
        if data.isspace():
            return True
