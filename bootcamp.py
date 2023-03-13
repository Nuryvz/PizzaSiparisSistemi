# pizza üst sınıfı
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    
# pizza alt sınıfı
class Classic(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza: sucuk, sosis, mısır, mozarella peyniri, yeşil biber, mantar, pizza sos", 160)

class Margarita(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza: mozarella peyniri, pizza sos", 140)

class Turk(Pizza):
    def __init__(self):
        super().__init__("Türk Pizza: sucuk, köz biber, mozarella peyniri, yeşil biber, mantar, pastırma, biftek, pizza sos", 190)

class Sade(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza: sucuk, zeytin, mozarella peynir, pizza sos", 150)                         

# decorator üst sınıfı
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component
        
    def get_cost(self):
        return self.component.get_cost()
    
    def get_description(self):
        return self.component.get_description()
    
    
# decorator alt sınıf    
class Olives(Decorator):
    def __init__(self, component):
        description = "Extra Zeytinli "
        cost = 6
        super().__init__(component)
        self.description = description + component.get_description()
        self.cost = component.get_cost() + cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost    

class Mushroom(Decorator):
    def __init__(self, component):
        description = "Extra Mantarlı "
        cost = 7
        super().__init__(component)
        self.description = description + component.get_description()
        self.cost = component.get_cost() + cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost       
    
class Cheese(Decorator):
    def __init__(self, component):
        description = "Keçi Peynirli "
        cost = 10
        super().__init__(component)
        self.description = description + component.get_description()
        self.cost = component.get_cost() + cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost    

class Meat(Decorator):
    def __init__(self, component):
        description = "Extra Etli "
        cost = 18
        super().__init__(component)
        self.description = description + component.get_description()
        self.cost = component.get_cost() + cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Onion(Decorator):
    def __init__(self, component):
        description = "Extra Soğanlı "
        cost = 8
        super().__init__(component)
        self.description = description + component.get_description()
        self.cost = component.get_cost() + cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost    

class Corn(Decorator):
    def __init__(self, component):
        description = "Extra Mısırlı "
        cost = 8
        super().__init__(component)
        self.description = description + component.get_description()
        self.cost = component.get_cost() + cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost    

# pizza sipariş ve kullanıcı bilgisi
import csv
from datetime import datetime
import datetime        

# menüyü okuma        
def read_menu():
    with open('Menu.txt', 'r') as menu_file:
        menu = menu_file.read()
        print(menu)   

# sistem başlangıcı ve sipariş
print("NUMNUM Pizzaya Hoşgeldiniz.")
read_menu()

while True:
    pizza_taban = int(input("Pizza Taban Seçimi İçin için Lütfen Uygun Numarayı Giriniz (1-4): "))

    if pizza_taban == 1:
        print("Klasik Pizza Seçiminiz Onaylanmıştır. Sos Seçimi İçin Devam Ediniz.")
        taban = Classic()
        break
    elif pizza_taban == 2:
        print("Margarita Pizza Seçiminiz Onaylanmıştır. Sos Seçimi İçin Devam Ediniz.")
        taban = Margarita()
        break
    elif pizza_taban == 3:
        print("Türk Pizza Seçiminiz Onaylanmıştır. Sos Seçimi İçin Devam Ediniz.")
        taban = Turk()
        break
    elif pizza_taban == 4:
        print("Sade Pizza Seçiminiz Onaylanmıştır. Sos Seçimi İçin Devam Ediniz.")
        taban = Sade()
        break
    else:
        print("Seçiminiz Onaylanmadı")  

while True:

    sos_secim = int(input("Sos Seçmek için Lütfen Uygun Numarayı Giriniz (11-16): "))  

    if sos_secim == 11:
        print("Zeytin eklenmiştir.")
        sos = Olives(taban)
        break
    elif sos_secim == 12:
        print("Mantar eklenmiştir.")
        sos = Mushroom(taban)
        break
    elif sos_secim == 13:
        print("Keçi Peyniri eklenmiştir.")
        sos = Cheese(taban)
        break
    elif sos_secim == 14:
        print("Et eklenmiştir.")
        sos = Meat(taban)
        break
    elif sos_secim == 15:
        print("Soğan eklenmiştir.")
        sos = Onion(taban)
        break
    elif sos_secim == 16:
        print("Mısır eklenmiştir.")  
        sos = Corn(taban)
        break
    else:
        print("Seçiminiz Onaylanmadı")

print("Ücret kısmına yönlendiriliyorsunuz.")   
total_cost = sos.get_cost()

# Kullanıcı Bilgileri
name = input("İsim Soyisim: ")

tc = input("TC: ")
while len(tc) != 11:
    print("TC kimlik numarası 11 haneli olmalıdır")
    tc = input("TC yeniden giriniz: ")

credit = input("Kredi Kart numarası: ")
parola = input("Kredi Kartı Şifresi: ")

with open('Orders_Database.csv','a') as read_file:
    writer = csv.writer(read_file)
    writer.writerow([name, tc, credit, parola, datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), sos.get_description(), total_cost])
read_file.close()

print(f"Siparişiniz oluşturuldu: {sos.get_description()}. Toplam Tutar: {total_cost} Bizi tercih ettiğiniz için teşekkürler. Afiyet Olsun.")

        