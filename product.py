products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Smartphone", "price": 600},
    {"name": "Headphones", "price": 150},
    {"name": "Keyboard", "price": 80},
    {"name": "Mouse", "price": 30}
]

print("Products:")
for product in products:
    print(f"Name: {product['name']}, Price: ${product['price']}")
