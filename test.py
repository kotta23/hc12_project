class  Techer():
        attr_2 =12412
        def __init__(self , tech_name):
                self.tech_name = tech_name

class Student(Techer):
        attr = '12412' #class variable
        def __init__(self , name , sub1 , sub2 , sub3,tech_name):
                self.name  = name # instance variable
                self.__sub1  = sub1
                self.sub2  = sub2
                self.sub3  = sub3
                Techer.__init__(self,tech_name)

        def get_name (self):
                print(f'my name is {self.name}')

        def set_name(self,n_name):
                self.name = n_name

x = Student('ahmed' , 'math','physi' ,'chem','taha' )
x.attr
x.get_name()
x.set_name('djhf')
x.get_name()
print(x.attr_2)
print(x.tech_name)
