products = {
    "Хлеб": 50,
    "Молоко": 80,
    "Яблоки": 120,
    "Сыр": 200,
    "Шоколад": 90,
    "Кофе": 300,
    "Чай": 150
}

if products:
    min_product = min(products, key=products.get)
    max_product = max(products, key=products.get)
    print(f"min: {min_product} - {products[min_product]}")
    print(f"max: {max_product} - {products[max_product]}")