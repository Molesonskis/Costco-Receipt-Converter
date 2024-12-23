class CostcoReceiptCalculator:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, tax_code, quantity=1, discount=0):
        vat_rates = {"0": 0.0, "20": 0.20}
        if tax_code not in vat_rates:
            print("Invalid tax code. Use '0' or '20'.")
            return

        vat_rate = vat_rates[tax_code]
        price_after_discount = price - discount
        total_price = price_after_discount * (1 + vat_rate) * quantity
        vat_amount = price_after_discount * vat_rate * quantity

        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "tax_code": tax_code,
            "vat_amount": vat_amount,
            "discount": discount,
            "total_price": total_price,
        })

    def print_receipt(self):
        if not self.items:
            print("No items in the receipt.")
            return

        print("\n--- Simplified Receipt ---")
        total_without_vat = 0
        total_vat = 0
        total_discount = 0
        total_price = 0

        for item in self.items:
            print(f"Item: {item['name']}")
            print(f"  Price: £{item['price']:.2f} x {item['quantity']}")
            print(f"  VAT ({item['tax_code']}%): £{item['vat_amount']:.2f}")
            print(f"  Discount per unit: £{item['discount']:.2f}")
            print(f"  Total: £{item['total_price']:.2f}\n")

            total_without_vat += (item['price'] - item['discount']) * item['quantity']
            total_vat += item['vat_amount']
            total_discount += item['discount'] * item['quantity']
            total_price += item['total_price']

        print("--- Totals ---")
        print(f"Subtotal (without VAT): £{total_without_vat:.2f}")
        print(f"Total VAT: £{total_vat:.2f}")
        print(f"Total Discounts: £{total_discount:.2f}")
        print(f"Grand Total: £{total_price:.2f}")

    def run(self):
        while True:
            print("\nCostco Receipt Calculator")
            print("1. Add item")
            print("2. Print receipt")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter item name: ")
                try:
                    price = float(input("Enter item price (pre-tax): "))
                except ValueError:
                    print("Invalid price. Please enter a number.")
                    continue

                try:
                    quantity = int(input("Enter quantity: "))
                except ValueError:
                    print("Invalid quantity. Please enter an integer.")
                    continue

                tax_code = input("Enter tax code (0, 5, 20): ")
                try:
                    discount = float(input("Enter discount (per unit, if any, default 0): ") or 0)
                except ValueError:
                    print("Invalid discount. Please enter a number.")
                    continue

                self.add_item(name, price, tax_code, quantity, discount)

            elif choice == "2":
                self.print_receipt()

            elif choice == "3":
                print("Exiting calculator. Goodbye!")
                break

            else:
                print("Invalid choice. Please select again.")

if __name__ == "__main__":
    app = CostcoReceiptCalculator()
    app.run()
