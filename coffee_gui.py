import tkinter as tk
from tkinter import messagebox

class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        messagebox.showinfo("Order", f"Added {coffee.name} to your order")

    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            messagebox.showinfo("Order", "No items in order")
            return
        order_text = "\n".join([f"{i+1}. {item.name} - ${item.price}" 
                                for i, item in enumerate(self.items)])
        order_text += f"\n\nTotal: ${self.total():.2f}"
        messagebox.showinfo("Your Order", order_text)

    def checkout(self):
        if not self.items:
            messagebox.showinfo("Checkout", "Your cart is empty.")
            return
        self.show_order()
        confirm = messagebox.askyesno("Checkout", "Proceed to checkout?")
        if confirm:
            messagebox.showinfo("Checkout", "Order Confirmed! Thank you.")
            self.items.clear()
        else:
            messagebox.showinfo("Checkout", "Checkout cancelled")

def main():
    menu = [
        Coffee("Espresso", 2.5),
        Coffee("Latte", 3.5),
        Coffee("Cappuccino", 3.0),
        Coffee("Americano", 2.0)
    ]

    order = Order()

    root = tk.Tk()
    root.title("Coffee App")
    root.geometry("300x400")

    tk.Label(root, text="--- Coffee Menu ---", font=("Arial", 14)).pack(pady=10)

    for coffee in menu:
        btn = tk.Button(root, text=f"{coffee.name} - ${coffee.price}",
                        command=lambda c=coffee: order.add_item(c))
        btn.pack(pady=5)

    tk.Button(root, text="View Order", command=order.show_order).pack(pady=10)
    tk.Button(root, text="Checkout", command=order.checkout).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
