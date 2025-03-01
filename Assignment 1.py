# Class representing a Customer in the Delivery System
class Customer:
    """Class to represent a customer with an ID, name, email, and delivery address."""
    def __init__(self, customer_id, name, email, address):
      self.__customer_id = customer_id
      self.__name = name
      self.__email = email
      self.__address = address

    # Getters and Setters methods to access private attributes
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    def get_address(self):
        return self.__address
    def set_address(self, address):
        self.__address = address


# Class representing an Item in an Order
class Item:
    """Class to represent an item with item code, description, quantity, and unit price."""
    def __init__(self, item_code, description, quantity, unit_price):
        self.__item_code = item_code
        self.__description = description
        self.__quantity = quantity
        self.__unit_price = unit_price

    # Getters and Setters methods to access private attributes
    def get_item_code(self):
        return self.__item_code

    def get_description(self):
        return self.__description
    def set_description(self, description):
        self.__description = description

    def get_quantity(self):
        return self.__quantity
    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_unit_price(self):
        return self.__unit_price
    def set_unit_price(self, unit_price):
        self.__unit_price = unit_price

    def get_total_price(self):
        """Calculate the total price of the item (quantity * unit price)."""
        return self.__quantity * self.__unit_price


# Class representing an Order placed by a Customer
class Order:
    """Class to represent an order with order number, reference number, delivery details, and items list."""
    def __init__(self, order_number, reference_number, delivery_date, delivery_method, total_weight, items):
        self.__order_number = order_number
        self.__reference_number = reference_number
        self.__delivery_date = delivery_date
        self.__delivery_method = delivery_method
        self.__total_weight = total_weight
        self.__items = items  # List of Item objects

    # Getters and Setters methods to access private attributes
    def get_order_number(self):
        return self.__order_number

    def get_reference_number(self):
        return self.__reference_number

    def get_delivery_date(self):
        return self.__delivery_date
    def set_delivery_date(self, delivery_date):
        self.__delivery_date = delivery_date

    def get_delivery_method(self):
        return self.__delivery_method
    def set_delivery_method(self, delivery_method):
        self.__delivery_method = delivery_method

    def get_total_weight(self):
        return self.__total_weight
    def set_total_weight(self, total_weight):
        self.__total_weight = total_weight

    def get_items(self):
        return self.__items
    def set_items(self, items):
        self.__items = items

    def calculate_subtotal(self):
        """Calculate the total price of all items in the order."""
        return sum(item.get_total_price() for item in self.__items)

    def calculate_taxes(self):
        """Calculate taxes (5% of subtotal)."""
        return round(self.calculate_subtotal() * 0.05, 2)

    def calculate_total_charges(self):
        """Calculate the final total (subtotal + taxes)."""
        return self.calculate_subtotal() + self.calculate_taxes()


# Class representing a Delivery Note generated for an Order
class DeliveryNote:
    """Class to represent a delivery note linked to a customer and an order."""

    def __init__(self, customer, order):
        self.__customer = customer
        self.__order = order

    def __str__(self):
        """Return the formatted delivery note for the customer as a string."""
        details = "=" * 50 + "\n"
        details += "\t\tDELIVERY NOTE\n"
        details += "=" * 50 + "\n"
        details += "Thank you for using our delivery service! Please print your receipt and present it upon receiving your items.\n"

        # Display recipient details
        details += "\nRecipient Details:\n"
        details += "  Name: " + self.__customer.get_name() + "\n"
        details += "  Contact: " + self.__customer.get_email() + "\n"
        details += "  Delivery Address: " + self.__customer.get_address() + "\n"

        # Display delivery information
        details += "\nDelivery Information:\n"
        details += "  Order Number: " + self.__order.get_order_number() + "\n"
        details += "  Reference Number: " + self.__order.get_reference_number() + "\n"
        details += "  Delivery Date: " + self.__order.get_delivery_date() + "\n"
        details += "  Delivery Method: " + self.__order.get_delivery_method() + "\n"
        details += "  Total Weight: " + str(self.__order.get_total_weight()) + " kg\n"

        # Display items in order
        details += "\nSummary of Items Delivered:\n"
        details += "-" * 60 + "\n"
        details += "Item Code\tDescription\t\tQty\tUnit Price (AED)\tTotal Price (AED)\n"
        details += "-" * 60 + "\n"

        for item in self.__order.get_items():
            details += f"{item.get_item_code()}\t{item.get_description()}\t\t{item.get_quantity()}\tAED {item.get_unit_price()}\t\tAED {item.get_total_price()}\n"

        # Display final charges
        details += "-" * 60 + "\n"
        details += "Subtotal:\t\t\t\t\tAED " + str(self.__order.calculate_subtotal()) + "\n"
        details += "Taxes and Fees (5%):\t\t\tAED " + str(self.__order.calculate_taxes()) + "\n"
        details += "=" * 60 + "\n"
        details += "Total Charges:\t\t\t\tAED " + str(self.__order.calculate_total_charges()) + "\n"
        details += "=" * 60 + "\n"

        return details

    def display(self):
        """Print the formatted delivery note."""
        print(str(self))


# Sample Data for Testing
customer = Customer(101, "Sarah Johnson", "sarah.johnson@example.com", "45 Knowledge Avenue, Dubai, UAE")

# Create item objects for the order
items = [
    Item("ITM001", "Wireless Keyboard", 1, 100.00),
    Item("ITM002", "Wireless Mouse & Pad", 1, 75.00),
    Item("ITM003", "Laptop Cooling Pad", 1, 120.00),
    Item("ITM004", "Camera.  Lock ", 3, 15.00),
]

# Create an order object
order = Order("DEL123456789", "DN-2025-001", "January 25, 2025", "Courier", 7, items)

# Generate a delivery note object
delivery_note = DeliveryNote(customer, order)

# Display the delivery note
delivery_note.display()
