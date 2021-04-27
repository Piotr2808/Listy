ALLOWED_COMMAND = ["account balance", "sale", "purchase", "account", "warehouse", "overview"]
warehouse = {"mountain bike": 3,
             "sport shoes": 5,
             "ball": 4}

choose_items = {}
amount_of_money = 0
history_sale = {}
history_purchase = {}
history = []
while True:
    print("\nKomendy: account balance, sale, purchase, account, warehouse, overview")
    comm = input("Command: ")

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
                    summary_sale = [(f"Sprzedano {numbs_elements}: {element_sale} w cenie: {price} zł")]
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
                    summary_purchase = [(f"Zakupiono {numbs_elements}: {choose_items_to_purchase} w cenie: {price} zł")]
                    print(summary_purchase)
                    history += summary_purchase
                if amount_of_money < 0:
                    print("Bankrut")
                    break
            if not choose_items_to_purchase in warehouse:
                numbs_elements = int(input("Ilość: "))
                history_purchase.update({choose_items_to_purchase: numbs_elements})
                warehouse[choose_items_to_purchase] = numbs_elements
                price = float(input("Cena: ")) * numbs_elements
                amount_of_money -= price
                if amount_of_money > 0:
                    summary_purchase = [(f"Zakupiono {numbs_elements}: {choose_items_to_purchase} w cenie: {price} zł")]
                    print(summary_purchase)
                    history += summary_purchase
                if amount_of_money < 0:
                    print("Bankrut")
                    break
                summary_purchase = [(f"Zakupiono {numbs_elements}: {choose_items_to_purchase} w cenie: {price} zł")]
                print(summary_purchase)
                history += summary_purchase

# d) python accountant.py konto
        if comm == ALLOWED_COMMAND[3]:
            print(ALLOWED_COMMAND[3])

# e) python accountant.py magazyn <str identyfikator produktu 1>
# <str identyfikator produktu 2> <str identyfikator produktu 3> ...
        if comm == ALLOWED_COMMAND[4]:
            print(warehouse)

# f) python accountant.py przegląd
        if comm == ALLOWED_COMMAND[5]:
            print(ALLOWED_COMMAND[5])
    if not comm in ALLOWED_COMMAND:
        print("BAD COMMAND")
        continue