def buy(lst):
    print('[구입]')
    item=input('상품명? ')
    if not item:
        return False
    num=int(input('수량은? '))
    shopping_bag[item]=num
    print()
    return True


def show(lst):
    print()
    print(f'장바구니 보기:{lst}')
    print()


def find(lst):
    print('[검색]')
    search=input('장바구니에서 확인하고자 하는 상품은? ')
    if search in lst:
        print(f'{search}은(는) {lst[search]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {search}은(는) 없습니다.')
    



shopping_bag={}
while True:
    if buy(shopping_bag)==False:
        break

show(shopping_bag)
find(shopping_bag)
