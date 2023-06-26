from django.db import models
from django.contrib.auth.models import User
#Ecommerce ,1234
# Create your models here.
STATE_CHOICES=(
    ('Bihar','Bihar'),
    ('Jharkhand','Jharkhand'),
    ('WestBengal','WestBengal'),
    ('Maharastra','Mharastra'),
    ('Orissa',"Orissa"),
    ('Telegana','Telegana'),
    ('Tamilnadu','Tamilnadu'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Punjab','Punjab'),
    ('Haryana','Haryana'),
    ('Rajasthan','Rajasthan'),
    ('Uttarakhand','Uttrakhand'),
    ('Madhya Pradesh','madhya Pradesh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Sikkim','Sikkim'),
    ('Assam','Assam'),
    ('Nagaland','Nagaland'),
    ('Arunchal Pradesh','Arunchal Pradesh'),
    ('Tripura','Tripura'),
    ('Mizoram','Mizorm'),
    ('Meghalaya','Meghalaya'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Kerela','Kerela'),
    ('Karnatka','Karnatka'),
    ('Himachal Pradesh','Himachal Pradesh'),
     ('New Delhi','New Delhi'),
     ('Jammu','Jammu'),
     ('Kashmir','kashmir'),
     ('Pudducherry','Pudducherry'),
)     


CATEGORY_CHOICES=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','Milkshake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-Creams'),
    ('BL','Butter-Milk'),
    ('ST','Sweets'),
    
)
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    discription=models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='product')
    def __str__(self):
        return self.title


class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=55)
    mobile=models.IntegerField(default=0)
    pincode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)


    def __str__(self):
        return self.name+self.city
    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
    
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Deleiverd','Deliverd'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),

)    
class Payment(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     amount=models.FloatField()
     razor_order_id=models.CharField(max_length=100,blank=True,null=True)
     razor_payment_status=models.CharField(max_length=100,blank=True,null=True)
     razor_payment_id=models.CharField(max_length=100,blank=True,null=True)
     paid=models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE )    
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customers')
    product=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='products')
    quantity=models.PositiveIntegerField(default=1)
    orderd_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
    