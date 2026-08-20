class school:
#class property
    school="abc schcool"
    school_time="9:00am to 4:00pm"
    school_location="cheannai"
    #object property
    def __init__(self,name,age,id,std):
        self.name=name
        self.age=age
        self.id=id
        self.std=std
    #object property information
    def display_student(self):
        print(self.name,self.age,self.id,self.std)
    #object property motification
    def ch_student_property(self,new_name,new_age,new_id,new_std):
        self.name=new_name
        self.age=new_age
        self.id=new_id
        self.std=new_std
    def ch_student_name(self,new_name):
           self.name=new_name
    def ch_student_age(self,new_age):
           self.age=new_age
    def ch_student_id(self,new_id):
           self.id=new_id
    def ch_student_std(self,new_std):
           self.std=new_std
    #class property information
    @classmethod
    def display_class(cls):
        print(cls.school,cls.school_time,cls.school_location)
    #class property motification
    @classmethod
    def ch_class(cls,new_school,new_school_time,new_school_location):
        cls.school=new_school
        cls.school_time=new_school_time
        cls.school_location=new_school_location

s1=school("selva",22,123151358,"B.Com")
s1.display_student()
s1.display_class()
s1.ch_student_property("kevin",22,12312390,"M.com")
s1.display_student()
s1.ch_student_name("god")
s1.display_student()
        
        
        

