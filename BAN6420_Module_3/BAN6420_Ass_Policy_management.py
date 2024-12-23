# Product Class creation
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.status = 'active'  # Product is active by default

    def update_product(self, name=None, price=None):
        if name:
            self.name = name
        if price:
            self.price = price
        print(f"Product {self.product_id} updated.")

    def suspend_product(self):
        self.status = 'suspended'
        print(f"Product {self.product_id} has been suspended.")

    def remove_product(self):
        self.status = 'removed'
        print(f"Product {self.product_id} has been removed.")

# Payment Class
class Payment:
    def __init__(self, amount, policyholder, product):
        self.amount = amount
        self.policyholder = policyholder
        self.product = product
        self.status = 'processed'  # Payment status can be processed or pending

    def process_payment(self):
        print(f"Payment of {self.amount} for {self.product.name} has been processed for {self.policyholder.name}.")
        self.policyholder.add_payment(self)
        self.product.status = 'active'  # Product remains active after successful payment

    def send_reminder(self):
        print(f"Reminder: Payment of {self.amount} is due for {self.product.name} by {self.policyholder.name}.")

    def apply_penalty(self):
        penalty = 10  # Example penalty amount
        print(f"Penalty of {penalty} applied to {self.policyholder.name} for {self.product.name}.")
        self.policyholder.add_payment(self)

# Policyholder Class
class Policyholder:
    def __init__(self, policyholder_id, name):
        self.policyholder_id = policyholder_id
        self.name = name
        self.status = 'active'  # By default, a policyholder is active
        self.products = []
        self.payments = []

    def register(self):
        self.status = 'active'
        print(f"Policyholder {self.name} has been registered.")

    def suspend(self):
        self.status = 'suspended'
        print(f"Policyholder {self.name} has been suspended.")

    def reactivate(self):
        self.status = 'active'
        print(f"Policyholder {self.name} has been reactivated.")

    def add_payment(self, payment):
        self.payments.append(payment)
        print(f"Payment of {payment.amount} has been added to {self.name}'s account.")

    def display_account_details(self):
        print(f"Policyholder: {self.name}, Status: {self.status}")
        print(f"Payments: {[payment.amount for payment in self.payments]}")
        print(f"Products: {[product.name for product in self.products]}")

    def add_product(self, product):
        if product.status == 'active':
            self.products.append(product)
            print(f"{self.name} has been enrolled in product {product.name}.")

# Demonstration with policyholders, products, and payments
# Create products
product1 = Product(1, "Health Insurance", 150)
product2 = Product(2, "Car Insurance", 200)

# Create policyholders
policyholder1 = Policyholder(101, "John Doe")
policyholder2 = Policyholder(102, "Jane Smith")

# Register policyholders
policyholder1.register()
policyholder2.register()

# Policyholders enroll in products
policyholder1.add_product(product1)
policyholder2.add_product(product2)

# Process payments
payment1 = Payment(150, policyholder1, product1)
payment1.process_payment()

payment2 = Payment(200, policyholder2, product2)
payment2.process_payment()

# Display account details for policyholders
policyholder1.display_account_details()
policyholder2.display_account_details()

# Suspend product and policyholder
product1.suspend_product()
policyholder1.suspend()

# Reactivate product and policyholder
product1.status = 'active'
policyholder1.reactivate()

# Suspend policyholder
policyholder2.suspend()
