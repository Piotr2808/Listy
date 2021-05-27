class Magazyn:
    def __init__(self):
        self.magazyn = {}
        self.read_magazyn_info()
        self.sale_()
        self.write_magazyn_info()

    def read_magazyn_info(self):
        with open("magazyn.txt", "r") as file:
            for line in file:
                rzecz = line.split(':')[0]
                ilosc = line[1]
                produkt_ = Produkt(rzecz, ilosc)
                self.magazyn = produkt_
    def sale_(self):
        rzecz = input("Przedmiot: ")
        ilosc = input("Ilośc: ")
        produkt = Produkt({rzecz, ilosc})

    def write_magazyn_info(self):
        with open("magazyn.txt", "w") as file:
            for cos in self.magazyn:
                file.write(str(cos.rzecz) + ':' + (str(cos.ilosc) + '\n'))

class Produkt:
    def __init__(self, rzecz, ilosc):
        self.rzecz = rzecz
        self.ilosc = ilosc
    def __repr__(self):
        return f"'{self.rzecz}': {self.ilosc}"

commands = ["account balance", "sale", "purchase", "account", "stop"]
mag = Magazyn()
while True:
    command = input("Czynność: ")
    if not command in commands:
        continue
    if command == "stop":
        break
    if command == "sale":
        mag.sale_()
        mag.write_magazyn_info()