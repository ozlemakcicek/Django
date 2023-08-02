import os
os.system('cls' if os.name == 'nt' else 'clear')

print("-------------------------------------")




#!Topics to be Covered:

#* Everything in Python is class
#? Defining class
#* Defining class attributes
#? Difference between class attributes and instance attributes
#* SELF keyword
#? Static methods
#* Special methods (init, str)
#? 4 pillars of OOP:
#     Encapsulation
#     Abstraction
#     Inheritance
#        Multiple inheritance
#     Polymorphism
#        Overriding methods
#* Inner class







#!Everything in Python is class
print("hello")

def print_types(data):
    for i in data:
        print(i,type(i))


test=[122,"henry",[1,2,3],{1,2,3},(1,2,3), True,lambda x:x]     
print_types(test)  




#! Defining class(byk harfle baslanir.4space or tab ile classa attribute ekle.o classdan istedgn kadar nesne olstrblrsn.)

class Person:
    company = "clarusway"
    department = "IT"

person1=Person()
person2=Person()

print(person1.company)


#* class a  yeni bir attribut ekleyince o nesnelere(instance) de gecer
Person.job = "developer"
print(person1.job)


#* nesnenin(instance) birisine eklenen attribute diger instance i etkilemez
person2.location = "Germany"
# print(person1.location) # AttributeError




#! SELF keyword
#* classa birde fonksiyon ekliyoruz ve buna method denilir.instanceler ona da ulasablr

class Person:
    company = "clarusway"
    department = "IT"

    # def test():  # TypeError asagidaki cagirmaya gore. aciklamasi altta
    def test(self):
        print("test")

person1=Person()
person2=Person()

# person1.test() # bunu calistirinca TypeError verir.cunku arka planda  Person.test(person) seklinde class.method(nerden cagirisan onun adi) olarak gonderir.halbuki def test() de bir argmnt koymadik.buna engel olmak icin baslangicta herhngi bir attrbt ver.self diye basepractis olarak veririz bunu



# 2.bir method kullanalim.birkac attribute yazblrz
class Person:
    company = "clarusway"
    department = "IT"


    def set_details(self,name,age):
        self.name=name
        self.age=age  

    def get_details(self):
        print(self.name, self.age)


person1=Person()
person2=Person()

person1.set_details("barry",40)
person2.set_details("henry",20)

print(person2.age)



#! Static methods   : @staticmethod decoratoru
# self gorduklerimiz instance a gore farkli calisir.instance lara gore farkli calissin istemezsek herkese gore ayni ,statik bir method istersek @staticmethod koyariz

class Person:
    company = "clarusway"
    department = "IT"


    @staticmethod
    def salute():
        print("Hi there!")


person1=Person()
person2=Person()

person1.salute()
person2.salute()



#! Special Methods(init,str)
# iki underscore,bosluk, method ismi ve tekrar iki underscore seklinde tanimlanir
#nesne create ederken  nesnenin ozelliklerini set edeblrz init ile.NameError


#* 4 pillars of OOP
#!  Encapsulation methods: kullanicilarin neye nekadar ulasilabilecegini saglayan method __ile disaridan ulasilamaz yapip,_ile ulasilabilir yapariz
#!  Abstraction methods: fiziken yazdigimiz bisey degil.mesela my_list i siralamada arka plandaki olacak olanlari bilmeye gerek yok.OOP nin bize sagladigi bir guzellik

class Person:
    company = "clarusway"
    department = "IT"
    


    def __init__(self,name,age):
       self.name=name
       self.age=age
       self._salary=3000 # tek underscore ile disaridan da ulasilabilir yapariz
       self.__id=35 # iki underscore ile disaridan ulasilamaz kilariz 

    def __str__(self):
        return f"{self.name}-{self.age}" # f string; string ifade icine degsiken koyabiliriz {} icinde

person1= Person("Hasan",25)
print(person1.name)

# print(person1)# bu sekilde pek anlamli bir cikti almayiz.bunu str methodu ile anlamlandirirz.ustte str yi yazdiktan sonra print edebiliriz bu sekilde

print(person1)
print(person1._salary)
person1._salary=4000
print(person1._salary)
# print(person1.__id) # AttributeErrror verir.yukarida __ ile koruma altina aliyrz
# python buna da bir cozum bulmus.ulasilabilir ve degistirilebilir
print(person1._Person__id)


#? class imiz bir tabloya denk gelecek django da.tanimlanan instance lar dao tablodaki elemanlar olacak

my_list =[3,4,1,5]
my_list.sort()
print(my_list) # Abstraction ile bizim hicbirsey yapmamiza gerek olmadan siralar



#! Inheritance methods. miras alma

class Person:
    company = "Clarusway"
  
    


    def __init__(self,name,age):
       self.name=name
       self.age=age
      
    def __str__(self):
        return f"{self.name}-{self.age}" # f string; string ifade icine degsiken koyabiliriz {} icinde

    def get_details(self):
        print(self.name, self.age)

#* birden fazla classin ozelligini tek bir classta toplayablrz
class Lang:
    def __init__(self,lang):
        self.lang=lang

    def display_langs (self):
        print(self.lang)       


class Employee(Person,Lang):  # Person classini miras alarak yeni bir class urettik ve onun herseyini aldi.once kendi uzerinde varmi diye bakar.varsa onu kullanir yoksa Person dan alir
    
    def __init__(self,name,age,path,lang,location="Germany"):
        # self.name=name
        # self.age=age
        super().__init__(name,age)# tek tek tanimlamaya gerek yok name ve age icin zaten parent da var.super()ile yapariz
        self.path=path
        # self.lang=lang
        Lang.__init__(self,lang)
        self.location=location


#! Polymorphism  method: parent dakinin disinda biseyler yazmak istersek..
   #bu sekilde sadece parent daki get_details fonksiyonunda tanimlanan name ve age i verir bize
   #emp1=Employee("victor",33,["fullstack","devops"])
   #emp1.get_details()

#? emp1 deki language larin gozukmesi icin parent dakini degistirmiyoruz cunku baska instance larda kullanabilir bunu.o yuzden o methodu alip kendine gore custumize yapacagiz
# buna overriding diyoruz .yine bunu tek tek yazmaktansa super ile direkt tasiyabiliriz ve uzerine kendimiz de biseyler ekleyeblrz 
   
    # def get_details(self):
    #     print(self.name, self.age,self.path)

    def get_details(self):
      super().get_details() # self yazmaya gerek yok 
      print(self.path)
      Lang.display_langs(self) # class adi ile cagirirken self yazmaliyiiz


emp1=Employee("victor",33,["fullstack","devops"],["python","javascript"])

emp1.get_details()
print(emp1.location)
# emp1.display_langs() # get_details altina ekleyince ayriyeten yazmaya gerek olmaz




##*************************************************##
#! hangi class lardan miras almis onu gormek icin mro() kullanilir
# print(Employee.mro())

#! bir nevi mr cekme.bunu yazinca iskeleti doker.cikmak icin ..q yap terminalde
# print(help(Employee))

print(emp1.__dict__)  # detayli key:value seklinde verir


##************************************************##
#? inherit class.ic ice class larda settings yapar.class Meta: ile yapariz bunu
from django.db import models

class Makale(models.Model):
    adi=models.CharField(max_length=30)
    yazari=models.CharField(max_length=30)

    class Meta:
        ordering = ["yazari"]







print("-------------------------------------")