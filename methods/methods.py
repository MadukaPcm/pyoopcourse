class Laptop:
    discount = 10
    sno = 0

    #class variable
    def __init__(self,name,price):
        Laptop.sno += 1
        self.sno = Laptop.sno
        self.name = name
        self.price = price

    #dealing with class method:
    @classmethod
    def from_string(clr,string):    # clr represents a class name
        import re   #use of re is just getting specific value from string.
        item = re.findall('is \w*',string)
        name = item[0][3:]
        price = item[1][3:]
        return clr(name,int(price))

    #INSTANCE METHOD.
    def applyDiscount(self):
        discount_amount = (self.price/100)*self.discount
        final_amount = self.price - discount_amount
        return  int(final_amount)


hp00 = Laptop('dell-09',200)
hp11 = Laptop.from_string('my laptop name is frank and price is 90000')

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #dealing with static method.
    @staticmethod
    def printstatement():
        print("This is a static method.")

#Arranging date format in day Month and Year.
class Date:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    def arrange_value_into_date(self):
        date = str(self.day) + '-' + str(self.month)+ '-' + str(self.year)
        return date

    @classmethod
    def getDataFromString(clr, string): #clr represeent the class name eg.Date
        import re
        date = re.findall('\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}', string)[0]
        list_date = date.replace('/','-').split('-')
        day = list_date[0]
        month = list_date[1]
        year = list_date[2]
        return clr(day,month,year)

    #static method.
    @staticmethod
    def setDatePattern(string):
        list1 = string.replace('/','-').split('-')
        date_update = list1[2]+ '-'+ list1[1] +'-'+ list1[0]
        return date_update

print("DEALING WITH CLASS METHOD:")
print(hp00.applyDiscount())
print("A dictionary from an object")
print(hp00.__dict__)
print("A dictionary for data extracted fro string only\n")
print(hp11.__dict__)
print("And its discount amount\n")
print(hp11.applyDiscount())

s00 = Student('Coder',23)
print("\nDEALING WITH STATIC METHOD:")
print(s00.__dict__)
print(s00.printstatement())

print("\nDealing with static method in arranging date:")
date00 = Date(2022,9,9)
print(date00.arrange_value_into_date())
date11 = Date.getDataFromString("today is 19-03-2022")
print("fetching a date from thestring: using a class method")
print(date11.arrange_value_into_date())
print("\nusing static method ffor date printing:")
date22 = Date(2022,2,9)
print(date22.setDatePattern('2022-02-09'))


