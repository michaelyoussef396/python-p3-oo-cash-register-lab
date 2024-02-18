#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100.0)
            self.total -= discount_amount
            # Check if total is an integer and format accordingly
            if self.total.is_integer():
                message = f"After the discount, the total comes to ${self.total:.0f}.\n"
            else:
                message = f"After the discount, the total comes to ${self.total:.2f}.\n"
        else:
            message = "There is no discount to apply.\n"
        print(message.strip())  # Ensure the message is printed without extra newlines
        return message.strip()  # Ensure the return value matches the printed message

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        if self.items:
            title = self.items.pop()  # Optionally capture the title of the item being removed, if needed
