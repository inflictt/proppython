# # # #eg
# # # a=10
# # # b=11
# # # sum=a+b
# # # diff=a-b
# # # print(sum)
# # # print(diff)

# # class Student:
# #     #default
# #     college_name="BML MUNJAL UNI"
# #     # name="raman munjal"
# #     def __init__(self,name,marks):
# #         pass
# #     #paramete
# #     def __init__(self,name,marks):
# #         self.name=name
# #         self.marks=marks
# #         print('creating a init function')

# #     def welcome(self):
# #         print('welcome student',self.name)

# # s1=Student("saksham",91)
# # s1.welcome()
    

# # # s1=Student("saksham",90)
# # # print(s1.name)
# # # print(s1.marks)
# # # print(Student.college_name)

# # # s2=Student("lakshya",89)
# # # print(s2.name)
# # # print(s2.marks)
# # # print(Student.college_name)

# # # s2=Student()
# # # print(s2.name)


# # # class Car:
# # #     color="blue"
# # #     brand="mercedes"
# # # c1=Car()
# # # c2=Car()
# # # print(c1.color)
# # # print(c1.brand)

# # create a student class that takes a name and marks of 3 subjectd as argument in constructor print avg

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         total = sum(self.marks)
#         avg = total / len(self.marks)
#         print(self.name, "your avg score is:", avg)

#     @staticmethod
#     def hello():
#         print('hello')
# s1 = Student("saksham", [90, 88, 69])
# s1.get_avg()
# s1.hello()
# # s2=Student("lakshya",[93,89,73])
# # s3=Student("vaibhav",[99,89,93]) 
# # s1.get_avg()
# # abstraction
# # excapsualation
# #inheritence
# #polymorphisim are the 4 pillars


# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False

#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("dhrooooooom car started")

# c1=Car()
# c1.start()  

class Account:
    def __init__(self,bal,accno):
        self.bal=bal
        self.accno=accno

    def debit(self,amount):
        self.bal -= amount
        print(f"rs {amount} was debited..")
        print("total bal = ",self.get_balance())

    def credit(self,amount):
        self.bal += amount
        print(f"rs {amount} was credited..")
        print("total bal = ",self.get_balance())


    def get_balance(self):
        return self.bal

acc1=Account(10000,12345)
# print(acc1.bal)
# print(acc1.accno)
acc1.debit(500)
acc1.credit(50000)