def empty_fields(product_name, description, price, quantity):
    if product_name and description and price and quantity == "":
        return True
