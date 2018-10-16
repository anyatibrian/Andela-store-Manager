product_list = []


class Products:
    """the that initializes all the instance of a product"""
    def __init__(self):
        pass

    def create_product(self, product_name, description, quantity, price):
        """the function that enables product creation and appends to the list"""
        products = {
            'product_id': len(product_list)+1,
            'product_name': product_name,
            'description': description,
            'quantity': quantity,
            'price': price
        }
        product_list.append(products)
        return product_list
