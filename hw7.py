shopping_bag={}
print('[구입]')
while True:
    item=input('상품명? ')
    if item=='':
        print()
        break
    num=int(input('수량은? '))
    print()

    shopping_bag[item]=num



print(f'장바구니 보기:{shopping_bag}')
print()

print('[검색]')
serch=input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{serch}은(는) {shopping_bag[serch]}개 담겨 있습니다.')
