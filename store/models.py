from collections import OrderedDict
import datetime

from django.db import models#django  database tizimidan models degan class bor shundan voris olib kel, yoki ishlat

# Create your models here.
class Category(models.Model):#avtomatik primary key orqali ID yaratilib qoyiladi , 1 2 3 4 5 
    name = models.CharField(max_length=20)#char turiga tegishli string matnlar bilan ishlovchi ozgaruvchi hoat
    @staticmethod #decorator , staticmethod , property - ochiq , yopiq malumot uchun ishlaydigan 
    def get_all_categories():#olib kel , hamma categoriyani olib kel
        return Category.objects.all()

    def __str__(self):#classlarda __str__ printni vazifasini bajaradi , admin qismi uchuun ishlatiladi , agar __str__deb belgilanmasa category object 1, categoriy object 2 ....  
        return self.name #admin qismida nomi korastilsin

class Product(models.Model): 
    name = models.CharField(max_length=50)
    price = models.IntegerField()#butun son turida narxi 50000 som
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)#primary key va foreinKey bor bularni farqi, primary key bu - birinchi kalit, aynan bir modelga tegishli boladi, ForeinKey bu tashqi kalit , yani boshqa modelga ulanishni amalga oshiradi , category bu ozi alohida model va product modeli category modelga tashqi kalit orqali ulaniadi, 1 ga 1, kopga kop, kopga bir  
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod#id bu identifikasion raqam, bu primary ketdan 
    def get_products_by_id(ids):
        return Product.object.filter(id_in=ids)

    @staticmethod
    def get_all_products():   
        return Product.object.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:#man tanlagan category mavjud bo'lsa 
            return Product.objects.filter(category=category_id) 
        else:
            return Product.get_all_products()

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)

    def register(self):
        self.save()
    @staticmethod
    def get_customer_by_email(email):
        try:#if == try
            return Customer.objects.get(email=email)
        except:
            return False
    def isExists(self):
        if Customer.object.filter(email=self.email):
            return True
        return False         



class order(models.Model):
    product = product = models.ForeignKey(Product,on_delete=models.CASCADE)#models.CASCADE, agar tanlangan product to'liq bazadan o'chirib tashlansa, unga tegishli hamma ma'lumot to'liq o'chrib yuborilsin
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50,default='',blank=True)
    phone = models.CharField(max_length=50,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    def placeOrder(self):#buyurtmani tasdiqlash
        self.save()#buyurtma saqlnsin

    @staticmethod
    def get_orders_by_customer(customer_id):#mijozaga tegishli buyurtmalarni olib kelib berish
        return OrderedDict.objects.filter(customer=customer_id).order_by('-date')



#class Turkum(models.Model):#category
