class Phone:  #Base ./Parent class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    # def make_a_call(self,phone_num):
    #     print(f"calling.. {phone_num}\n")

    @staticmethod
    def make_a_call(phone_num):
        print(f"calling.. {phone_num}\n")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


class SmartPhone(Phone):  #A child class.
    def __init__(self, brand, model_name, price,ram,internal_memory,rare_camera):
        #Un common way of doing ./Inherirint method.
        #Phone.__init__(self, brand, model_name, price)

        #common way used by deveelopers for class inheritance with its methods ./attri
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rare_camera = rare_camera

class SmartPhone2(SmartPhone):  #A child class.
    def __init__(self, brand, model_name, price,ram,internal_memory,rare_camera):
        #Un common way of doing ./Inherirint method.
        #Phone.__init__(self, brand, model_name, price)

        #common way used by deveelopers for class inheritance with its methods ./attri
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rare_camera = rare_camera

class FlagShip(SmartPhone):  #A child class.
    def __init__(self, brand, model_name, price,ram,internal_memory,rare_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rare_camera)
        self.front_camera = front_camera

print("Dealing with Phone class\n")
phone1 = Phone('nokia','Majani',4000)
print(phone1.__dict__['brand'])
print(phone1.make_a_call('0620141577'))
print(f"{phone1.full_name()}\n")

print("Dealing with Smart Phone class\n")
phone2 = SmartPhone('samsung','A7',4000,'4gb','128gb','25MP')
print(phone2.__dict__)
print(phone2.make_a_call('0620141577'))
print(phone2.full_name())

print("Dealing with flag ship class\n")
oneflag = FlagShip('samsung','A7',4000,'4gb','128gb','25MP','kk')
print(f'{oneflag.__dict__}\n')
print(oneflag.make_a_call('0620141577'))
print(oneflag.full_name())


# **************** .OOP TERMINOLOGIES. **************
#
# ABSTRACTION: Is the process of hiding functionalities defined within the same class ftom being accessed
#             Eg: A class is having two methods that have task to be done by two programmers
#             Where either programmer can not see task done by his or her fellow.
# ENCAPSULATION: Is the process of placing methods and attributes related in the same class.