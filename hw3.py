def get_fixed_price (discount_rate, discount_price):
    price=discount_price/(1 - discount_rate/100)
    return price

discount_rate = float(input('할인율은? '))
discount_price_A = float(input('상품의 할인된 가격은? '))
discount_price_B = float(input('상품의 할인된 가격은? '))

price_A = int(get_fixed_price (discount_rate, discount_price_A))
price_B = int(get_fixed_price (discount_rate, discount_price_B))

print('A 상품의 정가는',price_A,'원')
print('B 상품의 정가는',price_B,'원')
