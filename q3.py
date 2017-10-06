class employee:
    raise_amt=1.04

    def __init__(self,firstname,lastname,pay):
        self.firstname= firstname
        self.lastname=lastname
        self.pay=pay
        self.email=firstname+'.'+lastname+'@company.com'

    def apply_raise(self):
        self.pay=self.pay*self.raise_amt



class student:

    def __init__(self,firstname,lastname,ID):
        self.firstname=firstname
        self.lastname=lastname
        self.ID=ID

class book:

    def __init__(self,Name,Author,Bookid):#init and self

         self.name=Name
         self.auth=Author
         self.id=Bookid
class librarian(employee):#single inheritence
   raise_amt=1.10
   def __intit__(self,firstname,lastname,pay,deskno):
       super().__init__(firstname,lastname,pay)
       self.deskno=deskno


class student_employee(student,employee)  :  #multiple inheritence

    raise_amt=1.02
    def __init__(self,firstname,lastname,ID,pay):
        #super().__init__(self,firstname,lastname,ID,pay)
       self.firstname=firstname
       self.lastname=lastname
       self.__ID=ID    #private ID
       self.pay=pay

emp1=employee('atanu','maiti',50000)
lib1=librarian('tom','fg',5000)

print(emp1.pay)
print(lib1.pay)

emp1.apply_raise()
lib1.apply_raise()

print(emp1.pay)
print(lib1.pay)



stu_emp1=student_employee('abc','xyz','34BA',50000)
stu_emp1.apply_raise()
print(stu_emp1.pay)


