#메뉴를 선택한다.
#현금을 넣는다.
#구매한후에 거스름돈을 받는다.

menus = {"아메리카노": 4000, "카페라떼": 4500, "카푸치노": 5000}

print("=======메뉴판=======")

for name, price in menus.items():
    print(f"{name} : {price}원")

selected_menu = input("주문할 메뉴를 선택하세요.")
money = int(input("돈을 넣으세요."))

price = menus.get(selected_menu,0)
if price == 0:
    print("메뉴가 없습니다.")
else:
    change = money - price
    if change >= 0:
        print(f"{selected_menu}를 주문하셨습니다. 거스름돈은 {change}원 입니다.")
    else:
        print("돈이 부족합니다.")