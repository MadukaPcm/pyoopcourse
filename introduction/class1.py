class Student:
    #a constructor for class object initialization, and attribute definition
    total_marks = 1000
    def __init__(self,name,roll_no,marks):
        self.studentName = name
        self.studentNo = roll_no
        self.studentMarks = marks
        self.total_marks = Student.total_marks

    def result(self):
        if self.studentMarks >= 500:
            return "passed exam"
        else:
            return "failed exam"

#note self stands for student object you can use any name of yourr choice
student1 = Student("maduka",30,233)
student2 = Student("oyaa",345,900)
student3 = Student("goya",390,103)
student4 = Student("jjj",35,500)

li = [student1,student2,student3,student4]

passStudent = []
failStudent = []
student_result = []

for x in li:
    if x.result() == "passed exam":
        passStudent.append(x.studentName)
        student_result.append(x.studentMarks)
    else:
        failStudent.append(x.studentName)
        student_result.append(x.studentMarks)

class Product:
    def __init__(object,name,brand,model,price):
        object.name = name
        object.brand = brand
        object.model = model
        object.price = price
        object.nameWithBrand = name +' '+brand

    def discount(self,dscountvalue):
        discountAmount = (self.price/100)*dscountvalue
        final_price = self.price - discountAmount
        return int(final_price)

product1 = Product("oya","niaje","mwanangu",33000)

class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def circle_circumference(self):
        value_circle_circumference = 2*self.pi*self.radius
        return value_circle_circumference

    def circle_area(self):
        area = self.pi*self.radius**2
        return area

c = Circle(7)

class Laptop:
    discount = 10
    sno = 0
    def __init__(self,name,price):
        Laptop.sno += 1
        self.sno = Laptop.sno
        self.name = name
        self.price = price

    def applydiscount(self):
        discount_amount = (self.price/100)*Laptop.discount
        return discount_amount

hp00 = Laptop("hpi",200)
hp11 = Laptop("hp2",400)

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        # self.price = max(price,0)
        if price > 0:
            self.price = price
        else:
            self.price = 0

          # self.completeSpecification = f"{self.brand} {self.model_name} and price is {self.price}"

    @property
    def completeSpecification(self):
        return f"{self.brand} {self.model_name} and price is {self.price}"

    @staticmethod
    def make_a_call(phone_num):
        print(f"calling {phone_num}.....")

    def full_name(self):
        return f"{self.brand}{self.model_name}"

phone1 = Phone('nokia','1233',-900)

#student class
print("A student class")
print(student1.studentName)
print(student2.studentNo)
print(student1.result())
print(student1.total_marks)

print("\n")
print("Student result")
print(passStudent)
print(student_result)
print("\n")

#product class
print("The Product class")
print(product1.discount(6))
print(product1.price)
print(product1.nameWithBrand)
print("\n")

#dealing with circle area and circumference.
print("dealing with the circle:")
print('the circumference is ' + str(c.circle_circumference()))
print('the area is ' + str(c.circle_area()))
print("\n")

#dealing with laptop class
print("dealing with laptop class")
print('dictionary'+str(hp00.__dict__))
print("the applydiscount is "+str(hp00.applydiscount()))
print('dictionary'+str(hp11.__dict__))
print("\n")

#dealing with phones...
print("Dealing with phones")
print(phone1.brand)
print(phone1.completeSpecification)
print("\n")

#dealing with list.
print("Dealing with Lists")
li = [1,2,3,4,5]
#pop() method always retrieves the last element value in a list.

print(list.pop(li))
print(li.pop())



