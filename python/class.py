# #Create class
# class school:
# #class property
#     school="abc schcool"
#     school_time="9:00am to 4:00pm"
#     school_location="cheannai"
#     #object property(method)
#     def __init__(self,name,age,id,std):
#         self.name=name
#         self.age=age
#         self.id=id
#         self.std=std
#     #object property accuss(object method)
#     def display_student(self):
#         print(self.name,self.age,self.id,self.std)
#     #object property motification(object method)
#     def ch_student_property(self,new_name,new_age,new_id,new_std):
#         self.name=new_name
#         self.age=new_age
#         self.id=new_id
#         self.std=new_std
#     def ch_student_name(self,new_name):
#            self.name=new_name
#     def ch_student_age(self,new_age):
#            self.age=new_age
#     def ch_student_id(self,new_id):
#            self.id=new_id
#     def ch_student_std(self,new_std):
#            self.std=new_std
#     #class property accuss
#     @classmethod
#     def display_class(cls):
#         print(cls.school,cls.school_time,cls.school_location)
#     #class property motification
#     @classmethod
#     def ch_class(cls,new_school,new_school_time,new_school_location):
#         cls.school=new_school
#         cls.school_time=new_school_time
#         cls.school_location=new_school_location

# #create object
# s1=school("selva",22,123151358,"B.Com")
# s1.display_student()
# s1.display_class()
# s1.ch_student_property("kevin",22,12312390,"M.com")
# s1.display_student()
# s1.ch_student_name("god")
# s1.display_student()
        
        
        

# #Create class(single inheritance)
# class school:
# #class property
#     school="abc schcool"
#     school_time="9:00am to 4:00pm"
#     school_location="cheannai"
#     #object property(method)
#     def __init__(self,name,age,id,std):
#         self.name=name
#         self.age=age
#         self.id=id
#         self.std=std
#     #object property accsus(object method)
#     def display_student(self):
#         print(self.name,self.age,self.id,self.std)
#     #object property motification(object method)
#     def ch_student_property(self,new_name,new_age,new_id,new_std):
#         self.name=new_name
#         self.age=new_age
#         self.id=new_id
#         self.std=new_std
#     def ch_student_name(self,new_name):
#            self.name=new_name
#     def ch_student_age(self,new_age):
#            self.age=new_age
#     def ch_student_id(self,new_id):
#            self.id=new_id
#     def ch_student_std(self,new_std):
#            self.std=new_std

# class collage(school):
#       def __init__(self,collage_name):
#             super().__init__(name, age, id, std)
#             self.collage_name=collage_name

#       def display_collage(self):
#             print(f"collage name: {self.collage_name}\nname: {self.name}")



# s1=school("selva",22,123151358,"B.Com")
# s1.display_student()
# s1=collage("abc collage")
# s1.display_collage()


# #Create class(multilevel inheritance)
# class Employee:
#     #object property(method)
#     def __init__(self,name):
#         self.name=name
    
# class Developer(Employee):
#     def __init__(self,name,programming_language):
#         super().__init__(name)
#         self.programming=programming_language
    
# class BackendDeveloper(Developer):
#     def __init__(self, name, programming_language,framework):
#         super().__init__(name, programming_language)
#         self.framework=framework
#     def display_all(self):
#         print(f"name: {self.name}")
#         print(f"programming_language: {self.programming}")   
#         print(f"framework: {self.framework}")           

        

# u1=BackendDeveloper("selva","python","Django")
# u1.display_all()




# class person:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f"person: {self.name}")
# class student(person):
#     def __init__(self,name,student_id):
#         person.__init__(self,name)
#         super().display()
#         self.student_id=student_id
# class teacher(person):
#     def __init__(self, name,subject):
#         person.__init__(self,name)
#         super().display()
#         self.subject=subject
# class both(student,teacher):
#     def __init__(self,name,student_id,subject):
#         student.__init__(self,name,student_id)
#         teacher.__init__(self,name,subject)
#         print(f"both:-\nname: {self.name}\nstudent id: {self.student_id}\nsubject: {self.subject}")


# s1=both("selva",123456789,"python")
# print(both.mro())

#abstract method
from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class upi(payment):
    def pay(self):
        print("upi payment")
class credit(payment):
    def pay(payment):
        print("credit payment")
class debit(payment):
    def pay(self):
        print("debit payment")


p1=upi()
p1.pay()
p2=credit()
p2.pay()
p3=debit()
p3.pay()

  