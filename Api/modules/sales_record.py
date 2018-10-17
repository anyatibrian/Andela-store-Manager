sales_records = []


class SalesRecord:
    def __init__(self):
        pass

    def create_sales_records(self, attendant_name, product_name, quantity, unit_price):
        grand_total = int(unit_price) * int(quantity)
        records = {
            "id": len(sales_records)+1,
            "attendant": attendant_name,
            "product": product_name,
            "quantity": quantity,
            "unit_price": unit_price,
            "grand_total": str(grand_total) + "{}".format("ugx")

        }
        sales_records.append(records)
        return sales_records
