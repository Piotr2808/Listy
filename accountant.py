saldo = open("saldo.txt", "a+")
saldo_read = open("saldo.txt", "r+")

import linecache

saldo_line = len(open("saldo.txt", "r").readlines())
wiersz_saldo = linecache.getline("saldo.txt", saldo_line)
for s in wiersz_saldo.split():
    pass # print(f"\n{s}", end='')
    linia = s
    tab = linia.split(",")
    tab = [float(x) for x in tab]
    aom = float(linia)

ALLOWED_COMMAND = ["account balance", "sale", "purchase", "account", "stop"]

warehouse = {}
choose_items = {}
amount_of_money = aom
history_sale = {}
history_purchase = {}
history = []
def his_read():
    with open("historia.txt", "r") as file_:
        for l_ in file_.readlines():
            line_ = l_.split("\n")[0]
            history.append(line_)
def ware_read():
    with open("magazyn.txt", "r") as file:
        for l in file.readlines():
            name = l.split("\n")[0].split(",")[0]
            wart = int(l.split("\n")[0].split(",")[1])
            warehouse[name] = wart
ware_read()
his_read()

while True:
    print("\nKomendy: account balance, sale, purchase, account, stop.")
    print("\nUwaga! Komenda: stop wyłącza program!")
    comm = input("Komenda: ")

    # a) python accountant.py saldo <int wartosc> <str komentarz>
    if comm in ALLOWED_COMMAND:
        if comm == ALLOWED_COMMAND[0]:
            print(f"Saldo: {amount_of_money} zł \nHistory:\n{history}")
            print(f"Hisotria sprzedaży: {history_sale}")
            print(f"Historia zakupów {history_purchase}")

    # b) python accountant.py sprzedaż <str identyfikator produktu> <int cena> <int liczba sprzedanych>
        if comm == ALLOWED_COMMAND[1]:
            print(f"Magazyn: {warehouse}")
            element_sale = input("Produkt: ")
            if element_sale in warehouse:
                numbs_elements = int(input("Ilość: "))
                if numbs_elements > 0 and numbs_elements <= warehouse[element_sale]:
                    warehouse[element_sale] -= numbs_elements
                    price = float(input("Cena: ")) * numbs_elements
                    history_sale.update({element_sale: numbs_elements})
                    amount_of_money += price
                    summary_sale = [(f"Sprzedano {numbs_elements}: {element_sale} w cenie: {price} zl")]
                    history += summary_sale
                    print(summary_sale)
                if not warehouse[element_sale] > 0:
                    print("Brak wystarczającej ilości towaru!")
                    print(warehouse)
                    continue
            if not element_sale in warehouse:
                print("Wprowadź ponownie komendę!")
                continue

    # c) python accountant.py zakup <str identyfikator produktu> <int cena> <int liczba zakupionych>
        if comm == ALLOWED_COMMAND[2]:
            print(warehouse)
            choose_items_to_purchase = input("Zakupiony produkt: ")
            if choose_items_to_purchase in warehouse:
                numbs_elements = int(input("Ilość: "))
                warehouse[choose_items_to_purchase] += numbs_elements
                history_purchase.update({choose_items_to_purchase: numbs_elements})
                price = float(input("Cena: ")) * numbs_elements
                amount_of_money -= price
                if amount_of_money > 0:
                    summary_purchase = [(f"Zakupiono {numbs_elements}: {choose_items_to_purchase} w cenie: {price} zl")]
                    print(summary_purchase)
                    history += summary_purchase
                if amount_of_money < 0:
                    print("Bankrut")
                    break
            if not choose_items_to_purchase in warehouse:
                numbs_elements = int(input("Ilość: "))
                history_purchase.update({choose_items_to_purchase: numbs_elements})
                warehouse[choose_items_to_purchase] = numbs_elements
                price_items = float(input("Cena: "))
                price = price_items * numbs_elements
                amount_of_money -= price
                summary_purchase = [(f"Zakupiono {numbs_elements}: {choose_items_to_purchase} w cenie: {price} zl")]
                if amount_of_money > 0:
                    history += summary_purchase
                if amount_of_money < 0:
                    print("Bankrut")
                    break
                print(summary_purchase)


    # d) python accountant.py konto
        if comm == ALLOWED_COMMAND[3]:
            action = ['Payment of money', 'Money payment']
            print("Wypłata środków (Payment of money) lub wpłata środków(Money payment):")
            command = input("Payment of money/ Money payment: ")
            if not command in action:
                print("Powtórz czynność.")
                continue
            if command == action[0]:
                print(f"Twoje saldo wynosi: {amount_of_money}")
                payment_of_money = int(input("Kwota do wypłaty: "))
                if payment_of_money > amount_of_money:
                    print("Niewystraczająca liczba środków!")
                    continue
                if payment_of_money <= amount_of_money:
                    amount_of_money -= payment_of_money
                summary_payment_of_money = [(f"Wypłacono {payment_of_money}. Twój stan konta: {amount_of_money}.")]
                history += summary_payment_of_money
                print(summary_payment_of_money)
            if command == action[1]:
                print(f"Twoje saldo wynosi: {amount_of_money}")
                money_payment = int(input("Kwota do wpłaty: "))
                amount_of_money += money_payment
                summary_money_payment = [(f"Wpłacono {money_payment}. Twój stan konta: {amount_of_money}.")]
                print(summary_money_payment)
                history += summary_money_payment
    if not comm in ALLOWED_COMMAND:
        print("BAD COMMAND")
        continue
    if comm == ALLOWED_COMMAND[4]:
        magazyn = open("magazyn.txt", "w")
        for name, value in warehouse.items():
            magazyn.write(str(name) + ',' + str(value) + '\n')
        saldo.write(f"\n{amount_of_money}\n")
        his = open("historia.txt", "w")
        for name_ in history:
            his.write(str(name_) + '\n')
        break