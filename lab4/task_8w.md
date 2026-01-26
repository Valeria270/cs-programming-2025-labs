purchase_amount = float(input("Введите сумму покупки: "))

if purchase_amount >= 10000:
    discount_percent = 15
elif purchase_amount >= 5000:
    discount_percent = 10
elif purchase_amount >= 1000:
    discount_percent = 5
else:
    discount_percent = 0

final_amount = purchase_amount * (1 - discount_percent / 100)

print(f"Ваша скидка: {discount_percent}%")
print(f"К оплате: {final_amount}")