product_list = []


class Products:
    def __init__(self):
        pass

    def create_product(self, product_name, description, quantity, price):
        product = {
            "id": len(product_list)+1,
            "product_name": product_name,
            "description": description,
            "quantity": quantity,
            "price": price

        }
        product_list.append(product)
        return product_list