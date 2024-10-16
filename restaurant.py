restaurants = [
    {"name": "The Italian Restaurant", "cuisine_type": "Italian"},
    {"name": "Sushi House", "cuisine_type": "Japanese"},
    {"name": "Burger King", "cuisine_type": "American"},
    {"name": "Taco Bell", "cuisine_type": "Mexican"},
    {"name": "McDonald's", "cuisine_type": "American"}
]

print("\nRestaurants:")
for restaurant in restaurants:
    print(f"Name: {restaurant['name']}, Cuisine Type: {restaurant['cuisine_type']}")