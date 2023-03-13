#pizza ordering system project

#Gerekli Kitaplıkları İçe Aktarma
import datetime
import csv


class Pizza:
  def get_description(self):
    return self.__class__.__name__
  
  def get_cost(self):
    return self.__class__.cost
  
class Klasik(Pizza):
    cost = 50

    def __init__(self):
        self.description = "Kaşar, Biber, Zeytin"
        print(self.description +"\n")
class Margarita(Pizza):
    cost = 40

    def __init__(self):
        self.description = "Mozeralla, Fesleğen"
        print(self.description +"\n")

class TurkPizza(Pizza):
    cost = 70

    def __init__(self):
        self.description = "Kaşar, Biber, Pastırma"
        print(self.description +"\n")
class Sade(Pizza):
    cost = 50

    def __init__(self):
        self.description = " "
        print(self.description +"\n")

class Decorator(Pizza):
    def __init__(self, topping):
        self.component = topping

    def get_cost(self):
        return self.component.get_cost() + \
          Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
          ' : ' + Pizza.get_description(self)
class Zeytin(Decorator):
    cost = 3

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Mantar(Decorator):
    cost = 5

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Kecipeyniri(Decorator):
    cost = 7

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Et(Decorator):
    cost = 8

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Sogan(Decorator):
    cost = 5

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Misir(Decorator):
    cost = 5

    def __init__(self, topping):
        Decorator.__init__(self, topping)

def main():
    with open("menu.txt", "r",  newline='',          encoding='utf-8') as menu:
      print(menu.read())
    class_number = {1: Klasik, 
                  2: Margarita, 
                  3: TurkPizza, 
                  4: Sade, 
                  11: Zeytin, 
                  12: Mantar, 
                  13: Kecipeyniri, 
                  14: Et, 
                  15: Sogan, 
                  16: Misir}

    pizzanumber = input("Lütfen Bir Pizza Seçiniz: ")
    while pizzanumber not in ["1", "2", "3", "4"]:
        pizzanumber = input("Seçim Hatalı: ")

    order = class_number[int(pizzanumber)]()

    while pizzanumber != "x":
        pizzanumber = input("Ekstra malzemeler seçiniz ve x tuşuna basınız]: ")
        if pizzanumber in ["11", "12", "13", "14", "15", "16"]:
            order = class_number[int(pizzanumber)](order)
    print("\n"+order.get_description().strip() +
          ": ₺" + str(order.get_cost()))
    print("\n")

    print("Sipariş Detayları\n")
    name = input("İsim: ")
    ID = input("Kimlik No: ")
    credit_card = input("Kredi Kartı No: ")
    credit_pass = input("Kredi Kartı Şifresi: ")
    time_of_order = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow(["İsim","Kimlik No","Kredi Kartı No","Kredi Kartı Şifresi", "Acıklama", "Tarih"])
        orders.writerow([name, ID, credit_card, credit_pass, order.get_description(), time_of_order])
    print("Siparişiniz Alındı.")

if __name__ == '__main__':
    main()
